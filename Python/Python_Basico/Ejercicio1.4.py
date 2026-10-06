# Víctor Daniel Rodriguez Figueroa
#E1.4 · FizzBuzz del 1 al 100, en 6 líneas o menos.

for i in range(1,101):
    print("")
    print("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or i)