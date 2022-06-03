def card_number(card):
    secured = ("Converted form of credit card number is ==>  "+"*"*(len(card)-4)+card[len(card)-4:len(card)+1])
    return secured



card = input("Enter the card number == > ")
secured_number = card_number(card)
print(secured_number)
