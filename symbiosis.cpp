#include <stdio.h>
#include <winsock2.h>
#include <windows.h>
#include <XInput.h>
#include <dsound.h>
#include <math.h>

#define PLAYSOUND 0

#pragma comment(lib,"ws2_32.lib") //Winsock Library

#define BUFLEN 512  //Max length of buffer
#define PORT 5324   //The port on which to listen for incoming data

#define COLOR_WHITE (UINT64) 0xFFFFFFFF
#define COLOR_BLACK (UINT64) 0xFF000000
#define COLOR_GREEN (UINT64) 0xFF00FF00
#define COLOR_BLUE (UINT64) 0xFF0000FF
#define COLOR_RED (UINT64) 0xFFFF0000
#define COLOR_YELLOW (UINT64) 0xFFFFFF00

#define PI 3.1415926535f

typedef unsigned char uint8;

static bool running;
static LPRECT clientRect;

struct BitmapBuffer
{
	BITMAPINFO Info;
	void *Memory;
	int Width;
	int Height;
	int BytesPerPixel;
};

struct SoundSettings
{
	int SamplesPerSecond;
	int ToneHz;
	int WavePeriod;
	int HalfWavePeriod;
	int BytesPerSample;
	int SecondaryBufferSize;
	int ToneVolume;
	UINT32 RunningSampleIndex;
	float tSine;
	int LatencySamples;			/* How far ahead of cursor to write */
};

struct Box
{
	short x;
	short y;
};

struct UDPStruct
{
	uint8 length;
	Box *boxes;
};

struct Platform {
	Box pos;
	Box size;
	UINT64 color;
	Platform()
	{
		pos.x = 0;
		pos.y = 0;
		size.x = 0;
		size.y = 0;
		color = COLOR_BLACK;
	}
	Platform(short x, short y, short width, short height, UINT64 c)
	{
		pos.x = x;
		pos.y = y;
		size.x = width;
		size.y = height;
		color = c;
	}
	void update()
	{

	}
	void draw(BitmapBuffer *Bitmap) {
		UINT32 *pixel = (UINT32*)Bitmap->Memory;
		for (int y = pos.y; y < pos.y+size.y; y++)
		{
			for (int x = pos.x; x < pos.x+size.x; x++)
			{
				if (x > 0 && x < Bitmap->Width && y > 0 && y < Bitmap->Height)
				{
					pixel[y*Bitmap->Width+x] = (UINT64) ((y*10 << 16) | (y*10 << 8) | y*20);;
				}
			}
		}
	}
};

struct Guy
{
	LARGE_INTEGER Frequency;
	LARGE_INTEGER JumpTimeStart;

	Box pos;
	UINT64 color;
	Guy()
	{
		QueryPerformanceFrequency(&Frequency);
	}
	void jump() {
		LARGE_INTEGER EndingTime, ElapsedMicroseconds;

		if (JumpTimeStart.QuadPart == 0)
		{
			QueryPerformanceCounter(&JumpTimeStart);
			pos.y -= 20;
		}

		else {
			QueryPerformanceCounter(&EndingTime);
			ElapsedMicroseconds.QuadPart = EndingTime.QuadPart - JumpTimeStart.QuadPart;
			ElapsedMicroseconds.QuadPart *= 1000000;
			ElapsedMicroseconds.QuadPart /= Frequency.QuadPart;

			if (ElapsedMicroseconds.QuadPart < 200000) {
				pos.y -= 20;
			}
		}
	}
	void update(Platform *platforms, int l, Box *boxes, int b) {
		for ( int i = 0; i < l; i++)
		{
			if ((pos.x > platforms[i].pos.x && pos.x < platforms[i].pos.x + platforms[i].size.x) && (pos.y+20 < platforms[i].pos.y+platforms[i].size.y && pos.y+20 > platforms[i].pos.y))
			{
				pos.y = platforms[i].pos.y-20;
				JumpTimeStart.QuadPart = 0;
			}
		}

		for ( int i = 0; i < b; i++)
		{
			if ((pos.x > boxes[i].x-20 && pos.x < boxes[i].x+20) && (pos.y+20 < boxes[i].y+20 && pos.y+20 > boxes[i].y-20))
			{
				pos.y = boxes[i].y-30;
				JumpTimeStart.QuadPart = 0;
			}
		}

		if (pos.y < 700) {
			pos.y += 10;
		} else {
			JumpTimeStart.QuadPart = 0;
		}
	}
	void draw(BitmapBuffer *Bitmap) {
		UINT32 *pixel = (UINT32*)Bitmap->Memory;
		for (int y = pos.y-20; y < pos.y+20; y++)
		{
			for (int x = pos.x-20; x < pos.x+20; x++)
			{
				if (x > 0 && x < Bitmap->Width && y > 0 && y < Bitmap->Height)
				{
					pixel[y*Bitmap->Width+x] = color;
				}
			}
		}
	}
};

//static SoundSettings GlobalSoundSettings;
static UDPStruct BoxCords;
static BitmapBuffer GlobalBitmap;
static LPDIRECTSOUNDBUFFER GlobalSecondaryBuffer;
static Guy guy;
#define PLATFORM_Q 5
static Platform platforms[PLATFORM_Q];

static SOCKET Socket;
static sockaddr_in ClientAddr;
int slen = sizeof(ClientAddr);

struct WindowDimensions
{
	int Width;
	int Height;
};

#define _XInputGetState_(name) DWORD WINAPI name(DWORD dwUserIndex, XINPUT_STATE* pState)
typedef _XInputGetState_(_XInputGetState);
_XInputGetState_(_XInputGetStateStub) { return ERROR_API_UNAVAILABLE; }
static _XInputGetState* XInputGetState_ = _XInputGetStateStub;
#define XInputGetState XInputGetState_

#define _XInputSetState_(name) DWORD WINAPI name(DWORD dwUserIndex, XINPUT_VIBRATION* pVibration)
typedef _XInputSetState_(_XInputSetState);
_XInputSetState_(_XInputSetStateStub) { return ERROR_API_UNAVAILABLE; }
static _XInputSetState* XInputSetState_ = _XInputSetStateStub;
#define XInputSetState XInputSetState_

#define _DirectSoundCreate_(name) HRESULT WINAPI name(LPCGUID pcGuidDevice, LPDIRECTSOUND *ppDS, LPUNKNOWN pUnkOuter)
typedef _DirectSoundCreate_(_DirectSoundCreate);

static void LoadXInput()
{
	HMODULE XInputLibrary = LoadLibraryA("xinput1_4.dll");
	if (!XInputLibrary) XInputLibrary = LoadLibraryA("xinput9_1_0.dll");
	if (!XInputLibrary) XInputLibrary = LoadLibraryA("xinput1_3.dll");
	if (XInputLibrary)
	{
		XInputGetState = (_XInputGetState*)GetProcAddress(XInputLibrary, "XInputGetState");
		XInputSetState = (_XInputSetState*)GetProcAddress(XInputLibrary, "XInputSetState");
	}
}

static void Win32InitDSound(HWND Window, int SamplesPerSecond)
{
	HMODULE DSoudLibrary = LoadLibraryA("dsound.dll");

	if (DSoudLibrary)
	{
		_DirectSoundCreate* DirectSoundCreate = (_DirectSoundCreate*) GetProcAddress(DSoudLibrary, "DirectSoundCreate");

		LPDIRECTSOUND DirectSound;
		if (DirectSoundCreate && SUCCEEDED(DirectSoundCreate(0, &DirectSound, 0)))
		{
			WAVEFORMATEX WaveFormat = {};
			WaveFormat.cbSize = 0;
			WaveFormat.nChannels = 2;
			WaveFormat.nSamplesPerSec = SamplesPerSecond;
			WaveFormat.wBitsPerSample = 16;
			WaveFormat.wFormatTag = WAVE_FORMAT_PCM;
			WaveFormat.nBlockAlign = 4; //(WaveFormat.nChannels*WaveFormat.wBitsPerSample) /8;
			WaveFormat.nAvgBytesPerSec = WaveFormat.nSamplesPerSec*WaveFormat.nBlockAlign;

			if (SUCCEEDED(DirectSound->SetCooperativeLevel(Window, DSSCL_PRIORITY)))
			{
				DSBUFFERDESC BufferDescription = {};
				BufferDescription.dwSize = sizeof(BufferDescription);
				BufferDescription.dwFlags = DSBCAPS_PRIMARYBUFFER;

				LPDIRECTSOUNDBUFFER PrimaryBuffer;
				if (SUCCEEDED(DirectSound->CreateSoundBuffer(&BufferDescription, &PrimaryBuffer, 0)))
				{
					if (HRESULT Error = PrimaryBuffer->SetFormat(&WaveFormat))
					{
						OutputDebugStringA("Sound Buffer Error\n");
					}
				}
			}

			DSBUFFERDESC BufferDescription = {};
			BufferDescription.dwSize = sizeof(BufferDescription);
			BufferDescription.dwFlags = 0;
			BufferDescription.dwBufferBytes = SamplesPerSecond*4;
			BufferDescription.lpwfxFormat = &WaveFormat;
			
			//LPDIRECTSOUNDBUFFER SecondaryBuffer = GlobalSecondaryBuffer;
			if (HRESULT Error = DirectSound->CreateSoundBuffer(&BufferDescription, &GlobalSecondaryBuffer, 0))
			{
				OutputDebugStringA("Sound Buffer Error\n");
			}

		}
	}
}

static WindowDimensions GetWindowDimensions(HWND Window)
{
	WindowDimensions Result;
	RECT clientRect;
	GetClientRect(Window, &clientRect);
	Result.Width = clientRect.right - clientRect.left;
	Result.Height = clientRect.bottom - clientRect.top;

	return Result;
}

static void RenderWeirdGradient(BitmapBuffer *Bitmap, int offsetX, int offsetY)
{
	UINT32 *pixel = (UINT32*)Bitmap->Memory;

	for (int y = 0; y < Bitmap->Height; y++)
	{
		for (int x = 0; x < Bitmap->Width; x++)
		{
			uint8 blue = (x + offsetX); //Blue
			uint8 green = (y + offsetY); //Green
			uint8 red = 255; //Red
			uint8 pad = 0; //Pad

			*pixel++ = (UINT64) ((red << 16) | (green << 8) | blue);
		}

	}
	pixel = (UINT32*)Bitmap->Memory;
	//Draw Boxes from android
	for (int i = 0; i < BoxCords.length; i++)
	{
		if (BoxCords.boxes[i].x == 0 && BoxCords.boxes[i].y == 0) continue;
		for (int y = BoxCords.boxes[i].y-20; y < BoxCords.boxes[i].y+20; y++)
		{
			for (int x = BoxCords.boxes[i].x-20; x < BoxCords.boxes[i].x+20; x++)
			{
				if (x > 0 && x < Bitmap->Width && y > 0 && y < Bitmap->Height)
				{
					pixel[y*Bitmap->Width+x] = (UINT64) 0xFFFFFFFF;
				}
			}
		}
	}

}

static void Win32ResizeDIBSection(BitmapBuffer *Bitmap, int width, int height)
{
	if (Bitmap->Memory)
	{
		VirtualFree(Bitmap->Memory, 0, MEM_RELEASE);
	}

	Bitmap->Width = width;
	Bitmap->Height = height;
	Bitmap->BytesPerPixel = 4;

	Bitmap->Info.bmiHeader.biSize = sizeof(Bitmap->Info.bmiHeader);
	Bitmap->Info.bmiHeader.biWidth = Bitmap->Width;
	Bitmap->Info.bmiHeader.biHeight = -Bitmap->Height;
	Bitmap->Info.bmiHeader.biPlanes = 1;
	Bitmap->Info.bmiHeader.biBitCount = 32;
	Bitmap->Info.bmiHeader.biCompression = BI_RGB;

	int bitmapMemorySize = Bitmap->BytesPerPixel*Bitmap->Width*Bitmap->Height;
	Bitmap->Memory = VirtualAlloc(0, bitmapMemorySize, MEM_COMMIT, PAGE_READWRITE);

}

static void Win32DrawBitmap(BitmapBuffer *Bitmap, HDC DeviceContext, int WindowWidth, int WindowHeight)
{
	StretchDIBits(DeviceContext, 
		0, 0, WindowWidth, WindowHeight, 
		0, 0, Bitmap->Width, Bitmap->Height, 
		Bitmap->Memory, &Bitmap->Info, DIB_RGB_COLORS, SRCCOPY);
}

static void FillSoundBuffer(SoundSettings* Settings, DWORD ByteToLock, DWORD BytesToWrite)
{
	
	void* Region1;
	DWORD Region1Size;
	void* Region2;
	DWORD Region2Size;
					
	if (SUCCEEDED(GlobalSecondaryBuffer->Lock(ByteToLock, BytesToWrite, &Region1, &Region1Size, &Region2, &Region2Size, 0)))
	{
		INT16* SampleOut = (INT16*) Region1;
		DWORD Region1SampleCount = Region1Size/Settings->BytesPerSample;
		for (DWORD SampleIndex = 0; SampleIndex < Region1SampleCount; SampleIndex++)
		{
			Settings->tSine += 2.0f*PI/(float)Settings->WavePeriod;
			INT16 SampleValue = (INT16)(Settings->ToneVolume * sinf(Settings->tSine));
			*SampleOut++ = SampleValue;
			*SampleOut++ = SampleValue;

			Settings->RunningSampleIndex++;
		}
		SampleOut = (INT16*) Region2;
		DWORD Region2SampleCount = Region2Size/Settings->BytesPerSample;
		for (DWORD SampleIndex = 0; SampleIndex < Region2SampleCount; SampleIndex++)
		{
			Settings->tSine += 2.0f*PI/(float)Settings->WavePeriod;
			INT16 SampleValue = (INT16)(Settings->ToneVolume * sinf(Settings->tSine));
			*SampleOut++ = SampleValue;
			*SampleOut++ = SampleValue;

			Settings->RunningSampleIndex++;
		}

		GlobalSecondaryBuffer->Unlock(Region1, Region1Size, Region2, Region2Size);
	}
}

LRESULT CALLBACK Win32MainWindowCallback(HWND window, UINT message, WPARAM wParam, LPARAM lParam)
{
	LRESULT result = 0;

	switch (message)
	{	
	case WM_SIZE:
	{
		//WindowDimensions WD = GetWindowDimensions(window);
		//Win32ResizeDIBSection(&GlobalBitmap, WD.Width, WD.Height);
		OutputDebugStringA("WM_SIZE\n");
	} break;

	case WM_DESTROY:
		running = false;
		break;
	
	case WM_CLOSE:
		running = false;
		break;
	
	case WM_ACTIVATEAPP:
		//OutputDebugStringA("WM_ACTIVATEAPP\n");
		
		break;
	
	case WM_SYSKEYDOWN:
	case WM_SYSKEYUP:
	case WM_KEYDOWN:
	case WM_KEYUP:
		{
			bool WasDown = ((lParam & (1 << 30)) != 0);
			bool IsDown = ((lParam & (1 << 31)) == 0);

			UINT32 VKCode = wParam;
			if (VKCode == 'W')
			{
				if (IsDown != WasDown) OutputDebugStringA("W\n");
				if (IsDown) OutputDebugStringA("IsDown\n");
				if (WasDown) OutputDebugStringA("WasDown\n");
			}
		}
		break;


	case WM_PAINT:
	{
		PAINTSTRUCT paint;
		HDC deviceContext = BeginPaint(window, &paint);

		WindowDimensions WD = GetWindowDimensions(window);
		Win32DrawBitmap(&GlobalBitmap, deviceContext, WD.Width, WD.Height);
		EndPaint(window, &paint);
		OutputDebugStringA("PAINT\n");

	} break;

	default:
		//OutputDebugStringA("default\n");
		result = DefWindowProc(window, message, wParam, lParam);
		break;
	}
	return result;
}


UDPStruct BufToMessage(char* buf)
{
	UDPStruct message;
	uint8 l = buf[0];
	message.length = l;
	message.boxes = new Box[l];
	for (int i = 0; i < l; i++)
	{	//Converting from byte array to signed short
		message.boxes[i].x = (short) ((buf[2+i*4] << 8) & 0xff00) | (buf[1+i*4] & 0xff);
		message.boxes[i].y = (short) ((buf[4+i*4] << 8) & 0xff00) | (buf[3+i*4] & 0xff);
	}
	return message;
}

DWORD WINAPI NetworkThread(LPVOID lpParameter)
{
	int recv_len;
	int slen = sizeof(ClientAddr);
	char buf[69];
	while (running)
	{
		memset(buf,'\0', 69);
		if ((recv_len = recvfrom(Socket, buf, BUFLEN, 0, (struct sockaddr *) &ClientAddr, &slen)) > 0)
		{
			BoxCords = BufToMessage(buf);
		}
		if (recv_len == SOCKET_ERROR)
		{
			int asdf = WSAGetLastError();
		}

	}
	return 0;
}

DWORD WINAPI SenderThread(LPVOID lpParameter)
{
	int slen = sizeof(ClientAddr);
	char buf[4];

	while (running)
	{
		buf[0] = (byte) (guy.pos.x & 0xff);
		buf[1] = (byte) ((guy.pos.x >> 8) & 0xff);
		buf[2] = (byte) (guy.pos.y & 0xff);
		buf[3] = (byte) ((guy.pos.y >> 8) & 0xff);

		if (sendto(Socket, buf, 4, 0, (struct sockaddr*) &ClientAddr, slen) == SOCKET_ERROR) ;//TODO: handle error
		Sleep(20);

	}
	return 0;
}

int CALLBACK WinMain(
	HINSTANCE hInstance,
	HINSTANCE hPrevInstance,
	LPSTR CmdLine,
	int CmdShow)
{


	if (CmdLine[0])
		MessageBoxA(0,CmdLine,"CmdLine",MB_OK|MB_ICONINFORMATION);
	LoadXInput();
	WNDCLASSA windowClass = {};

	Win32ResizeDIBSection(&GlobalBitmap, 1280, 752);

	windowClass.style = CS_OWNDC|CS_HREDRAW|CS_VREDRAW;
	windowClass.lpfnWndProc = Win32MainWindowCallback;
	windowClass.hInstance = hInstance; //GetModuleHandle(0);
	
	windowClass.lpszClassName = "HandmadeHero";

	if (RegisterClassA(&windowClass))
	{
		HWND Window = CreateWindowExA(0, windowClass.lpszClassName, "Handmade Hero", WS_OVERLAPPEDWINDOW|WS_VISIBLE, 
			CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,
			0, 0, hInstance, 0);
		if (Window)
		{
			running = true;
			
			struct sockaddr_in server;
			WSADATA wsa;

			if (WSAStartup(MAKEWORD(2,2),&wsa) != 0) return 0;
			if((Socket = socket(AF_INET , SOCK_DGRAM , 0 )) == INVALID_SOCKET) return 0;

			server.sin_family = AF_INET;
			server.sin_addr.s_addr = INADDR_ANY;
			server.sin_port = htons( PORT );

			if( bind(Socket ,(struct sockaddr *)&server , sizeof(server)) == SOCKET_ERROR) return 0;
			CreateThread(0,0,SenderThread,NULL,0,NULL);
			HANDLE network_thread = CreateThread(0,0,NetworkThread,NULL,0,NULL);

			//Graphics test
			int Xoffset = 0;
			int Yoffset = 0;

			HDC deviceContext = GetDC(Window);

#if PLAYSOUND
			//Sound test
			SoundSettings GlobalSoundSettings;
			GlobalSoundSettings.SamplesPerSecond = 48000;
			GlobalSoundSettings.ToneHz = 300;
			GlobalSoundSettings.WavePeriod = GlobalSoundSettings.SamplesPerSecond/GlobalSoundSettings.ToneHz;
			GlobalSoundSettings.BytesPerSample = sizeof(INT16)*2;
			GlobalSoundSettings.SecondaryBufferSize = GlobalSoundSettings.SamplesPerSecond*GlobalSoundSettings.BytesPerSample;
			GlobalSoundSettings.ToneVolume = 16000;
			GlobalSoundSettings.RunningSampleIndex = 0;
			GlobalSoundSettings.tSine = 0;
			GlobalSoundSettings.LatencySamples = GlobalSoundSettings.SamplesPerSecond/5;

			Win32InitDSound(Window, GlobalSoundSettings.SamplesPerSecond);

			FillSoundBuffer(&GlobalSoundSettings, 0, GlobalSoundSettings.LatencySamples*GlobalSoundSettings.BytesPerSample);
			GlobalSecondaryBuffer->Play(0, 0, DSBPLAY_LOOPING);
#endif

			guy.pos.x = 100;
			guy.pos.y = 100;
			guy.color = COLOR_BLACK;

			platforms[0] = Platform(100, 600, 100, 20, COLOR_BLACK);
			platforms[1] = Platform(200, 500, 100, 20, COLOR_BLACK);
			platforms[2] = Platform(300, 400, 100, 20, COLOR_BLACK);
			platforms[3] = Platform(550, 400, 100, 20, COLOR_BLACK);
			platforms[4] = Platform(800, 400, 100, 20, COLOR_BLACK);

			while (running)
			{
				MSG message;
				while (PeekMessageA(&message, 0, 0, 0, PM_REMOVE))
				{
					if (message.message == WM_QUIT) running = false;

					TranslateMessage(&message);
					DispatchMessage(&message);
				}

				for (DWORD ControllerIndex = 0; ControllerIndex < XUSER_MAX_COUNT; ControllerIndex++)
				{
					XINPUT_STATE ControllerState;
					if (XInputGetState(ControllerIndex, &ControllerState) == ERROR_SUCCESS)
					{
						//ControllerState.dwPacketNumber
						XINPUT_GAMEPAD *Pad = &ControllerState.Gamepad;
						bool PadA = ((Pad->wButtons & XINPUT_GAMEPAD_A) != 0);
						bool PadB = ((Pad->wButtons & XINPUT_GAMEPAD_B) != 0);
						bool PadX = ((Pad->wButtons & XINPUT_GAMEPAD_X) != 0);
						bool PadY = ((Pad->wButtons & XINPUT_GAMEPAD_Y) != 0);
						if (PadA) {
							guy.color = COLOR_GREEN;
							guy.jump();
						}
						else if (PadB) guy.color = COLOR_RED;
						else if (PadX) guy.color = COLOR_BLUE;
						else if (PadY) guy.color = COLOR_YELLOW;
						else guy.color = COLOR_BLACK;

						short StickX = Pad->sThumbLX;
						short StickY = Pad->sThumbLY;

						if (StickX > XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE || StickX < -XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE) guy.pos.x+= StickX >> 12;
						//if (StickY > XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE || StickY < -XINPUT_GAMEPAD_LEFT_THUMB_DEADZONE) guy.pos.y-= StickY >> 12;
						
						short RStickX = Pad->sThumbRX;
						short RStickY = Pad->sThumbRY;

						if (RStickX > XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE || RStickX < -XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE)
						{
				//			GlobalSoundSettings.ToneHz = 1+((USHORT)(RStickX^(1<<15)) >> 6);
				//			GlobalSoundSettings.WavePeriod = GlobalSoundSettings.SamplesPerSecond/GlobalSoundSettings.ToneHz;
						}

						if (RStickY > XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE || RStickY < -XINPUT_GAMEPAD_RIGHT_THUMB_DEADZONE);
							//GlobalSoundSettings.ToneVolume = (USHORT)(RStickY^(1<<15)) >> 1;

						XINPUT_VIBRATION vibration = {};
						vibration.wLeftMotorSpeed = 0;
						vibration.wRightMotorSpeed = 0;

						if(Pad->bLeftTrigger > 0) vibration.wLeftMotorSpeed = Pad->bLeftTrigger << 8;
						if(Pad->bRightTrigger > 0) vibration.wRightMotorSpeed = Pad->bRightTrigger << 8;
						
						XInputSetState(0, &vibration);

						if (Pad->wButtons & XINPUT_GAMEPAD_START) running = false;
						
					}
				}

				RenderWeirdGradient(&GlobalBitmap, Xoffset,Yoffset);

				for (int i = 0; i < PLATFORM_Q; i++)
				{
					platforms[i].draw(&GlobalBitmap);
				}

				guy.update(platforms, PLATFORM_Q, BoxCords.boxes, BoxCords.length);
				guy.draw(&GlobalBitmap);
#if PLAYSOUND
				DWORD PlayCursor = 0;
				DWORD WriteCursor = 0;
				if (SUCCEEDED(GlobalSecondaryBuffer->GetCurrentPosition(&PlayCursor, &WriteCursor)))
				{
					DWORD ByteToLock = (GlobalSoundSettings.RunningSampleIndex*GlobalSoundSettings.BytesPerSample) % GlobalSoundSettings.SecondaryBufferSize;
					DWORD BytesToWrite;
					DWORD TargetCursor = (PlayCursor + GlobalSoundSettings.LatencySamples*GlobalSoundSettings.BytesPerSample) % GlobalSoundSettings.SecondaryBufferSize;
					if (ByteToLock > TargetCursor)
					{
						BytesToWrite = (GlobalSoundSettings.SecondaryBufferSize - ByteToLock) + TargetCursor;
					}
					else
					{
						BytesToWrite = TargetCursor - ByteToLock;
					}

					FillSoundBuffer(&GlobalSoundSettings, ByteToLock, BytesToWrite);
				}
#endif



				WindowDimensions WD = GetWindowDimensions(Window);
				Win32DrawBitmap(&GlobalBitmap, deviceContext, WD.Width, WD.Height);
			}
			
		    closesocket(Socket);
			WSACleanup();
		}
	}

    return 0;
}