choice = "0"
phase = 0


def placeholder():
  print("PLACEHOLDER TEXT")
  quit()


while True:
  if phase == 0:
    print(
        "The date is March 1st, 2012, and you have decided to go explore a cave. You enter the cave and immediately encounter 2 different paths to take."
    )
    choice = input("Do you go left, or go right?")
    match choice:
      case "left":
        phase = 1
        placeholder()
      case "right":
        print(2)
        phase = 2
        placeholder()
      case _:
        print("\nInvalid input. Try again.\n\n")
