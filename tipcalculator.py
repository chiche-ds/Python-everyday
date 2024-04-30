# a program to calculate a tip 
print("Welcome to the tip Calculator !")
Bill = float(input("what is your Bill? \n"))
tip = int(input("How much tip will you like to give 10, 12 or 15 ?"))
tip_in_percentage = tip/100 * Bill

person = int(input("how many persons are spliting the bill? "))

final_bill = Bill + tip_in_percentage

bill_per_person = round(final_bill/person , 2)


print(f"Each person should pay: {bill_per_person}")