#include <stdio.h>
int main(){
	FILE * file = fopen("advent2.txt", "r");
	int l,w,h,t;
	int a = 0, r = 0;
	char num[10];
	while (fgets(num, sizeof(num), file) != NULL)
	{
		sscanf(num, "%dx%dx%d", &l, &w, &h);
		if (w < l) {t = l; l = w; w = t;}
		if (h < l) {t = l; l = h; h = t;}
		if (h < w) {t = w; w = h; h = t;}
	    printf("%dx%dx%d\n", l, w, h);
		a += 2*l*w + 2*l*h + 2*w*h + l*w;
		r += l*w*h + 2*l + 2*w;
	}
	printf("\na: %d\n", a);
	printf("\nr: %d\n", r);
	exit(0);
}
// 1598415
// 3812909