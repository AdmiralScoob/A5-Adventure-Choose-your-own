choice = "0"
def placeholder():
  quit()
def part1():
  global choice
  print(
      "The date is March 1st, 2012, and you have decided to go explore a cave. You enter the cave and immediately encounter 2 different paths to take.\n"
  )
  choice = input("Do you go left (A), or go right (B)?")

  
  match choice:
    case "A":
      choice = "0"
      placeholder()
    case "B":
      choice = "0"
      placeholder()
    case _:
      print("\nInvalid input. Try again.")
  