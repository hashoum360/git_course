def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index (BMI).

    Formula: BMI = weight (kg) / height (m)^2
    """
    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return weight_kg / (height_m ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


if __name__ == "__main__":
    try:
        weight = float(input("Enter weight in kg: "))
        height = float(input("Enter height in meters (e.g. 1.75): "))

        bmi = calculate_bmi(weight, height)
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {bmi_category(bmi)}")
    except ValueError as e:
        print(f"Invalid input: {e}")