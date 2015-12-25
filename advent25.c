
int main(){
	int row = 1, col = 1, i = 1, n = 20151125;

	while (1) {
		n = n * 252533 % 33554393;
		if (row == 1) {
			row = col + 1;
			col = 1;
		} else {
			row--;
			col++;
		}
		i++;
		if (row == 2947 && col == 3029) {
			printf("%d %d %d %d\n", n, row, col, i);
			exit(0);
		}
	}
}

// 30147031 2947 3029 17850354
// [Finished in 1.0s]
