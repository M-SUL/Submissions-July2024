
import random as r, math as m

max = 100
gen = r.randint(0,max)



attempts = m.ceil(m.log2(max))
# print(attempts)
guesses = 0

inp = int(input("Enter your number"))

while True:
    
    if guesses > attempts:
        print("you loosed")
        break
    
    guesses = guesses+1
    if inp == gen:
        print("Win "+ "with number of guesses ="+ str(guesses))



    elif inp > gen:
        print("try smaller")     
        
    else:
        print("try bigger") 

    inp = int(input("Enter your number"))







