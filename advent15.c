/*
Sprinkles: 		capacity 2, durability  0, flavor -2, texture  0, calories 3
Butterscotch: 	capacity 0, durability  5, flavor -3, texture  0, calories 3
Chocolate: 		capacity 0, durability  0, flavor  5, texture -1, calories 8
Candy: 			capacity 0, durability -1, flavor  0, texture  5, calories 8
*/

int main(){
	int ingr[4][5] = {{2,0,-2,0,3},{0,5,-3,0,3},{0,0,5,-1,8},{0,-1,0,5,8}};
	int a,b,c,d;
	int score, maxscore = 0;
	int cap, dur, fla, tex, cal;

	for (a = 0; a <= 100; a++) {
		for (b = 0; b <= 100; b++) {
			if (a+b > 100) break;
			for (c = 0; c <= 100; c++) {
				if (a+b+c > 100) break;
				d = 100-(a+b+c);
				cap = a*ingr[0][0] + b*ingr[1][0] + c*ingr[2][0] + d*ingr[3][0];
				if (cap <= 0) continue;
				dur = a*ingr[0][1] + b*ingr[1][1] + c*ingr[2][1] + d*ingr[3][1];
				if (dur <= 0) continue;
				fla = a*ingr[0][2] + b*ingr[1][2] + c*ingr[2][2] + d*ingr[3][2];
				if (fla <= 0) continue;
				tex = a*ingr[0][3] + b*ingr[1][3] + c*ingr[2][3] + d*ingr[3][3];
				if (tex <= 0) continue;
				cal = a*ingr[0][4] + b*ingr[1][4] + c*ingr[2][4] + d*ingr[3][4];
				if (cal != 500) continue;
				score = cap * dur * fla * tex;
				if (score > maxscore) {
					printf("%d %d %d %d, %d %d %d %d %d - %d\n", a,b,c,d, cap, dur, fla, tex, cal, score);
					maxscore = score;
				}
			}
		}
	}
}
