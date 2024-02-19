def calcCircufrence(radius):
  return round(3.14159 * radius * 2, 3)

def calcArea(radius):
  return round(3.14159 * radius ** 2, 3)

  
def main():
  rad = float(input("Enter the radius: "))
  print(f"Circufrence: {calcCircufrence(rad)}\nArea: {calcArea(rad)}")
  pass


if __name__ == "__main__":
  main()