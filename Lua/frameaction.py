class Btn_t:
    """Enum of button presses"""
    # UNKNOWNs are stand-ins for the
    # buttons I don't yet know
    UNKNOWN1 = 0
    UNKNOWN2 = 1
    UNKNOWN3 = 2
    R = 3
    UNKNOWN4 = 4
    UNKNOWN5 = 5
    UNKNOWN6 = 6
    UNKNOWN7 = 7
    X = 8
    A = 9
    UNKNOWN8 = 10
    UNKNOWN9 = 11
    
    @classmethod
    def all_buttons(cls):
        """Returns a list of all button flags in order"""
        return tuple((cls.UNKNOWN1, cls.UNKNOWN2, cls.UNKNOWN3, cls.R,
           cls.UNKNOWN4, cls.UNKNOWN5, cls.UNKNOWN6, cls.UNKNOWN7,
           cls.X, cls.A, cls.UNKNOWN8, cls.UNKNOWN9))


class Frame(object):
    """One frame of gameplay, can be viewed as either a
    line in a mnemonic file or bit flags that represent
    whether or not each button is pressed"""
    
    btn_representations = ['?', '?', '?', 'R', '?', '?', '?', '?', 'X', 'A', '?', '?']
    # characters of each button that will show up in the mnemonic frame
    # ^ as of right now ?'s stand in for buttons that I am not familiar with
    
    def __init__(self, *flags):
        self._bitvalue = 0
        self._bitvalue = self.add_buttons(*flags)

    @property
    def bitvalue(self):
        return self._bitvalue

    def __str__(self):
        """Shows the frame as it should appear to the mnemonic reader"""
        characters = []
        all_flags = zip(Btn_t.all_buttons(), self.__class__.btn_representations)
        for flag, btn_char in all_flags:
            characters.append(btn_char if self.has_button(flag) else '.')
        return '|..|' + ''.join(characters) + '|............|'

    def add_buttons(self, *flags):
        """Add buttons if not already pressed"""
        for f in flags:
            self._bitvalue |= (1 << f)
        return self.bitvalue

    def remove_buttons(self, *flags):
        """Remove buttons if pressed"""
        for f in flags:
            self._bitvalue &= ~(1 << f)
        return self.bitvalue

    def toggle_buttons(self, *flags):
        """Flip buttons on and off"""
        for f in flags:
            self._bitvalue ^= (1 << f)
        return self.bitvalue

    def has_button(self, button_flag):
        return bool(self.bitvalue & (1 << button_flag))

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    frame = Frame(Btn_t.R, Btn_t.X)
    print frame

