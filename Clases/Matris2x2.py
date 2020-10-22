class Matris2x2:
        x11= 1;
	x12= 0;
	x21= 0;
	x22= 1;
	a= 0;
	b= 0;

	def __init__(self):
                self.x11=1;
                self.x12=0;
                self.x21=0;
                self.x22=1;
                self.a=0;
                self.b=0;

	def __init__(self,x11,x12,x21,x22,a,b):
                self.establecerX11(x11)
                self.x12=x12;
                self.x21=x21;
                self.x22=x22;
                self.a=a;
                self.b=b;
                
        def establecerX11(self,x11):
                self.x11=x11;

        def obtenerX11(self):
                return x11;
                
	def Hacer1(self):
                self.a= self.a*(1/self.x11);
                self.x12= self.x12*(1/self.x11);
                self.x11= self.x11*(1/self.x11);

        def Hacer0(self):
                self.b= (self.x21*-1)*self.a+self.b;
                self.x22= (self.x21*-1)*self.x12+self.x22;
                self.x21= (self.x21*-1)*self.x11+self.x21;

        def Hacer12(self):
                self.b=self.b*(1/self.x22);
                self.x21=self.x21*(1/self.x22);
                self.x22=self.x22*(1/self.x22);

        def Hacer02(self):
                self.a=(self.x12*-1)*self.b+self.a;
                self.x11 -(self.x12)*self.x21+self.x11;
                self.x12=-(self.x12)*self.x22+self.x12
                
a= Matris2x2()
a.establecerX11(12)
