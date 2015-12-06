#include <stdio.h>

int main() {
	FILE * file = fopen("advent6.txt", "r");
	int (*grid)[1000] = (int(*)[1000])malloc(1000*1000*sizeof(int));
	int i,j;
	char str[50];
	char trash[10];
	int x1,x2,y1,y2;
	int n;
	for (i = 0; i < 1000; i++) {
		for (j = 0; j < 1000; j++) {
			grid[i][j] = 0;
		}
	}
	while (fgets(str, sizeof(str), file) != NULL) {
//		printf("%s",str);
		if (str[1] == 'o') {
			sscanf(str, "%s %d,%d through %d,%d", &trash, &x1, &y1, &x2, &y2);
//			printf("toggle %d\n",x1);
			for (i = x1; i <= x2; i++) {
				for (j = y1; j <= y2; j++) {
					//grid[i][j] ^= 1;
					grid[i][j] += 2;
				}
			}
		} else {
			sscanf(str, "%s %s %d,%d through %d,%d", &trash,&trash, &x1, &y1, &x2, &y2);
//			printf("turn %c %d\n",str[6], x1);
			for (i = x1; i <= x2; i++) {
				for (j = y1; j <= y2; j++) {
					//grid[i][j] = (str[6] == 'n');
					grid[i][j] += (str[6] == 'n')?1:-1;
					if (grid[i][j] == -1) grid[i][j] = 0;
				}
			}
		}
	}
	n=0;
	for (i = 0; i < 1000; i++) {
		for (j = 0; j < 1000; j++) {
			n += grid[i][j];
		}
	}
	printf("\n%d\n",n);
}