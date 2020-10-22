x= "sanidinas";
long= len(x) - 1
fr= "";

for i in range (long,-1,-1):
	fr += x[i];

if(x == fr):
	print("La oracion es palindroma");
else:
	print("La oracion no es palindroma");
