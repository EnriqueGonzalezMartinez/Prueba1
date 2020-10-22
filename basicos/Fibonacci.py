x=0
z=1
v=0
i=0
y=3

print(str(1)+"-"+str(0))
print(str(2)+"-"+str(1))


for i in range (0,23,1):
	v=x+z
	x=z
	z=v
	print(str(y)+"-"+str(v))
	y=y+1