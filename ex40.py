class song(object):
    def __init__(self, lines):
        self.lines = lines

    def sing_a_song(self):
        for i in self.lines:
            print(i)

happy_bday1 = song(["Happy birthday to you",
                    "Happy birthaday dear papa",
                    "Many many returns of the day"])

happy_bday1.sing_a_song()
