import time
import os
import termcolor as color
import random

score = 0
sequence = ""
a_human_is_playing = True

for var in ("Simon says numbers!\nAnswer the number by typing it.\nEach new number is added to the end of the sequence.\nBut remember, you have to type the whole sequence. "):
  print(var, end = "", flush = True)
  time.sleep(0.05)

input()
os.system("clear")

for var2 in ("Ready..."):
  print(var2, end = "", flush = True)
  time.sleep(0.25)
os.system("clear")

time.sleep(1)

while a_human_is_playing:
  number = random.randint(0, 9)
  print(number)
  time.sleep(0.5)

  os.system("clear")
  number = str(number)
  sequence += number

  choice = input()
  if(choice == sequence):
    score = len(sequence)
    color.cprint("Correct!", "green")
    print("Your score is %s" % score)
    time.sleep(1)
    os.system("clear")
    time.sleep(0.5)

  else:
    color.cprint("Incorrect", "red")
    time.sleep(1)
    print("The pattern was {0}\nYour score is {1}".format(sequence, score))
    time.sleep(1)
    color.cprint("You lose!!!", "red", attrs = ["bold"])
    a_human_is_playing = False
  
  if(score == 10):
    time.sleep(1)
    print("Your score is 10!")
    time.sleep(1)
    print("You beat the game!")
    time.sleep(1)
    color.cprint("YOU WIN!!!", "green", attrs = ["bold"])
    a_human_is_playing = False