//It's a Game of Lights
#include <stdio.h>

int grid[100][100];
int ngrid[100][100];

int alive_neighbors(int x, int y) {
	int n = 0;
	if (x > 0) {
		n += grid[x-1][y];
		if (y > 0) n += grid[x-1][y-1];
		if (y < 99) n += grid[x-1][y+1];
	}
	if (x < 99){
		n += grid[x+1][y];
		if (y < 99) n += grid[x+1][y+1];
		if (y > 0) n += grid[x+1][y-1];
	}
	if (y > 0) n += grid[x][y-1];
	if (y < 99) n += grid[x][y+1];
	return n;
}

void update(){
	int x,y,n;
	for (x = 0; x < 100; ++x) {
		for (y = 0; y < 100; ++y) {
			n = alive_neighbors(x,y);
			ngrid[x][y] = grid[x][y];
			if (grid[x][y] && n < 2 || n > 3)
					ngrid[x][y] = 0;
			else if (!grid[x][y] && n == 3)
					ngrid[x][y] = 1;
		}
	}
	for (x = 0; x < 100; ++x) {
		for (y = 0; y < 100; ++y) {
			grid[x][y] = ngrid[x][y];
		}
	}
	/* part 2: */
	grid[0][0] = 1;
	grid[0][99] = 1;
	grid[99][0] = 1;
	grid[99][99] = 1;
	
}

int main() {
	FILE *file = fopen("advent18.txt", "r");
	char c;
	int i,x,y;
	int n = 0;
	for (x = 0; x < 100; ++x) {
		for (y = 0; y < 100; ++y) {
			c = fgetc(file);
			grid[x][y] = (c == '#') ? 1 : 0;
		}
		c = fgetc(file);
	}
	for (i = 0; i < 100; ++i) update();

	for (x = 0; x < 100; ++x) {
		for (y = 0; y < 100; ++y) {
			n += grid[x][y];
		}
	}
	printf("%d\n",n);
}