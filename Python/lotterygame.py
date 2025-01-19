#Lottery Game adding a user with loop
import random

lottery_no = random.sample(range(0,9),k=7)
print(lottery_no)
points = 0
user_no = list(map(int,input("Enter your 7 numbers: (Seprated by space) ").split()))
print(user_no)

for i,j in zip(lottery_no,user_no):
    if i == j:
        print(f"{i} & {j} match {chr(10004)}")
        points += 1
    else:
        print(f"{i} & {j} don't match {chr(10060)}")

print(f"You got {points} points out of 7")