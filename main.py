# Credit Card Validator by vice :)

CardNum = input("Type in Credit Card #: ").replace('-', '').replace(' ', '')
if not CardNum.isdigit():
    raise Exception("VALIDATOR ERROR - Only digits (eg: 123)!")

value = 0

for num in CardNum[::-2]: # odd
    value += int(num)
for num in CardNum[-2::-2]: # even
    num = int(num) * 2
    if num > 9:
        num = 1 + num%10 # as 9 is the highest num, 9*2 = 18, first num will always be 1 
    value += num

if value % 10 == 0:
    print(f'Card # ({CardNum}) is valid!')
else:
    print(f'Card # ({CardNum}) is invalid!')