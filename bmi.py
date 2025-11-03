def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height)
    print(bmi)

    if (bmi>25.0):
        classification = -1
    elif (18.5 < bmi < 25.0):
        classification = 0
    elif (bmi < 18.5):
        classification = 1

    return bmi, classification

calculate_bmi(weight=57, height=1.73)

