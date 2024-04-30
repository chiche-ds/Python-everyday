# task 1 calculate the sume of two degit number 
tw0_digit_number = input("enter a two digit number")
print(int(tw0_digit_number[0]) + int(tw0_digit_number[1]))


# create a BMI calculator. 

height = float(input("Enter your height in meter square : \n"))

weight = int(input("Enter your weight in meter square : \n"))

BMI = int(weight/(height * height))

print(BMI)

#your life in weeks 

age = int(input("Whats your age \n") )
age_in_weeks = age * 52 

Total_number_of_weeks = 4680

weeks_left_to_live = Total_number_of_weeks - age_in_weeks

print(f"You have {weeks_left_to_live} weeks left to live")