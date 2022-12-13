# A calculator that will give you the amount that you have to pay if there are many persons
print("Welcome to tip calculator.")
total_bill = float(input("Enter total bill: $"))
tip_percentage = float(input("what is the tip percentage by per person"))
total_persons = int(input("how many people are there?"))

bill_per_person = total_bill / total_persons
bill_with_tip = bill_per_person + bill_per_person / tip_percentage
print(f"tip per person will be ${bill_per_person/tip_percentage}")
print(f"The amount that per person will pay is ${format(bill_with_tip,'.2f')}")
