import random

print("please Enter the Number your betting at.")

first = int(input("please enter the first number: "))
second = int(input("please enter the second number: "))
third = int(input("please enter the third number: "))

Lfnum = random.randint(1, 3)
Lsnum = random.randint(1, 2)
Ltnum = random.randint(2, 3)

mylist = first,second,third
lotolist = Lfnum,Lsnum,Ltnum

print(f"your number are: ",mylist)
print("And the Result are:",lotolist)


if first == Lfnum and second == Lsnum and third == Ltnum:
    print("Jackpot")
elif (
    first in {Lfnum, Lsnum, Ltnum} and
    second in {Lfnum, Lsnum, Ltnum} and
    third in {Lfnum, Lsnum, Ltnum} and
    len({first, second, third}) == 3  
):
    print("you partially win some rewards")
else:
    print("Better Luck next time")