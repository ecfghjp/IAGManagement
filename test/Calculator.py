class Calculator:
    def sum(self, a, b):
        return a + b
    
    def subtract(self,a,b):
        return a-b
    
    def devide(self,a,b):
        if b==0:
            raise ZeroDivisionError
        return a/b