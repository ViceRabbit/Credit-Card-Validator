# Credit Card Validator by vice :)

CardNum = input("Type in Credit Card #: ").replace('-', '').replace(' ', '')
if not CardNum.isdigit():
    raise Exception("VALIDATOR ERROR - Only digits (eg: 123)!")

value = 0
# "354345435"
for num in CardNum[::-2]: # odd
    value += int(num)
for num in CardNum[-2::-2]: # even
    num = int(num) * 2
    if num > 9:
        num = 1 + num%10 # as 9 is the highest num, 9*2 = 18, first num will always be 1. 
    value += num

# 348282246310005378282246310005

if value % 10 == 0:
    CardType = ""
    if len(CardNum) == 15 and (CardNum[0:2] == "34" or CardNum[0:2] == "37"):
        CardType = " [American Express]"
    if (len(CardNum) == 13 or len(CardNum) == 16) and CardNum[0] == "4":
        CardType = " [Visa]"
    if len(CardNum) == 16 and CardNum[0] == "5":
        CardType = " [Mastercard]"
    if len(CardNum) == 16 and CardNum[0] == "6":
        CardType = " [Discover]"
    print(f'Card # {CardNum}{CardType} is valid!')
else:
    print(f'Card # ({CardNum}) is invalid!')