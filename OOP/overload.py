class operasi:
    def add(self, a, b):
        return a + b
    
    def add(self, a, b, c):
        return a + b + c
    
    def add(self, a, b, d):
        return a + b + d
    

opr = operasi()
print(opr.add(5, 10, 15))
print(opr.add(20, 20, 20))
print(opr.add(2, 2, 2))
