from .object import WorldObject
from .textures import tex_coords

GRASS = tex_coords((1, 0), (0, 1), (0, 0))
SAND = tex_coords((1, 1), (1, 1), (1, 1))
BRICK = tex_coords((2, 0), (2, 0), (2, 0))
STONE = tex_coords((2, 1), (2, 1), (2, 1))


class Block(WorldObject):

    unique = False
    texture = None
    breakable = False

def get_block(id):
    if id == "brick":
        return Brick
    elif id == "grass":
        return Grass
    elif id == "sand":
        return Sand
    elif id == "weakstone":
        return WeakStone
    elif id == "stone":
        return Stone

class Brick(Block):
    texture = BRICK
    breakable = True


class Grass(Block):
    texture = GRASS
    breakable = True


class Sand(Block):
    texture = SAND
    breakable = True


class WeakStone(Block):
    texture = STONE
    breakable = True


class Stone(Block):
    texture = STONE
