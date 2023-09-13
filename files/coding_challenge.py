import re

def isValidCreditCard(cardNumber):
    # Check if the card number starts with only digits  4, 5, or 6 
    if re.match(r'^[4-6]\d{3}(-?\d{4}){3}$', cardNumber):
        #  check for consecutive repeated digits
        cardNumber = cardNumber.replace('-', '')
        if re.search(r'(\d)(\1{3,})', cardNumber):
            return 'Invalid'
        else:
            return 'Valid'
    else:
        return 'Invalid'

n = int(input())

for _ in range(n):
    cardNumber = input().strip()
    result = isValidCreditCard(cardNumber)
    print(result)
