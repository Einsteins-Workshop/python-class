import time
import random

def jump_rope_game(players):
    round_num = 1
    min_time = 1.5  # time to react, gets shorter each round

    print("\n=== SQUID GAME: JUMP ROPE ===")
    print(f"{len(players)} players are starting!\n")
    time.sleep(2)

    while len(players) > 1:
        print(f"\n--- ROUND {round_num} ---")
        print("Get ready to jump!")
        time.sleep(2)

        # Random wait time before rope swings
        swing_wait = random.uniform(2, 4)
        print("Rope is swinging soon...")
        time.sleep(swing_wait)

        survivors = []
        for player in players:
            print(f"\n{player}'s turn to JUMP!")
            start_time = time.time()

            try:
                input("Press [ENTER] to jump!")
                reaction_time = time.time() - start_time
            except:
                reaction_time = float('inf')

            if reaction_time <= min_time:
                print(f"✅ {player} jumped in {reaction_time:.2f}s and SURVIVED!")
                survivors.append(player)
            else:
                print(f"❌ {player} was too slow ({reaction_time:.2f}s) and is ELIMINATED!")

        if not survivors:
            print("\n💀 Everyone failed. No winners this round.")
            return

        players = survivors
        round_num += 1
        min_time *= 0.85  # shorter reaction time each round
        time.sleep(2)

    print(f"\n🎉 WINNER: {players[0]} 🎉")

# Example player list
players = ["Player 1", "Player 2", "Player 3", "Player 4"]

jump_rope_game(players)
