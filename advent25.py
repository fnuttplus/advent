
row, col, i, n = 1, 1, 1, 20151125

while True:
	n = n * 252533 % 33554393
	if row == 1:
		row = col + 1
		col = 1
	else:
		row -= 1
		col += 1
	i += 1
	if row == 2947 and col == 3029:
		print(n, row, col, i)
		break

# 19980801 2947 3029 17850354
# [Finished in 14.2s]
