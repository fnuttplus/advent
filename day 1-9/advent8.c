#include <stdio.h>
int main(){
	FILE * file = fopen("advent8.txt", "r");
	char c;
	int n1 = 0;
	int n2 = 0;
	while((c = fgetc(file)) != EOF){
/* PART 1 *
//		printf("%c",c);
		if (c == '"') {
			n1++;
		}
		else if (c == '\\') {
			n2++;
			n1+=2;
			if ((c = fgetc(file)) == 'x') {
				n1+=2;
				fseek(file, 2, SEEK_CUR);
			}
		}
		else if (c <= ' '){
//			printf("%d %d\n",n1, n2);
		}
		else {
			n1++;
			n2++;
		}
	}
*/
		if (c == '\"' || c == '\\') n1++;
		if (c == '\n') n1 += 2;
		else {
			n1++;
			n2++;
		}
	}
	n1 += 2;
	printf("\n%d-%d=%d\n",n1, n2, n1-n2);

}