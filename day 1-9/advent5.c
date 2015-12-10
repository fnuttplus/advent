#include <stdio.h>

int main(){
	FILE * file = fopen("advent5.txt", "r");
	char str[18];
	char c,p;
	int i,j;
	int vowels, haspair, hasbanned;
	int nice = 0;
	int hasrepeat;
	while (fgets(str, sizeof(str), file) != NULL)
	{
/* part 1:
		vowels = 0;
		haspair = 0;
		hasbanned = 0;
		p = 0;
		for (i = 0; i < 16; i++){
			c = str[i];
			if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
				vowels++;
			}
			if (p == c) haspair = 1;
			if ((p == 'a' && c == 'b') || 
				(p == 'c' && c == 'd') || 
				(p == 'p' && c == 'q') || 
				(p == 'x' && c == 'y') ) {
				hasbanned = 1;
				break;
			}
//			printf("%c ",c);
			p = c;
		}
		if (vowels >= 3 && haspair && hasbanned == 0) nice++;
//		printf("\n%s %d %d %d %d\n",str,vowels,haspair,hasbanned,nice);
*/
		haspair	= 0;
		hasrepeat = 0;
		for (i = 1; i < 15; i++) {
			if (str[i-1] == str[i+1]) hasrepeat = 1;
			for (j = 0; j < i-1; j++) {
				if ((str[i] == str[j]) && (str[i+1] == str[j+1])) haspair = 1;
//				printf("%c%c %c%c -",str[i],str[i+1],str[j],str[j+1]);
			}
		}
		if (haspair && hasrepeat){ nice++; printf("%s",str); }
//		printf("\n%s\n",(haspair && hasrepeat)?"nice":"naughty");
	}
	printf("%d\n",nice);
	exit(0);
}
