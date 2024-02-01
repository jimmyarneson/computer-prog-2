import random
playernum = int(input("Enter a number 1-20: "))
computernum = random.randint(1, 20)

print("Computer Number: " + str(computernum))
print("Your Number: " + str(playernum))

if computernum == playernum:
  print(str("You Win!!!"))
else:
  print(str("You Lose"))