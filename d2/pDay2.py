print("Welcome to the tip calculator")

totalBill = float(input("What was the total bill?"))
tip = float(input("What was the percentage tip would you like to give?"))
peopleForTip = int(input("How many people to split the bill??"))

rawTotal = totalBill/peopleForTip
percentageTip = tip/100;

moneyToPay = round(rawTotal + (rawTotal*percentageTip), 2)

moneyToPay = "{:.2f}".format(rawTotal + (rawTotal*percentageTip))

print(f"Each person should pay: ${moneyToPay}")