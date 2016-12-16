#include <stdio.h>

int n[35651584] = {1,0,0,0,1,0,0,1,1,0,0,0,0,0,0,0,1};

int main(){
	int i, l = 17, m = 35651584;

	while (l < m) {
		for (i = 0; i < l; i++) {
			if (l+i+1 == m) break;
			n[l+i+1] = n[l-i-1] ? 0:1;
		}
		l = (l<<1)+1;
	}

	while (!(m&1)) {
		for (i = 0; i < m; i+=2) {
			n[i>>1] = (n[i]==n[i+1]);
		}
		m >>= 1;
	}

	for (i = 0; i < m; i++) {
		printf("%d",n[i]);
	}
	printf("\n");

	return 0;
}
