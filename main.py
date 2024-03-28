choice = "0"
phase = 0
doLoop = True

while doLoop:
  if phase == 0:
    print(
        "The date is March 1st, 2012, and you have decided to go explore a cave. You enter the cave and immediately encounter 2 different paths to take."
    )
    choice = input("Do you go left (A), or go right (B)?")
  if phase == 1:
    print(
        '\nYou go left and encounter a very large dragon. It is not in a good mood. It roars "You dare challenge me, human?"'
    )
    choice = input("Do you run (C) or fight (D)?")
  if phase == 2:
    print(
        "\nYou go right and encounter a large chasm. It is too wide to jump across. There is a shaky bridge that looks like it could fall apart at any moment, and a rope that looks like it's 15 years old."
    )
    choice = input("Do you risk the bridge (E) or swing across the rope (F)?")
  if phase == 3:
    print(
        "\nYou run away from the dragon and it gets stuck in the tunnel. It tries to breathe fire at you but you get away."
    )
    phase = 97
  if phase == 4:
    print(
        "\nYou fight the dragon and it's a tough fight. You manage to kill it, and it drops a key. You pick it up and go to the next room, where you find a treasure chest."
    )
    phase = 98
  if phase == 5:
    print(
        "\nYou choose to risk the bridge. You start to cross it, but it falls apart and you fall into the chasm."
    )
    phase = 99
  if phase == 6:
    print(
        "\nYou swing across the rope and make it to the other side. You find a map in the next room that shows the way to a treasure hidden in a pyramid in Egypt."
    )
    phase = 98
  if phase == 97:
    print("\nGAME OVER\n")
    print("You Lived\n")
    print("You got no treasure.\n")
    choice = input("Do you want to play again? (Y/N)")
  if phase == 98:
    print("\nGAME OVER\n")
    print("You Lived\n")
    print("You got treasure.\n")
    choice = input("Do you want to play again? (Y/N)")
  if phase == 99:
    print("\nGAME OVER\n")
    print("You Died\n")
    choice = input("Do you want to play again? (Y/N)")
  match choice:
    case "A":
      phase = 1
    # go left
    case "B":
      phase = 2
    # go right
    case "C":
      phase = 3
    # run
    case "D":
      phase = 4
    # fight
    case "E":
      phase = 5
    # risk the bridge
    case "F":
      phase = 6
    # swing across the rope
    case "Y":
      phase = 0
      # play again
    case "N":
      doLoop = False
      break
      # stop playing
    case _:
      print("\nInvalid input. Try again.\n\n")
