class ClaseEAN():
    longitud=-1
    
    def __init__(self):
      self.longitud = 0
      
    def Comprobar(self, numero):
        self.longitud=len(str(numero))
        sumapar=0
        sumaimpar=0
         for i in range (self.longitud-1):
            if ((i+1) % 2 == 0) :
                sumapar += int(str(numero)[i])
            else:
                sumaimpar += int(str(numero)[i])
            if (self.longitud)==8:
                sumaimpar=sumaimpar*3
            elif (self.longitud)==13:
                sumapar=sumapar*3
            else:
            return "El código EAN {numero} no es correcto"
        
        Total=sumapar+sumaimpar
        resto=Total%10
        digitoControl=10-resto
        
        if digitoControl==10:
            digitoControl=0
        if digitoControl==int(str(numero)[self.longitud-1]):
            return f"El código EAN {numero} es correcto"
         else:
            return f"El código EAN {numero} es incorrecto"
        
        
num = input("Introduzca un número EAN (8 o 13 caracteres):")
Ean=ClaseEAN()
result= Ean.Comprobar(num)
print(result)