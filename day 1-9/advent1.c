#include <stdio.h>
int main(){
	FILE * file = fopen("advent1.txt", "r");
	char c;
	int i = 0;
	int n = 0;
	while((c = fgetc(file)) != EOF){
		if (c == 40){i++;n++;printf("+");}
		else if (c == 41){i--;n++;printf("-");}
		printf("%d: %d\n",n,i);
		if (i == -1){
			printf("\n%d: %d",i,n);
			exit(0);
		}
	}
}