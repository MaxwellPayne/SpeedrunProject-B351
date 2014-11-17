class Btn_t:
    """Enum of button presses"""
    Up = 0
    Dn = 1
    Lt = 2
    Rt = 3
    Sl = 4
    St = 5
    Y = 6
    B = 7
    X = 8
    A = 9
    L = 10
    R = 11
    
    @classmethod
    def all_buttons(cls):
        """Returns a list of all button flags in order"""
        return tuple((cls.Up, cls.Dn, cls.Lt, cls.Rt,
           cls.Sl, cls.St, cls.Y, cls.B,
           cls.X, cls.A, cls.L, cls.R))


class Frame(object):
    """One frame of gameplay, can be viewed as either a
    line in a mnemonic file or bit flags that represent
    whether or not each button is pressed"""

    btn_representations = {Btn_t.Up: 'u',
                           Btn_t.Dn: 'd',
                           Btn_t.Lt: 'l',
                           Btn_t.Rt: 'r',
                           Btn_t.Sl: '&',
                           Btn_t.St: '*',
                           Btn_t.Y : 'Y',
                           Btn_t.B : 'B',
                           Btn_t.X : 'X',
                           Btn_t.A : 'A',
                           Btn_t.L : 'L',
                           Btn_t.R : 'R'}
    # characters of each button that will show up in the mnemonic frame
    
    def __init__(self, *flags, **kwargs):
        self._bitvalue = 0

        if flags and kwargs:
            raise ValueError('cannot init with both flags and frame_string')

        if 'frame_string' in kwargs: # init with existing string
            frame_string = kwargs['frame_string'][4:16]
            btn_flags = Btn_t.all_buttons()
            # convert P1 characters into flags
            flags_present = [btn_flags[idx] for idx, char in enumerate(frame_string) if char != '.']
            self.add_buttons(*flags_present)

        else: # init with the flags passed
            self.add_buttons(*flags)

    @property
    def bitvalue(self):
        return self._bitvalue

    def __str__(self):
        """Shows the frame as it should appear to the mnemonic reader"""
        characters, representations = [], self.__class__.btn_representations
        for flag in Btn_t.all_buttons():
            characters.append(representations[flag] if self.has_button(flag) else '.')
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
    
    frame = Frame(frame_string='|..|u..r....X...|............|')
    print frame

