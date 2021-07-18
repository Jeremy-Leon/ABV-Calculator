#
# Alcohol by Volume (ABV) Calculator
# 
# This program will calculate the ABV of a drink given the amount and alcohol percentage of the ingredients
#
# Simply run the script from the command line and follow the prompts
#

def main():
    print("\n------------------------------")
    print("Welcome to the ABV Calculator!")
    print("------------------------------")

    print("How many ingredients do you have?")
    numIngredients = input("Total ingredients: ")
    isNumber(numIngredients)

    print("How many ingredients contain alcohol?")
    numAlcohholicIng = input("Alcoholic ingredients: ")
    isNumber(numAlcohholicIng)

    getIngredients(int(numIngredients), int(numAlcohholicIng))


# Function to prompt the user to input all ingredients and pass on the information
def getIngredients(numIngredients, numAlcohholicIng): 
    if(numAlcohholicIng > numIngredients):
        print("ERROR: Invalid numbers entered, exiting")
        return

    # Initialize arrays for both alcoholic ingredients and non
    AlcoholicArr = [(-1,-1)] * numAlcohholicIng
    NonAlcArr = [-1] * (numIngredients - numAlcohholicIng)

    # Store the amount of liquid and alcohol percentage in a touple (amount in fl/oz, alcohol percentage)
    if(len(AlcoholicArr) != 0): print("\nPlease enter the amount and alcohol percentage of each alcoholic ingredient")
    for i in range(len(AlcoholicArr)):
        print("Alcohol #{}".format(i+1))
        amount = input("Amount (fl/oz): ")
        isNumber(amount)
        percentage = input("Alcohol %:")
        isNumber(percentage)
        AlcoholicArr[i] = (float(amount),float(percentage))


    if(len(NonAlcArr) != 0): print("\nPlease enter the amount of each non-alcoholic ingredient")
    for i in range(len(NonAlcArr)):
        print("Ingredient #{}".format(i+1))
        amount = input("Amount (fl/oz): ")
        isNumber(amount)
        NonAlcArr[i] = float(amount)
    
    calculateABV(AlcoholicArr, NonAlcArr)


# Function to combine all the ingredients and claculate the ABV percentage in the users drink
def calculateABV(AlcoholicArr, NonAlcArr):
    totalFloz_nonAlc = 0
    totalFloz_Alc = 0
    totalPercent = 0
    percentAvg = 0

    # Get total fluid ounces in non-alcoholic ingredients
    for ingredient in NonAlcArr:
        totalFloz_nonAlc += ingredient
    
    # Get total fluid ounces and percentages in alcoholic ingredients
    for ingredient in AlcoholicArr:
        totalFloz_Alc += ingredient[0]
        totalPercent += ingredient[1]
        percentAvg = totalPercent / len(AlcoholicArr)

    # Calculate the ABV of all the ingredients combined
    totalFloz = totalFloz_Alc + totalFloz_nonAlc
    ABV = (totalFloz_Alc / totalFloz) * percentAvg

    print("\nYour drink has {}% ABV in {} fl/oz!".format(str(round(ABV, 1)), totalFloz))

    compareDrinks(ABV, totalFloz)


# Function to compare the user inputed drink to several know drinks
def compareDrinks(ABV, totalFloz):
    # Initialize a couple of know drinks for comparison
    budLight = (12,4.2)
    titosVodka = (1.5, 40)
    glassWine = (5,13)

    userRatio = totalFloz * ABV
    budLightTuple = compareDrinks_helper(budLight, userRatio)
    titosVodkaTouple = compareDrinks_helper(titosVodka, userRatio)
    glassWineTouple = compareDrinks_helper(glassWine, userRatio)

    print("That is equal to...")
    print("{} Bud Light{}".format( budLightTuple[0], budLightTuple[1] ))
    print("{} Shot{} of Titos Vodka".format( titosVodkaTouple[0], titosVodkaTouple[1] ))
    print("{} 5 fl/oz serving{} of red wine".format( glassWineTouple[0], glassWineTouple[1] ))


# Helper function that takes in a know drink and the users drink ratio and calculates how many of known drinks = users drink
# Function also determines if the print statement should use a plural
def compareDrinks_helper(drink, userRatio):
    numDrinks = round( (userRatio / (drink[0] * drink[1])), 1)
    plural = ""
    if(numDrinks > 1):
        plural = "s"
    return (numDrinks, plural)


# Function to check if user input is a valid number, if not, exit
def isNumber(number):
    try:
        float(number)
        return True
    except:
        print("Invalid number entered, exiting")
        exit()


if __name__ == "__main__":
    main()