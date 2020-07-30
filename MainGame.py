from Live import welcome, load_game

print(welcome("Denis"))
play_again = "y"

while play_again == "y":
    load_game()
    play_again = input("Do you want to play again (y/n)? ")
