a = [int(i) for i in input().split()]
if a[1] - 2 * (a[1] * 2 - a[0]) > 0 and a[1] * 2 - a[0]:
	print(a[1] - 2 * (a[1] * 2 - a[0]), a[1] * 2 - a[0])
else:
	print("impossible")