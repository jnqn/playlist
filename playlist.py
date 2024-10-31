class Playlist:
    def __init__(self, title: str) -> None:
        if type(title) !=str:
            raise TypeError
        else:
            self._title = title
            self._tracks = []

    def __str__(self) -> str:
        return f"Playlist '{self._title}' with {len(self._tracks)} tracks"

    def __repr__(self) -> str:
        return f"Playlist(title='{self._title}')"

    def add_tracks(self, tracks: list[str]) -> None:
        for track in tracks:
            self.add_track(track)

    def add_track(self, track: str) -> None:
        if not isinstance(track, str):
            raise TypeError("Track must be a string")
        self._tracks.append(track)

    def list_tracks(self) -> list[str]:
        return self._tracks
