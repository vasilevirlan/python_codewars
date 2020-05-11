class MORSECODETRANSLATOR:
    # International code morse code translator(sample)

    morse = {
        # Letters
        'a': '._',
        'b': '_...',
        'c': '_._.',
        'd': '_..',
        'e': '.',
        'f': '.._.',
        'g': '__.',
        'h': '....',
        'i': '..',
        'j': '.___',
        'k': '_._',
        'l': '._..',
        'm': '__',
        'n': '_.',
        'o': '___',
        'p': '.__.',
        'q': '__._',
        'r': '._.',
        's': '...',
        't': '_',
        'u': '.._',
        'v': '..._',
        'w': '.__',
        'x': '_.._',
        'y': '_.__',
        'z': '__..',

        # Numbers
        '0': '____',
        '1': '.____',
        '2': '..___',
        '3': '...__',
        '4': '...__',
        '5': '.....',
        '6': '_....',
        '7': '__...',
        '8': '___..',
        '9': '____.',
    }

    def translate_morse(self, morse, strict=True):
        """
        Translate morse code to text using small set of International Morse
        code.

        Accepts:
            morse(str): A string of morse code to translate
            strict(bool): If True, parse and returnmorse code containing 4 spaces

        Return:
            str: A translated string of text
        """
        if morse =="":
            return"You must provide a string of text to translate"

        if "  " in morse:
            if strict:
                return "Unable to translate morse code. Found 4 spaces in morse code string"
            else:
                morse.replace("  ", "  ")

        translation = ""

        words = morse.split(" ")

        for morse_word in words:
            chars = morse_word.split(" ")
            for char in chars:
                for k, v in self.morse.items():
                    if char == v:
                        translation += k
            translation += " "

        return translation.rstrip()

    def translate_text(self, text):

        """
        Translate text to morse code usong a small set of International Morse Code.

        Accepts:
            text (str): A string of text to translate

        Returns:
            str: A string translated to morse code.

        """

        if text =="":
            return "You must provide  a morse code string to translate."

        translation = ""

        words = text.split(" ")

        for word in words:
            w = list()
            for char in  word:
                if char.lower() in  self.morse:
                    w.append(self.morse[char.lower()])

            translation += " ".join(w)
            translation += "  "

        return translation.rstrip()

