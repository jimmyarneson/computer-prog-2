def calcCircufrence(radius):
  return 2 * 3.14159 * radius

def calcArea(radius):
  return 3.14159 * radius ** 2

  
def main():
  radius = float(input("Enter the radius: "))
  print(f"Circufrence: {calcCircufrence(radius)}\nArea: {calcArea(radius)}")
  pass


if __name__ == "__main__":
  main()