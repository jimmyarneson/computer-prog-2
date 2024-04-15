from Cl702q import *

def main():
  try:
      people = []
      with open("Langdat/prog702q.txt", 'r') as f:
          num = int(f.readline())
          while num != 99:
              name = f.readline()
              favW = f.readline()
              if num == 1:
                  furM = float(f.readline())
                  a = Hiccas(name, favW, furM)
                  animal.append(a)
              elif num == 2:
                  steps = int(f.readline())
                  a = Wallies(name, favW, steps)
                  animal.append(a)
              elif num == 3:
                  sWord = f.readline().strip()
                  a = Beepers(name, favW, sWord)
                  animal.append(a)
              num = int(f.readline())
          tot = 0.0
          cnt = 0
          totstus = 0
          avgW = 0.0
          cnt2 = 0

          for person in people:
              if isinstance(animal, Hiccas):
                tot += animal.furM
                cnt += 1
              elif isinstance(animal, Wallies):
                totstus += animal.steps
              elif isinstance(animal, Beepers):
                avgW += animal.sWord
                cnt2 += 1

          print("The average value of the Hicca fur is: ", round(tot/cnt, 2))
          print("The average number of steps taken by the Wallies is: ", totStus)
          print("The average size of the Beepers words is:  ", round(avgW/cnt2, 2))
  except Exception as e:
      print("Error:", e)
  pass

  pass


if __name__ == "__main__":
  main()