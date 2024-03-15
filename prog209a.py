from CL209a import *

def main():
  try:
      nums = []
      with open("Langdat/prog215a.dat", 'r') as f:
        for line in f:
            nums.append(int(line))
      
            

  except Exception as e:
      print("Error:", e)
  pass

  pass


if __name__ == "__main__":
  main()