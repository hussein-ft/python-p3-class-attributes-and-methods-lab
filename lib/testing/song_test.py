#!/usr/bin/env python3

from song import Song

# Reset class attributes before tests
Song.count = 0
Song.genre_count = {}
Song.artist_count = {}

class TestSong:
    '''Class "Song" in song.py'''

    # Create some song instances for testing
    Song("99 Problems", "Jay Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert out_of_touch.name == "Out of Touch"
        assert out_of_touch.artist == "Hall and Oates"
        assert out_of_touch.genre == "Pop"

    def test_counts_songs(self):
        '''tracks the total number of songs created.'''
        assert Song.count == 4

    def test_genre_count(self):
        '''tracks the number of songs in each genre.'''
        assert Song.genre_count == {"Rap": 1, "Pop": 2, "Rock": 1}

    def test_artist_count(self):
        '''tracks the number of songs by each artist.'''
        assert Song.artist_count == {"Jay Z": 1, "Beyonce": 1, "Nirvana": 1, "Hall and Oates": 1}