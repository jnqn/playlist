import unittest
from playlist import Playlist

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        # This runs before each test
        self.playlist = Playlist("Test Playlist")

    def test_playlist_creation(self):
        # Test if playlist is created with correct title
        self.assertEqual(self.playlist._title, "Test Playlist")
        self.assertEqual(str(self.playlist), "Playlist 'Test Playlist' with 0 tracks")

    def test_add_single_track(self):
        # Test adding a single track
        self.playlist.add_track("Song 1")
        self.assertEqual(self.playlist.list_tracks(), ["Song 1"])

    def test_add_multiple_tracks(self):
        # Test adding multiple tracks
        tracks = ["Song 1", "Song 2", "Song 3"]
        self.playlist.add_tracks(tracks)
        self.assertEqual(self.playlist.list_tracks(), tracks)

    def test_add_empty_tracks_list(self):
        # Test adding an empty list of tracks
        self.playlist.add_tracks([])
        self.assertLessEqual(self.playlist._tracks, [])

    def test_add_invalid_track_type(self):
        # Test adding an invalid track type
        with self.assertRaises(TypeError):
            self.playlist.add_track(123)

    def test_list_tracks(self):
        # Test listing tracks
        tracks = ["Song 1", "Song 2"]
        self.playlist.add_tracks(tracks)
        self.assertEqual(self.playlist.list_tracks(), tracks)

    def test_string_representation(self):
        # Test string representation of playlist
        self.playlist.add_track("Song 1")
        expected_str = "Playlist 'Test Playlist' with 1 tracks"
        self.assertEqual(str(self.playlist), expected_str)

if __name__ == '__main__':
    unittest.main()
