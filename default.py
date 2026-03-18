#1 square number 
def sqr(num, exp=2):
    return num ** exp

print(sqr(3))     
print(sqr(3, 3))   
print(sqr(2, 4))   

#2 default name
def greet(name="Guest"):
    print("Hello", name)

greet()      
greet("Alice") 



