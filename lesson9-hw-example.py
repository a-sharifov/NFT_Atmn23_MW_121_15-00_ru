def game(player):
  print("Welcome to the game!")
  print("You are playing as " + player)
  print("Good luck!")

  choice = input("Ты проснулся и очутился в темном лесу. Ты хочешь пойти на 1 - север или на 2 - юг?")
  if choice == "1":
    print("Ты пошел на север и нашел выход из леса.")
    choice = input("Ты хочешь пойти на 1 - домой или на 2 - в город?")
  elif choice == "2":
    print("Ты пошел на юг и тебя съел медведь.")
    print("Game over!")
    return
