# Basal Metabolic Rate Calculator (Imperial System)

weight = int(input("Enter your weight in pounds: \n"))
height = int(input("Enter your height in inches: \n"))
age = int(input("Enter your age in years: \n"))
isMale = str(input("Are you male? (y/n)"))

if isMale == "y":
    isMale ==True
elif isMale == "n":
    isMale = False
else:
    print("Error")
    quit()

#The original Harris-Benedict equation (1919) converted for Imperial System
#if isMale:
#    bmr = 66.5 + (13.7516 * weight * 0.453592) + (5.0033 * height * 2.54) - (6.755 * age)
#else:
#    bmr = 655.1 + (9.5634 * weight * 0.453592) + (1.8496 * height * 2.54) - (4.6756 * age)

#The revised Harris-Benedict equation   (1984) converted to Imperial System
#if isMale:
#    bmr = 88.362 + (13.397 * weight * 0.453592) + (4.799 * height * 2.54) - (5.677 * age)
#else:
#    bmr = 447.593 + (9.247 * weight * 0.453592) + (3.098 * height * 2.54) - (4.33 * age)   

#The Mifflin St Jeor Equation (1990) converted to Imperial System  
if isMale:
    bmr = 5 + (10 * weight * 0.453592) + (6.25 * height * 2.54) - (5 * age)
else:
    bmr = -161 + (10 * weight * 0.453592) + (6.25 * height * 2.54) - (5 * age) 
bmr = round(bmr)
print("Your basal metabolic rate is " + str(bmr))
