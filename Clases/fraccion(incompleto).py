class Fraccion:

        def __init__(self,arriba,abajo):
                self.num= arriba
                self.den= abajo

        def __str__(self):
                return str(self.num)+"/"+str(self.den)
        
        def mcd(self,m,n):
                while m%n != 0:
                        mViejo = m
                        nViejo = n

                        m = nViejo
                        n = mViejo%nViejo
                return n
                        

        def __add__(self,otraFraccion):
                nuevoNum= self.num*otraFraccion.den + self.den*otraFraccion.num
                nuevoDen= self.den*otraFraccion.den
                comun = self.mcd(nuevoNum,nuevoDen)
                return Fraccion(nuevoNum//comun,nuevoDen//comun)

