import math

class Complex(object):
    def __init__(self, real=0, imaginary=0):
        self.real = real
        self.img = imaginary
        
    #This function method object's __add__ method overloading + operator for this class
    def __add__(self, no):
        ans=Complex()
        ans.real = self.real+no.real
        ans.img = self.img+no.img 
        return(ans)
    
    #This method overrides object's __sub__ method overloading - operator for this class
    def __sub__(self, no):
        ans=Complex()
        ans.real = self.real-no.real
        ans.img = self.img-no.img 
        return(ans)

    #This method overrides object's __mul__ method overloading * operator for this class
    def __mul__(self, no):
        ans=Complex()
        a = self.real
        b = self.img
        c = no.real
        d = no.img
        ans.real = (a*c)-(b*d)
        ans.img = (a*d)+(b*c)
        return(ans)

    #This method overrides object's __add__ method overloading % operator for this class
    def __truediv__(self, no):
        conj = Complex(no.real, -(no.img))
        denominator = (no.__mul__(conj)).real
        numerator = self.__mul__(conj)
        ans=Complex()
        ans.real = numerator.real/denominator
        ans.img = numerator.img/denominator
        return(ans)

    #This method returns the modulus of complex number
    def mod(self):
        ans=Complex()
        ans.real = math.sqrt(self.real**2 + self.img**2)
        return(ans)

    def __str__(self):
        if self.img== 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.img >= 0:
                result = "0.00+%.2fi" % (self.img)
            else:
                result = "0.00-%.2fi" % (abs(self.img))
        elif self.img > 0:
            result = "%.2f+%.2fi" % (self.real, self.img)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.img))
        return result


print("Enter numbers as real part followed by imaginary part")
c = map(float, input("Enter first number: ").split())
d = map(float, input("Enter second number: ").split())
x = Complex(*c)
y = Complex(*d)
print("\n")
print("The sum is: "+str(x+y))
print("The subtraction is: "+str(x-y))
print("The multiplication is: "+str(x*y))
print("The division is: "+str(x/y))
print("Mod of x: ",str(x.mod()))
print("Mod of y: ",str(y.mod()))
