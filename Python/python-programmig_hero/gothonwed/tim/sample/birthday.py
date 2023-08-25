class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        self.paths = {}

    def sing_me_a_song(self, sond):
        #for line in self.lyrics:
        #print(self.lyrics)
        return self.paths.get(sond, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)

happy_bday = Song("""
Happy birthday to you🎂
How old are you now?
How old are you now?
I don't want to get sued😁
So I'll stop right there🎉""")

bulls_on_parade = Song("""
They relly arround the familly🎃
with pockets full of shell🐚🦐

-> bulls
""")

poem = Song("""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.

-> poem
""")

happy_bday.add_paths({
    '21':bulls_on_parade
})
bulls_on_parade.add_paths({
    'bulls': poem
})
poem.add_paths({
    'poem': happy_bday
})

START = 'bulls_on_parade'

def load_lyrics(lyrics):
    """
    There is a potential security problem here.
    Who gets to set name? Can that expose a variable?
    """
    return globals().get(lyrics)

def lyrics_name(lyrics):
    """
    Same possible security problem. Can you trust room?
    What's a better solution than this globals lookup?
    """
    for key, value in globals().items():
        if value == lyrics:
            return key