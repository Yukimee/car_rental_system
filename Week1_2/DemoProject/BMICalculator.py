weight = float(input("Please enter your weight in kilograms: "))
height = float(input("Please enter your height in meters squared: "))

bmi_score = weight/(height**2)

if bmi_score < 18.5:
    bmi_category = "underweight."
elif 18.5 < bmi_score < 24.9:
    bmi_category = "normal weight."
elif 25 < bmi_score < 29.9:
    bmi_category = "Overweight!"
elif bmi_score >30:
    bmi_category = "Obese!"


print("Your BMI score =", round(bmi_score, 2), ". You are", bmi_category)




