from Xlib.display import Display
from Xlib import X
from Xlib.ext import record
from Xlib.protocol import rq
import time
from KeyListener import KeyListener


class Handler(object):
    def __init__(self, fed):

        self.disp = None
        self.listenerObject = fed

        self.keysym_map = {
            32: "SPACE",
            39: "'",
            44: ",",
            45: "-",
            46: ".",
            47: "/",
            48: "0",
            49: "1",
            50: "2",
            51: "3",
            52: "4",
            53: "5",
            54: "6",
            55: "7",
            56: "8",
            57: "9",
            59: ";",
            61: "=",
            91: "[",
            92: "\\",
            93: "]",
            96: "`",
            97: "a",
            98: "b",
            99: "c",
            100: "d",
            101: "e",
            102: "f",
            103: "g",
            104: "h",
            105: "i",
            106: "j",
            107: "k",
            108: "l",
            109: "m",
            110: "n",
            111: "o",
            112: "p",
            113: "q",
            114: "r",
            115: "s",
            116: "t",
            117: "u",
            118: "v",
            119: "w",
            120: "x",
            121: "y",
            122: "z",
            65293: "ENTER",
            65307: "ESC",
            65360: "HOME",
            65361: "ARROW_LEFT",
            65362: "ARROW_UP",
            65363: "ARROW_RIGHT",
            65505: "L_SHIFT",
            65506: "R_SHIFT",
            65507: "L_CTRL",
            65508: "R_CTRL",
            65513: "L_ALT",
            65514: "R_ALT",
            65515: "SUPER_KEY",
            65288: "BACKSPACE",
            65364: "ARROW_DOWN",
            65365: "PG_UP",
            65366: "PG_DOWN",
            65367: "END",
            65377: "PRTSCRN",
            65535: "DELETE",
            65383: "PRINT?",
            65509: "CAPS_LOCK",
            65289: "TAB",
            65470: "F1",
            65471: "F2",
            65472: "F3",
            65473: "F4",
            65474: "F5",
            65475: "F6",
            65476: "F7",
            65477: "F8",
            65478: "F9",
            65479: "F10",
            65480: "F11",
            65481: "F12"

        }
        # get current display
        self.disp = Display()
        self.root = self.disp.screen().root

        # Monitor keypress and button press
        self.context = self.disp.record_create_context(
            0,
            [record.AllClients],
            [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                'device_events': (X.KeyReleaseMask, X.ButtonReleaseMask),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
            }])
        self.disp.record_enable_context(self.context, self.handler)
        self.disp.record_free_context(self.context)

        while True:
            # Infinite wait, doesn't do anything as no events are grabbed
            event = self.root.display.next_event()

    def keyBind(self, sym):
        if sym in self.keysym_map:
            return self.keysym_map[sym]
        else:
            return sym

    def handler(self, reply):
        """ This function is called when a xlib event is fired """
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(
                data, self.disp.display, None, None)

            keycode = event.detail
            keysym = self.disp.keycode_to_keysym(event.detail, 0)

            if keysym in self.keysym_map:
                character = self.keyBind(keysym)
                # print character
                if event.type == X.KeyPress:
                    self.listenerObject.press(character)
                elif event.type == X.KeyRelease:
                    self.listenerObject.release(character)
