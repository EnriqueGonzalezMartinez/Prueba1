a= int(input("Ingresa la A"));
b= int(input("Ingresa la B"));
c= int(input("Ingresa la C"));
n=0;
m=1;
r=0;
w=1;
x= [];
y= [];

for i in range (-a,a,1):
	try:
		d = a%i;
	except:
		l = 0
	if(d == 0):
		for j in range (-a,a,1):
			try:
				e = a%j;
			except:
				k = 0
			if(e == 0):
				if(i*j == a):
					x.append(i);
					x.append(j);

for i in range (-50,50,1):
	try:
		f=c%i;
	except:
		q=0;
	if(f==0):
		for j in range (-50,50,1):
			try:
				g=c%j;
			except:
				q=0;
			if(g==0):
				if(i*j==c):
					y.append(i);
					y.append(j);

A=len(x)//2;
B=len(y)//2;

for i in range (0,A,1):
        H=x[n]
        I=x[m]

        for j in range (0,B,1):
                O=y[r]
                P=y[w]
		
                if(H*P+I*O==b):
                                print("("+str(H)+"+"+str(O)+")"+"("+str(I)+"+"+str(P)+")");
                r=r+2;
                w=w+2;
        r=0;
        w=1;
        n=n+2;
        m=m+2;
