from CL213f import *

def main():
  try:
      elecbills = []
      with open("Langdat/prog213f.dat", 'r') as f:
        for line in f:
            kwh = int(line)
            if kwh != -999:
              bill = responsibility(kwh)
              elecbills.append(bill)
      for bill in elecbills:
          bill.calc()
          print(bill)
  except Exception as e:
      print("Error:", e)
  pass

  pass


if __name__ == "__main__":
  main()