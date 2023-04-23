class Track:
    def __init__(self, id, year, album, artist, label, genre, title, duration):
        # TODO sanatize
        self.id = id
        self.year = year
        self.album = album
        self.artist = artist
        self.label = label
        self.genre = genre
        self.title = title
        self.duration = duration
        pass

    def duration_to_ms(self, duration_raw: str) -> str:
        if not duration_raw:
            return ""
        durations = duration_raw.split(":")
        ms = int(durations[0]) * 60000 + int(durations[1]) * 1000
        return ms if len(durations) == 2 else ms + int(durations[2])

    def get_header(self) -> list[str]:
        header = []
        for key in self.__dict__.keys():
            header.append(str(key))
        return header

    def get_values(self) -> str:
        return [self.__dict__[key] for key in self.get_header()]
