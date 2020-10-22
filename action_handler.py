from pynput.keyboard import Key, Controller


def handle_actions(ges_dict, gesture):
    # After getting gesture that we draw,
    # find the index of relating action and return it.
    keys = []
    values = list(ges_dict.values())
    for key in list(ges_dict.keys()):
        keys.append(key.text().upper())
    ges_dict1 = dict(zip(keys, values))

    if gesture:
        # get action index
        print('What you draw is ' + gesture)
        action = ges_dict1.get(gesture)
        return action


def actionToSys(i):
    # initialize preset actions
    global keys
    keys = []
    print('action is: ' + str(i))

    if i == 1:
        keys = [Key.cmd, Key.ctrl, 'f']
    if i == 2:
        keys = [Key.cmd, 'm']
    if i == 3:
        keys = [Key.left]
    if i == 4:
        keys = [Key.right]
    if i == 5:
        keys = [Key.esc]
    if i == 6:
        keys = [Key.shift, Key.cmd, Key.enter]

    keyboard = Controller()
    for key in keys:
        keyboard.press(key)
    for key in keys:
        keyboard.release(key)
