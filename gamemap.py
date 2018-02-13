class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

class StartTile(MapTile):
    def intro_text(self):
        return """
        It's an unfamiliar room. You don't know how you got there, or how to get out,
        but it doesn't seem threatening. 
        """

class ChairTile(MapTile):
    def intro_text(self):
        return '''
        There's an odd, ancient chair that you for some reason don't recall to
        have seen before leaning up against the wall. It looks uncomfortable.
        '''

class TableTile(MapTile):
    def intro_text(self):
        return '''
        It's a beaten-up wooden table, dirty and old. There's a layer of dust
        on it that makes you suspect that no one's used it in quite some time.
        '''

class ShelfTile(MapTile):
    def intro_text(self):
        return '''
        Here is a modern-looking bookshelf with a couple books on it. It's the
        only thing in the room that looks like it's been taken care of.
        '''

class BooksTile(MapTile):
    def intro_text(self):
        return '''
        There are books strewn all over the floor. They all have rather boring
        looking covers. The layer of dust on them seems thinner on them.
        '''

class LampTile(MapTile):
    def intro_text(self):
        return '''
        It's an odd looking lamp with no lightbulb.
        '''

class WallTile(MapTile):
    def intro_text(self):
        return '''
        Your nose bumps into the old, rough walls. Why did you walk this far
        again?
        '''

class KnifeWallTile(MapTile):
    def intro_text(self):
        return '''
        Your nose bumps into the old, rough walls. Squinting through the ashy dust,
        you notice that the wall seems have pieces taken out of it, as if someone
        had attacked it.
        '''
    
class NothingTile(MapTile):
    def intro_text(self):
        return '''
        There's a thick layer of dust on the ground. It reminds you morbidly of
        ash.
        '''

class DustTile(MapTile):
    def intro_text(self):
        return '''
        There is a large pile of dust against this wall. You feel strangely morose.
        '''

world_map = [
    [DustTile() , KnifeWallTile() , WallTile() , WallTile(), KnifeWallTile() , WallTile()]
    [WallTile() , NothingTile() , LampTile() , TableTile() , NothingTile() , WallTile()]
    [DustTile(), NothingTile(), NothingTile(), NothingTile(), NothingTile(), DustTile()]
    [WallTile(), NothingTile(), StartTile(), NothingTile(), NothingTile(), ChairTile()]
    [ShelfTile(), WallTile(), WallTile(), DustTile(), WallTile(), KnifeWallTile()]
]

def tile_at(x,y):
    if x<0 or y<0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
    
