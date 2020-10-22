x = "abcaj8sfj"
y,y1,y2,y3,y4 = x.find("0"),x.find("1"),x.find("2"),x.find("3"),x.find("4")
y5,y6,y7,y8,y9 = x.find("5"),x.find("6"),x.find("7"),x.find("8"),x.find("9")

if(y!=-1 or y1!=-1 or y2!=-1 or y3!=-1 or y4!=-1 or y5!=-1 or y6!=-1 or y7!=-1 or y8!=-1 or y9!=-1):
	print("Hay un numero")
else:
	print("No hay numero")
