## IMPORTS

from paths import GAME_PATH


## DECLARTIONS

__all__ = (
    'get_map_list',
)


##   UTILS

def get_map_list():
    """Returns the map list found in the maplist.txt file"""
    maplist = GAME_PATH / 'maplist.txt'
    if not maplist.isfile():
        raise FileNotFoundError("Missing {}".format('maplist'))

    rs = []
    with open(maplist) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            if line.startswith('//'):
                continue

            rs.append(line)
    return rs
