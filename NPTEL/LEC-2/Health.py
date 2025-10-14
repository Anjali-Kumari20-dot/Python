# This python program input's a patient's 
# age, weight and height. It calculates
# the patient's Body Mass Index (BMI),
# Basal Metabolic Rate (BMR) and
# Ideal Body Weight (IBW).

a = int(input('Enter age: '))
w = float(input('Enter weight in kg: '))
h = float(input('Enter height in cm: '))

# Calculate BMI
bmi = w / (h/100)**2
print(f'BMI is: {bmi}')

# Calculate BMR using Mifflin-St Jeor Equation
bmr = 10 * w + 6.25 * h - 5 * a
print(f'BMR is: {bmr} calories/day')

# Calculate IBW using Devine Formula
if a < 18:  
    ibw = 50 + 0.9 * (h - 152)
else:
    ibw = 48 + 0.9 * (h - 152)
print(f'IBW is: {ibw} kg')
# Note: These formulas are general estimates and may not be accurate for all individuals.
# Consult a healthcare professional for personalized health assessments.
# For more accurate results, consider factors like gender, muscle mass, and activity level.
# This program is for educational purposes only.
