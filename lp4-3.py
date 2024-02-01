eggs = int(input("Enter # of eggs "))
dozens = eggs // 12
remainder = eggs % 12
price = 0.0

if 0 < dozens <= 4:
  price = 0.50
elif 4 < dozens <= 6:
  price = 0.45
elif 6 < dozens <= 11:
  price = 0.40
elif dozens > 11:
  price = 0.35
total = round(int(dozens * eggs) / (remainder / price), 2) / 2
print("Total Cost: $" + str(total))