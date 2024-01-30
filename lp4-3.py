eggs = int(input("Enter # of eggs"))
dozens = eggs // 12
remainder = eggs % 12
price = 0.0

if 0 < eggs <= 4:
  price = 0.50
elif 4 < eggs <= 6:
  price = 0.45
elif 6 < eggs <= 11:
  price = 0.40
elif eggs > 11:
  price = 0.35
  
total = eggs + remainder 
print("Total Cost: $" + str(price + remainder))