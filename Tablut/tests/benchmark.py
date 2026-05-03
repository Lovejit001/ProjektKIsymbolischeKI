import scr.main
from scr import config

B = config.B
W = config.W
K = config.K


def benchmark():
    import time
   
    print("=" * 60)
    print("STARTING BENCHMARK")
    print("=" * 60)
    runs = 10000
    total_time = 0
    
    # Test 1: Startspiel

    
    for i in range(runs):
        config.board = [
            [0, 0, 0, B, B, B, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [B, 0, 0, 0, W, 0, 0, 0, B],
            [B, B, W, W, K, W, W, B, B],
            [B, 0, 0, 0, W, 0, 0, 0, B],
            [0, 0, 0, 0, W, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, 0, 0, 0],
            [0, 0, 0, B, B, B, 0, 0, 0]
        ]
        config.reset_pieces()
        config.onTurn = "Black"
        
        start_time = time.time()
        scr.main.main()
        end_time = time.time()
        
        game_time = end_time - start_time
        total_time += game_time
        print(f"  Run {i+1}: {game_time:.4f} seconds")
    
    print(f"\n Starting Board ({runs} runs):")
    print(f"   Total: {total_time:.4f} seconds")
    print(f"   Average: {total_time/runs:.4f} seconds\n")
    
    # Test 2: Mittelspiel

    total_time = 0
    
    for i in range(runs):
        config.board = [
            [0, 0, B, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, 0, B, 0, 0],
            [0, B, 0, W, 0, W, 0, 0, 0],
            [0, 0, 0, B, 0, 0, 0, B, 0],
            [B, W, W, 0, K, W, W, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, B, 0],
            [0, 0, 0, W, 0, 0, W, 0, 0],
            [0, 0, 0, W, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, B, B, 0, B, 0]
        ]
        config.reset_pieces()
        config.onTurn = "Black"
        print(f"Spiel {i+1}")
        start_time = time.time()
        scr.main.main()
        end_time = time.time()
        
        game_time = end_time - start_time
        total_time += game_time
        print(f"  Dauer {i+1}: {game_time:.4f} Sekunden")
    
    print(f"\n Mid Board ({runs} runs):")
    print(f"   Total: {total_time:.4f} seconds")
    print(f"   Average: {total_time/runs:.4f} seconds\n")
    
    # Test 3: Endspiel (angepasst an dein ursprÃ¼ngliches Board)
    
    total_time = 0
    
    for i in range(runs):
    #    #config.board = [
    #    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #    #    [0, 0, 0, B, 0, 0, 0, 0, 0],
    #    #    [0, 0, 0, 0, 0, 0, B, B, B],
    #    #    [B, 0, 0, 0, 0, B, B, K, 0],
    #    #    [0, 0, 0, 0, 0, 0, B, 0, B],
    #    #    [0, 0, 0, 0, 0, 0, 0, B, 0],
    #    #    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    #    #]
        config.board = [
            [0, 0, B, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, W, 0, 0, 0],
            [0, 0, 0, B, 0, 0, 0, 0, 0],
            [0, W, 0, W, 0, 0, 0, 0, 0],
            [B, 0, 0, 0, 0, 0, 0, K, 0],
            [0, 0, W, 0, 0, 0, B, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        config.reset_pieces()
        config.onTurn = "Black"
        print(f"Spiel {i+1}")
        start_time = time.time()
        scr.main.main()
        end_time = time.time()
        
        game_time = end_time - start_time
        total_time += game_time
        print(f"  Dauer {i+1}: {game_time:.4f} Sekunden")
    
    print(f"\n End Board ({runs} Sekunden):")
    print(f"   Gesamt: {total_time:.4f} Sekunden")
    print(f"   Durchschnitt: {total_time/runs:.4f} Sekunden\n")

    print("=" * 60)
    print("BENCHMARK COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    benchmark()