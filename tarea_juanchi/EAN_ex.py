class Validate_EAN():
    
    def __init__(self):
        self.ean = 0
        
    def check_ean(self, num):
        self.ean = len(str(num))
        sum_odd = 0
        sum_even = 0
        for i in range(self.ean):
            if (i % 2 != 0):
                sum_odd += int(str(num)[i])
            else:
                sum_even += int(str(num)[i])
            if (self.ean.count() == 8):
                sum_odd = sum_even * 3
            elif (self.ean.count() == 13):
                sum_even = sum_odd * 3
            else:
                print('El codigo EAN es incorrecto')
                
            result = sum_odd + sum_even
            rest = result % 10
            control_digit = 10 - rest
    
            if control_digit == 10:
                digit_control = 0
            elif digit_control == int(str(num)[self.ean-1]):
                print('Codigo {num} correcto')
            else:
                print('Codigo {num} incorrecto')
        
        
ean_number = input('Coloque el EAN: ')

validate_ean = Validate_EAN()

check_ean_number = validate_ean.check_ean(ean_number)


print(check_ean_number)

    
    
    
    
    
    
    

    
     
    

