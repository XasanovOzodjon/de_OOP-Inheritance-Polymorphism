class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def play(self):
        return f"Playing Media: {self.title} ({self.year})"

class Song(Media):
    def __init__(self, title, year, artist):
        super().__init__(title, year)
        self.artist = artist

    def play(self):
        return f"Playing Song: {self.title}, Artist: {self.artist}, Year: {self.year}"
    
class Movie(Media):
    def __init__(self, title, year, actor):
        super().__init__(title, year)
        self.actor = actor

    def play(self):
        return f"Playing Movie: {self.title}, Actor: {self.actor}, Year: {self.year}"


class Podcast(Media):
    def __init__(self, title, year, host):
        super().__init__(title, year)
        self.host = host

    def play(self):
        return f"Playing Podcast: {self.title}, Host: {self.host}, Year: {self.year}"
    
    
def main():
    media_items = [
        Song(title="Odamlar nima deydi", year=2017, artist="konsta"),
        Movie(title="Qaynonam suyuqoyoq", year=2010, actor="Axat qayom"),
        Podcast(title="The Daily", year=2020, host="Michael Barbaro")
    ]

    for item in media_items:
        print(item.play())

if __name__ == "__main__":
    main()