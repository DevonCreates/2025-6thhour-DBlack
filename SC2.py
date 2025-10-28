#Name:Devon Black
#Class: 6th Hour
#Assignment: SC2


#A local health clinic is looking to add a quick BMI calculator to their website so that their
#patients can quickly input their height and weight and be given a number as well as their
#classification. The classifications are as follows:

# - Underweight: Less than 18.5 BMI
# - Normal Weight: 18.5 to 24.9 BMI
# - Overweight: 25 to 29.9 BMI
# - Obese: 30 or more BMI

#It is up to you to figure out the calculation for an accurate BMI reading and tying it to
#the right classification

#Code Here:
Height = int(input("enter height in inches: "))
Weight = int(input("enter weight in pounds: "))

BMI = Weight / (Height **2) * 703

if BMI < 18.5:
    print("Patient Is Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Patient is Normal Weight")
elif BMI >= 25 and BMI <= 29.9:
    print("Patient is Overweight")
else:
    print("Patient is Obese Weight")