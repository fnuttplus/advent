#include <stdio.h>
#define SANTA 1

struct Santa{
	int x;
	int y;
};

int main(){
	char c;
	int grid[200][200];
	struct Santa santa;
	struct Santa robo;
	int turn = SANTA;
	int n = SANTA;
	FILE * file = fopen("advent3.txt", "r");
	int x,y;
	for (x = 0; x < 200; x ++){
		for (y = 0; y < 200; y++){
			grid[x][y] = 0;
		}
	}
	santa.x = 50;
	santa.y = 50;
	robo.x = 50;
	robo.y = 50;
	grid[50][50] = SANTA;
	while((c = fgetc(file)) != EOF){
		n += move(turn == SANTA ? &santa : &robo, c, grid);
		turn ^= SANTA;
	}
	printf("\n%d\n",n);
	exit(0);
}

int move (struct Santa *santa, int c, int grid[][200]) {
	if (c == 62) santa->x++;
	else if (c == 94) santa->y--;
	else if (c == 118) santa->y++;
	else if (c == 60) santa->x--;

	if (grid[santa->x][santa->y] == 0) {
		grid[santa->x][santa->y] = SANTA;
		return SANTA;
	}
	return 0;
}

//part 1:
//24,105,33,177
//2592

//part 2:
//11,101,27,142
//2360
