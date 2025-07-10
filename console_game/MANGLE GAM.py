import random
import time


def mingle_game(players):
    round_num = 1

    while len(players) > 1:
        print(f"\n--- Round {round_num} ---")
        print(f"Players left: {len(players)}")
        print("Mingle! Mingle! Mingle!")
        time.sleep(2)

        random.shuffle(players)
        pairs = []
        eliminated = None

        if len(players) % 2 == 1:
            eliminated = players.pop()
            print(f"{eliminated} couldn't find a partner and is ELIMINATED!")

        for i in range(0, len(players), 2):
            pair = (players[i], players[i + 1])
            pairs.append(pair)
            print(f"Paired: {pair[0]} ❤️ {pair[1]}")

        if eliminated:
            players = [player for player in players if player != eliminated]

        round_num += 1
        time.sleep(2)

    print(f"\n🎉 WINNER: {players[0]} 🎉")


# Example player list
players = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5", "Player 6", "Player 7"]

mingle_game(players)
