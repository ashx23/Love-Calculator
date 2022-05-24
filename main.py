
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

totalname = name1 + name2
lower_case_string = totalname.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e 

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("o")
e = lower_case_string.count("e")

love = l + o + v + e 

together = int(str(true) + str(love))

if together < 10 or together > 90:
  print(f"Your love is {together}, you go like coke and mentos")
elif together >= 40 and together <= 50:
  print(f"Your score is {together},you are alright together")
else:
  print(f"Your score is {together}")

