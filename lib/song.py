class Song:
    count = 0
    artists = ["Jay-Z", "Drake", "Beyonce"]
    genres = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.increase_artist_count()
        self.artist = artist
        self.genre = genre
        self.name = name
        self.increase_genre_count(genre)
        self.add_genre(genre)
        self.add_artist(artist)
        self.add_artist_count(artist)
        pass
    @classmethod
    def add_genre(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)
    @classmethod
    def increase_artist_count(cls, increment=1):
        cls.count+= increment
    @classmethod
    def increase_genre_count(cls, genre):
        if cls.genre_count.get(genre):
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1
    @classmethod
    def add_artist(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    @classmethod
    def add_artist_count(cls, artist):
        if cls.artist_count.get(artist):
            cls.artist_count[artist]+=1
        else:
            cls.artist_count[artist] = 1

    pass
