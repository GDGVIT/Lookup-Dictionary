class KeyListener(object):
    def __init__(self):

        self.pressedKeys = []
        self.listeners = {}

    def press(self, character):

        self.pressedKeys.append(character)
        action = self.listeners.get(tuple(self.pressedKeys), False)
        if action:
            action()

    def release(self, character):
        if character in self.pressedKeys:
            self.pressedKeys.remove(character)

    def addKeyListener(self, hotkeys, callable):
        keys = tuple(hotkeys.split("+"))
        self.listeners[keys] = callable
