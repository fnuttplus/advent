package com.ezs.touchtest;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.SocketException;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Point;
import android.graphics.PointF;
import android.view.MotionEvent;
import android.view.View;

public class GravityView extends View {

	private UDPSender senderThread;
	private UDPReceiver receiverThread;

	private Paint paint = new Paint();
	private long prevTime;
	private PointF[] planets;
	private short[] guy = new short[2];

	public GravityView(Context context) {
		super(context);

		planets = new PointF[5];
		for (int i = 0; i < 5; i++) {
			planets[i] = new PointF(0, 0);
		}
		guy[0] = -100;
		guy[1] = -100;
		prevTime = System.nanoTime();

		DatagramSocket client_socket = null;
		try {
			client_socket = new DatagramSocket(5324);
		} catch (SocketException e) {
			e.printStackTrace();
		}
		senderThread = new UDPSender(client_socket);
		receiverThread = new UDPReceiver(client_socket);

		new Thread(senderThread, "UDP Sender Thread").start();
		new Thread(receiverThread, "UDP Receiver Thread").start();
	}

	@Override
	protected void onDraw(Canvas canvas) {
		super.onDraw(canvas);

		int dt = (int) (System.nanoTime() - prevTime) / 1000000;
		prevTime = System.nanoTime();

		paint.setColor(Color.WHITE);
		canvas.drawText(Integer.toString(1000 / dt) + " FPS", 20, 20, paint);

		paint.setTextSize(25);
		int i = 0;
		for (PointF planet : planets) {
			if (!planet.equals(0, 0)) {
				canvas.drawCircle(planet.x, planet.y, 40, paint);
				canvas.drawText(Integer.toString(i++), planet.x, planet.y - 45,
						paint);
			}
		}

		canvas.drawRect((float)guy[0]-20, (float)guy[1]-20, (float)guy[0]+20, (float)guy[1]+20, paint);
		invalidate();
	}

	@Override
	public boolean onTouchEvent(MotionEvent event) {

		int pc = event.getPointerCount();
		if (pc > planets.length) {
			planets = new PointF[pc];
			for (int i = 0; i < pc; i++) {
				planets[i] = new PointF(0f,0f);
			}
		}

		switch (event.getActionMasked()) {
		case MotionEvent.ACTION_UP:
			planets[0].set(0, 0);
			break;
		case MotionEvent.ACTION_POINTER_UP:
			int pl = planets.length - 1;
			for (int i = event.getActionIndex(); i < pl; i++) {
				planets[i].set(planets[i + 1]);
			}
			planets[pl].set(0, 0);
			break;
		default: // case MotionEvent.ACTION_MOVE:

			for (int i = 0; i < pc; i++) {
				planets[i].set(event.getX(i), event.getY(i));
			}
			break;
		}

		synchronized (senderThread) {
			UDPStruct message = new UDPStruct(planets);
			senderThread.Message = message;
			senderThread.notify();
		}
		return true;
	}

	@Override
	public void onSizeChanged(int w, int h, int oldw, int oldh) {
		super.onSizeChanged(w, h, oldw, oldh);
	}

	private class UDPStruct {
		private byte[] Bytes;
		private int Length;

		public UDPStruct(PointF[] planets) {
			Length = 1 + planets.length * 4;
			byte[] b = new byte[Length];
			b[0] = (byte) planets.length; // overflow > 127
			for (int i = 0; i < planets.length; i++) {
				short x = (short) Math.floor(planets[i].x);
				short y = (short) Math.floor(planets[i].y);

				b[1 + i * 4] = (byte) (x & 0xff);
				b[2 + i * 4] = (byte) ((x >> 8) & 0xff);
				b[3 + i * 4] = (byte) (y & 0xff);
				b[4 + i * 4] = (byte) ((y >> 8) & 0xff);
			}
			Bytes = b;
		}

		public byte[] getBytes() {
			return Bytes;
		}

		public int length() {
			return Length;
		}

	}

	// https://www.safaribooksonline.com/library/view/efficient-android-threading/9781449364120/ch04.html
	private class UDPSender implements Runnable {
		public UDPStruct Message;
		DatagramSocket ClientSocket;

		UDPSender(DatagramSocket client_socket) {
			ClientSocket = client_socket;
		}

		@Override
		public void run() {
			InetAddress IPAddress;
			try {
				IPAddress = InetAddress.getByName("192.168.1.16");

				while (true) { // app is running
					synchronized (this) {
						this.wait();
						DatagramPacket send_packet = new DatagramPacket(
								this.Message.getBytes(), this.Message.length(),
								IPAddress, 5324);
						ClientSocket.send(send_packet);

					}
				}

			} catch (IOException e) {

			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
	private class UDPReceiver implements Runnable {
		DatagramSocket ClientSocket;

		UDPReceiver(DatagramSocket client_socket) {
			ClientSocket = client_socket;
		}

		@Override
		public void run() {
			byte[] rData = new byte[4];
			try {
				while (true) { // app is running
					DatagramPacket receive_packet = new DatagramPacket(
							rData, rData.length);
					ClientSocket.receive(receive_packet);
					guy[0] = (short) (((rData[1] << 8) & 0xff00) | (rData[0] & 0xff));
					guy[1] = (short) (((rData[3] << 8) & 0xff00) | (rData[2] & 0xff));
				}

			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}