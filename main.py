from pynput import keyboard
from write import increment, check_data_folder

check_data_folder()

def on_press(key):
    # try:
    #     print('alphanumeric key {0} pressed'.format(
    #         key.char))
    # except AttributeError:
    #     print('special key {0} pressed'.format(
    #         key))
    return

def on_release(key):
    # print('{0} released'.format(
    #     key))
    # if key == keyboard.Key.esc:
    #     # Stop listener
    #     return False
    num = increment()
    # print(num)
    

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


