import time
import threading as th

def print_nums(start, end, delay):
  for i in range(start, end):
    time.sleep(delay)
    print(i, " ")

def print_lets(delay):
  for letter in "abcdefghijklmnopqrstuvwxyz":
    time.sleep(delay)
    print(letter)

t1 = th.Thread(target=print_nums, args=(1,78, 0.5)).start()
#t2 = th.Thread(target=print_nums, args=(11,21, 0.5)).start()
t2 = th.Thread(target=print_lets, args =(0.5,)).start()
#wait for thread to complete before exiting
t1.join()
t2.join()