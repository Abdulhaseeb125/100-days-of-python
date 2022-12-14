#Love calculator
first_name = input("Enter 1st name: ")
second_name = input("Enter 2nd name: ")
Name = first_name + second_name
Name = Name.lower()
count2 = count1 = 0
count1 = count1 + Name.count('r') + Name.count('t') + Name.count('u') + Name.count('e')
count2 = count2 + Name.count('l') + Name.count('o') + Name.count('v') + Name.count('e')

score = str(count1) + str(count2)
score = int(score)
if score <= 10 or score >= 90:
    print(f"Your score is {score} and you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score} and you are alright together.")
else:
    print(f"Your score is {score}")
