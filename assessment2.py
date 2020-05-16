#Defining variables required for the program
productNames = []
productPrices = []
sumOfPriceList = int(0)

#Looping the input of item and price input 5 times
def userInput():
    currentProductPrice = int()
    currentProductName = str()
    while len(productNames) <5 and len(productPrices) <5:
        currentProductName = input("Please enter the product name - ")
        productNames.append(currentProductName)
        currentProductPrice = int(input("Please enter the price of that product - £"))
        productPrices.append(currentProductPrice)


#Bubble Sort for price listing. This also sorts the productNames so they match up with their associated cost.
def bubbleSort(productPrices,productNames):
    for i in range (0, len(productPrices) - 1):
        for j in range (0, len(productPrices) - 1 - i):
            if productPrices[j] > productPrices[j+1]:
                productPrices[j], productPrices[j+1] = productPrices[j+1], productPrices[j]
                productNames[j], productNames[j+1] = productNames[j+1], productNames[j]
    return productPrices

#Creates the final print to the user, showing the products, prices, total including discount on cheapest product
def finalPrint():
    print("Your basket is as follows - ")
    print((productNames[0]), "at £", (productPrices[0]))
    print((productNames[1]), "at £", (productPrices[1]))
    print((productNames[2]), "at £", (productPrices[2]))
    print((productNames[3]), "at £", (productPrices[3]))
    print((productNames[4]), "at £", (productPrices[4]))
    print("The total price is £" + str(sumOfPriceList) + ", including the 100% discount on '" + productNames[4] + "'.")

#Calls the userInput function
userInput()

#Calling the bubbleSort function, then reversing the lists so highest price is first.
bubbleSort(productPrices, productNames)
productPrices.reverse()
productNames.reverse()

#Calculating the total, missing the last entry to apply the discount
sumOfPriceList = productPrices[0] + productPrices[1] + productPrices[2] + productPrices[3]

#Calling the finalPrint function
finalPrint()