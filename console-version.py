import random

def player_turn(player_total, computer_total):
    while True:
        print("\n--- PLAYER TURN ---")
        print("1. Roll the die")
        print("2. End turn")
        choice = input("Select an option (1-2): ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")
            continue

        if choice == 1:
            roll = random.randint(1, 6)
            if roll == 1:
                print(f"You rolled {roll}")
                print(f"Player Total: {player_total} | Computer Total: {computer_total}")
                return player_total, computer_total, False, False, None
            else:
                print(f"You rolled {roll}")
                player_total += roll
                print(f"Player Total: {player_total} | Computer Total: {computer_total}")

            if player_total > 50:
                print("You went over 50.")
                return player_total, computer_total, True, False, "computer"
            elif player_total == 50:
                print("You reached 50.")
                return player_total, computer_total, True, False, "player"

        elif choice == 2:
            print(f"You hold at {player_total} points.")
            return player_total, computer_total, False, True, None
        else:
            print("Invalid input. Please enter 1 or 2.")

def computer_turn(player_total, computer_total):
    print("\n--- COMPUTER TURN ---")
    while True:
        roll = random.randint(1, 6)
        if roll == 1:
            print(f"Computer rolled {roll}")
            print(f"Player Total: {player_total} | Computer Total: {computer_total}")
            return player_total, computer_total, False, False, None
        else:
            print(f"Computer rolled {roll}")
            computer_total += roll
            print(f"Player Total: {player_total} | Computer Total: {computer_total}")

        if computer_total > 50:
            print("Computer went over 50.")
            return player_total, computer_total, True, False, "player"
        elif computer_total == 50:
            print("Computer reached 50.")
            return player_total, computer_total, True, False, "computer"

        if computer_total >= 48:
            print(f"Computer holds at {computer_total} points.")
            return player_total, computer_total, False, True, None

def main():
    while True:
        player_total = 0
        computer_total = 0
        current_player = "player"
        consecutive_holds = 0

        while True:
            if current_player == "player":
                player_total, computer_total, game_over, held, winner = player_turn(
                    player_total, computer_total
                )
                if not held and not game_over:
                    current_player = "computer"
                elif held:
                    current_player = "computer"
            else:
                player_total, computer_total, game_over, held, winner = computer_turn(
                    player_total, computer_total
                )
                if not held and not game_over:
                    current_player = "player"
                elif held:
                    current_player = "player"

            if game_over:
                if winner == "player":
                    print("\nYou win!")
                elif winner == "computer":
                    print("\nComputer wins!")
                else:
                    if player_total > computer_total:
                        print("\nYou win!")
                    elif computer_total > player_total:
                        print("\nComputer wins!")
                    else:
                        print("\nIt's a tie!")
                break

            if held:
                consecutive_holds += 1
            else:
                consecutive_holds = 0

            if consecutive_holds >= 2:
                print("\nBoth players held consecutively without scoring. Game ends.")
                break

        while True:
            again = input("\nWould you like to play again? (y/n): ").lower()
            if again in ('y', 'n'):
                break
            else:
                print("Please enter 'y' or 'n'.")

        if again == "n":
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
