# Esse codigo realiza um teste de amor entre duas pessoas utilizando a quantidade de letras no nome de cada uma

print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?

nome1 = name1.lower()
nome2 = name2.lower()

t = nome1.count("t") + nome2.count("t")
r = nome1.count("r") + nome2.count("r")
u = nome1.count("u") + nome2.count("u")
e = nome1.count("e") + nome2.count("e")

num1 = t + r + u + e
str_num1 = str(num1)

l = nome1.count("l") + nome2.count("l")
o = nome1.count("o") + nome2.count("o")
v = nome1.count("v") + nome2.count("v")
e = nome1.count("e") + nome2.count("e")

num2 = l + o + v + e
str_num2 = str(num2)

final_numer = str_num1+str_num2

int_final_number = int(final_numer)

if int_final_number < 10 or int_final_number >= 90:
    print(f"Your score is {int_final_number}, you go together like coke and mentos.")
    
elif int_final_number > 40 and int_final_number < 50:
    print(f"Your score is {int_final_number}, you are alright together.")
else:
    print(f"Your score is {int_final_number}.")