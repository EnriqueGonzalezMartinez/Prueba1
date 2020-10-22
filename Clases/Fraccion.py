class Fraccion:
        def __init__(self,arriba,abajo):
                self.x = arriba
                self.y = abajo

        def __str__(self):
               return str(self.x)+"/"+str(self.y)

        def __add__(self,otraF):
                ## Suma dos objetos
                nuevoNum = self.x*otraF.y + self.y*otraF.x
                nuevoDen = self.y*otraF.y
                com = self.mcd(nuevoNum,nuevoDen)
                return Fraccion(nuevoNum//com,nuevoDen//com)

        def __sub__(self,otraF):
                ## Resta dos objetos
                nuevoNum = self.x*otraF.y - self.y*otraF.x
                nuevoDen = self.y*otraF.y
                com = self.mcd(nuevoNum,nuevoDen)
                return Fraccion(nuevoNum//com,nuevoDen//com)

        def __mul__(self,otraF):
                ## Multiplica dos objetos
                nuevoNum = self.x * otraF.x
                nuevoDen = self.y * otraF.y
                com = self.mcd(nuevoNum,nuevoDen)
                return Fraccion(nuevoNum//com,nuevoDen//com)

        def __div__(self,otraF):
                ## Divide dos objetos
                nuevoNum = self.x * otraF.y
                nuevoDen = self.y * otraF.x
                com = self.mcd(nuevoNum,nuevoDen)
                return Fraccion(nuevoNum//com,nuevoDen//com)

        def rec(otraF):
                x = otraF.x
                y = otraF.y
                return Fraccion(y,x)

        def mcd(self,m,n):
                ## Saca el maximo comun divisor
                while m%n != 0:
                        mViejo = m
                        nViejo = n

                        m = nViejo
                        n = mViejo%nViejo
                return n

        def entero(otraF):
                x = otraF.x
                y = otraF.y
                
                if(x%y==0):
                        return (x//y)
                else:
                        com = self.mcd(x,y)
                        return Fraccion(x//com,y//com)
                
