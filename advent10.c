#include <stdio.h>

int main(){
	char *in = NULL, *out = NULL;
	//11132
	//311312
	const char start[11] = {'1','3','2','1','1','3','1','1','1','2', 0};
	//11131221133112
	int ii, i, inl, outl = 10, ci;
	char c;
	out = (char*)malloc(sizeof(start));
	memcpy(out, start, sizeof(start));

	for (ii = 0; ii < 50; ii++) {
		inl = outl+1;
		in = (char*)realloc(in, inl);
		memcpy(in, out, inl);
		out = (char*)realloc(out, 2*inl);
		c = in[0];
		ci = 1;
		outl = 0;
		for (i = 1; i < inl; i++) {
			if (in[i] == c) {
				ci++;
			}
			else {
				out[outl++] = 48+ci;
				out[outl++] = c;
				ci = 1;
				c = in[i];
			}
			out[outl] = 0;
		}
//		printf("%s %d\n", out, outl);

	}
	printf("%d\n",outl);
	free(in);
	free(out);
	exit(0);
}
//part 1: 492982
//part 2: 6989950