



L = []

I = []

i = 1

j = 2


if type(L) == type(I) :
	print("L and I is same type of List")

if type(i) == type(j) :
	print("i and j is same type of Integer")

if type(L) == list :
	print("okay")

print(type(i))
if type(i) == int:
	print("also okay")


if 'i' in locals():
	print(" i is exist in local variable")

if 'L' in locals():
	print(" L is exist in local variable")
if hasattr(list, 'L'):
	print(" L is exist in this project")

dic = {'one':1, 'two':2}


if 'dic['one']' in locals():
	print("dic - one")
