from pynput import keyboard
import threading
import time
import reqQuotes as rq
INPS = []


def on_press(key):
    try:
        INPS.append(key.char)
        print(key.char, end="", flush=True)
    except AttributeError:
        if key == key.space:
            INPS.append(" ")
            print(" ", end="", flush=True)
        
        # Handle backspace
        elif key == key.backspace:
            if len(INPS) != 0:
                INPS.pop()
                print("\b \b", end="", flush=True)
            pass
            
def game():
    start = time.time()
    while len(INPS) < len(TARGET):
        time.sleep(0.1)
    end = time.time()

    elapsed = end - start
    wpm = (len("".join(INPS)) / 5) / (elapsed / 60)
    correct = sum(1 for i, c in enumerate("".join(INPS)) if i < len(TARGET) and c == TARGET[i])
    accuracy = correct / len(TARGET) * 100

    # Display time taken, WPM, and Accuracy
    print(f"\nTime: {elapsed:.2f} seconds")
    print(f"WPM: {wpm:.2f}")
    print(f"Accuracy: {accuracy:.2f}%")           
    
    # Create controller to emulate keyboard
    c = keyboard.Controller()
    # Stop characters from filling terminal line
    for i in range(len(TARGET)):
        c.press(keyboard.Key.backspace)
        c.release(keyboard.Key.backspace)
    # Stop listener and exit program
    listener.stop() 
    exit()

# Use API to get random quotes. No key needed.
TARGET = rq.get_random_quote()

print("Starting in:")
for i in [3, 2, 1]:
    print(i)
    time.sleep(1)
print(TARGET, "\n")

# Create thread to start game
thread = threading.Thread(target=game)
thread.daemon = True
thread.start()

listener =  keyboard.Listener(on_press=on_press)
listener.start()
listener.join()

