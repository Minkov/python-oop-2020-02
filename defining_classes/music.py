class Music:
    def __init__(self, title, artist, lyrics):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def get_info(self):
        return f'This is {self.title} from {self.artist}'

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics


m = Music('ala bala nica', 'asdasd', 'ala bala nica, ')

print(m.get_info())
print(m.play())