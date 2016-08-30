#Diffie-Hellman python script
#Does one side of a diffy-hellman key exchange

#hard-coded private secret number
mySecret = 7

print("Enter values of the form\nA^b mod p = x")
generator = input("Generator (A): ")
modulus = input("Modulus (p): ")
answer = input("Answer (x): ")

print("(" + str(generator) + "^?)" + " mod " + str(modulus) + " = " + str(answer))

my_answer = (int(generator)^int(mySecret))%int(modulus)
print("My Answer (" + str(generator) + "^" + str(mySecret) + ") mod " + str(modulus) + " = " + str(my_answer))

our_secret = (int(answer)^int(mySecret))%int(modulus)
print("Our Secret = " + str(our_secret))