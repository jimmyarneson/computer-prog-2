from CL85b import Salesperson


def main():
  try:
    print("Number\tCode\tSales\tCommission")
    with open("Langdat/prog285b.dat", "r") as f:
      for line in f:
        ldat = line.split(" ")
        id = int(data[0])
        code = int(ldata[1])
        sales = float(ldata[2])

        seller = Salesperson(id, code, sales)
        seller.setComm()
        print(str(seller))
  except Exception as e:
    print("Error:", e)
  
  pass


if __name__ == "__main__":
  main()