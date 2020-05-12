#
# Gigatron built-in 5x8 font for ASCII codes 32 (SP) to 127 (DEL)
#

def _char(*args):
  """Convert character from easy-readable strings data into ROM bytes"""
  X, Y = len(args[0]), len(args)
  bytes = []
  for x in range(X):
    byte = 0
    for y in range(Y):
      bit = 0 if args[y][x]=='.' else 1
      byte = 2*byte + bit
    bytes.append(byte)
  return bytes

font = [
  _char(   #' '
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'!'
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '.....',
    '..#..',
    '.....'),
  _char(   #'"'
    '##.##',
    '.#..#',
    '#..#.',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'#'
    '.#.#.',
    '.#.#.',
    '#####',
    '.#.#.',
    '#####',
    '.#.#.',
    '.#.#.',
    '.....'),
  _char(   #'$'
    '..#..',
    '.####',
    '#.#..',
    '.###.',
    '..#.#',
    '####.',
    '..#..',
    '.....'),
  _char(   #'%'
    '##...',
    '##..#',
    '...#.',
    '..#..',
    '.#...',
    '#..##',
    '...##',
    '.....'),
  _char(   #'&'
    '.#...',
    '#.#..',
    '#.#..',
    '.#...',
    '#.#.#',
    '#..#.',
    '.##.#',
    '.....'),
  _char(   #"'"
    '.##..',
    '..#..',
    '.#...',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'('
    '...#.',
    '..#..',
    '.#...',
    '.#...',
    '.#...',
    '..#..',
    '...#.',
    '.....'),
  _char(   #'),'
    '.#...',
    '..#..',
    '...#.',
    '...#.',
    '...#.',
    '..#..',
    '.#...',
    '.....'),
  _char(   #'*'
    '.....',
    '..#..',
    '#.#.#',
    '.###.',
    '#.#.#',
    '..#..',
    '.....',
    '.....'),
  _char(   #'+'
    '.....',
    '..#..',
    '..#..',
    '#####',
    '..#..',
    '..#..',
    '.....',
    '.....'),
  _char(   #','
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.##..',
    '..#..',
    '.#...'),
  _char(   #'-'
    '.....',
    '.....',
    '.....',
    '#####',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'.'
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.##..',
    '.....'),
  _char(   #'/'
    '.....',
    '...#.',
    '...#.',
    '..#..',
    '..#..',
    '.#...',
    '.#...',
    '.....'),
  _char(   #'0'
    '.###.',
    '#...#',
    '#..##',
    '#.#.#',
    '##..#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'1'
    '..#..',
    '.##..',
    '#.#..',
    '..#..',
    '..#..',
    '..#..',
    '#####',
    '.....'),
  _char(   #'2'
    '.###.',
    '#...#',
    '....#',
    '..##.',
    '.#...',
    '#....',
    '#####',
    '.....'),
  _char(   #'3'
    '.###.',
    '#...#',
    '....#',
    '..##.',
    '....#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'4'
    '...#.',
    '..##.',
    '.#.#.',
    '#..#.',
    '#####',
    '...#.',
    '...#.',
    '.....'),
  _char(   #'5'
    '#####',
    '#....',
    '####.',
    '....#',
    '....#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'6'
    '.###.',
    '#...#',
    '#....',
    '####.',
    '#...#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'7'
    '#####',
    '....#',
    '...#.',
    '..#..',
    '.#...',
    '.#...',
    '.#...',
    '.....'),
  _char(   #'8'
    '.###.',
    '#...#',
    '#...#',
    '.###.',
    '#...#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'9'
    '.###.',
    '#...#',
    '#...#',
    '.####',
    '....#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #':'
    '.....',
    '.....',
    '.##..',
    '.....',
    '.....',
    '.##..',
    '.....',
    '.....'),
  _char(   #';'
    '.....',
    '.....',
    '.....',
    '.##..',
    '.....',
    '.##..',
    '..#..',
    '.#...'),
  _char(   #'<'
    '...#.',
    '..#..',
    '.#...',
    '#....',
    '.#...',
    '..#..',
    '...#.',
    '.....'),
  _char(   #'='
    '.....',
    '.....',
    '#####',
    '.....',
    '.....',
    '#####',
    '.....',
    '.....'),
  _char(   #'>'
    '.#...',
    '..#..',
    '...#.',
    '....#',
    '...#.',
    '..#..',
    '.#...',
    '.....'),
  _char(   #'?'
    '.###.',
    '#...#',
    '....#',
    '...#.',
    '..#..',
    '.....',
    '..#..',
    '.....'),
  _char(   #'@'
    '.###.',
    '#...#',
    '....#',
    '.##.#',
    '#.#.#',
    '#.#.#',
    '.###.',
    '.....'),
  _char(   #'A'
    '..#..',
    '.#.#.',
    '#...#',
    '#...#',
    '#####',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'B'
    '####.',
    '#...#',
    '#...#',
    '####.',
    '#...#',
    '#...#',
    '####.',
    '.....'),
  _char(   #'C'
    '.###.',
    '#...#',
    '#....',
    '#....',
    '#....',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'D'
    '###..',
    '#..#.',
    '#...#',
    '#...#',
    '#...#',
    '#..#.',
    '###..',
    '.....'),
  _char(   #'E'
    '#####',
    '#....',
    '#....',
    '####.',
    '#....',
    '#....',
    '#####',
    '.....'),
  _char(   #'F'
    '#####',
    '#....',
    '#....',
    '####.',
    '#....',
    '#....',
    '#....',
    '.....'),
  _char(   #'G'
    '.###.',
    '#...#',
    '#....',
    '#..##',
    '#...#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'H'
    '#...#',
    '#...#',
    '#...#',
    '#####',
    '#...#',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'I'
    '.###.',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '.###.',
    '.....'),
  _char(   #'J'
    '..###',
    '...#.',
    '...#.',
    '...#.',
    '...#.',
    '#..#.',
    '.##..',
    '.....'),
  _char(   #'K'
    '#...#',
    '#..#.',
    '#.#..',
    '##...',
    '#.#..',
    '#..#.',
    '#...#',
    '.....'),
  _char(   #'L'
    '#....',
    '#....',
    '#....',
    '#....',
    '#....',
    '#....',
    '#####',
    '.....'),
  _char(   #'M'
    '#...#',
    '##.##',
    '#.#.#',
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'N'
    '#...#',
    '#...#',
    '##..#',
    '#.#.#',
    '#..##',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'O'
    '.###.',
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'P'
    '####.',
    '#...#',
    '#...#',
    '####.',
    '#....',
    '#....',
    '#....',
    '.....'),
  _char(   #'Q'
    '.###.',
    '#...#',
    '#...#',
    '#...#',
    '#.#.#',
    '#..#.',
    '.##.#',
    '.....'),
  _char(   #'R'
    '####.',
    '#...#',
    '#...#',
    '####.',
    '#.#..',
    '#..#.',
    '#...#',
    '.....'),
  _char(   #'S'
    '.####',
    '#....',
    '#....',
    '.###.',
    '....#',
    '....#',
    '####.',
    '.....'),
  _char(   #'T'
    '#####',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '.....'),
  _char(   #'U'
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'V'
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '.#.#.',
    '.#.#.',
    '..#..',
    '.....'),
  _char(   #'W'
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '#.#.#',
    '##.##',
    '#...#',
    '.....'),
  _char(   #'#'
    '#...#',
    '#...#',
    '.#.#.',
    '..#..',
    '.#.#.',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'Y'
    '#...#',
    '#...#',
    '#...#',
    '.#.#.',
    '..#..',
    '..#..',
    '..#..',
    '.....'),
  _char(   #'Z'
    '#####',
    '....#',
    '...#.',
    '..#..',
    '.#...',
    '#....',
    '#####',
    '.....'),
  _char(   #'['
    '.###.',
    '.#...',
    '.#...',
    '.#...',
    '.#...',
    '.#...',
    '.###.',
    '.....'),
  _char(   #'\\'
    '.....',
    '.#...',
    '.#...',
    '..#..',
    '..#..',
    '...#.',
    '...#.',
    '.....'),
  _char(   #']'
    '.###.',
    '...#.',
    '...#.',
    '...#.',
    '...#.',
    '...#.',
    '.###.',
    '.....'),
  _char(   #'^'
    '..#..',
    '.#.#.',
    '#...#',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'_'
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....',
    '#####',
    '.....'),
  _char(   #'`'
    '..##.',
    '..#..',
    '...#.',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'a'
    '.....',
    '.....',
    '.###.',
    '....#',
    '.####',
    '#...#',
    '.####',
    '.....'),
  _char(   #'b'
    '#....',
    '#....',
    '####.',
    '#...#',
    '#...#',
    '#...#',
    '####.',
    '.....'),
  _char(   #'c'
    '.....',
    '.....',
    '.###.',
    '#...#',
    '#....',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'d'
    '....#',
    '....#',
    '.####',
    '#...#',
    '#...#',
    '#...#',
    '.####',
    '.....'),
  _char(   #'e'
    '.....',
    '.....',
    '.###.',
    '#...#',
    '#####',
    '#....',
    '.###.',
    '.....'),
  _char(   #'f'
    '..##.',
    '.#..#',
    '.#...',
    '###..',
    '.#...',
    '.#...',
    '.#...',
    '.....'),
  _char(   #'g'
    '.....',
    '.....',
    '.###.',
    '#...#',
    '#...#',
    '.####',
    '....#',
    '.###.'),
  _char(   #'h'
    '#....',
    '#....',
    '####.',
    '#...#',
    '#...#',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'i'
    '..#..',
    '.....',
    '.##..',
    '..#..',
    '..#..',
    '..#..',
    '.###.',
    '.....'),
  _char(   #'j'
    '...#.',
    '.....',
    '..##.',
    '...#.',
    '...#.',
    '...#.',
    '#..#.',
    '.##..'),
  _char(   #'k'
    '#....',
    '#....',
    '#..#.',
    '#.#..',
    '###..',
    '#..#.',
    '#...#',
    '.....'),
  _char(   #'l'
    '.##..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '.###.',
    '.....'),
  _char(   #'m'
    '.....',
    '.....',
    '##.#.',
    '#.#.#',
    '#.#.#',
    '#.#.#',
    '#...#',
    '.....'),
  _char(   #'n'
    '.....',
    '.....',
    '#.##.',
    '##..#',
    '#...#',
    '#...#',
    '#...#',
    '.....'),
  _char(   #'o'
    '.....',
    '.....',
    '.###.',
    '#...#',
    '#...#',
    '#...#',
    '.###.',
    '.....'),
  _char(   #'p'
    '.....',
    '.....',
    '####.',
    '#...#',
    '#...#',
    '####.',
    '#....',
    '#....'),
  _char(   #'q'
    '.....',
    '.....',
    '.####',
    '#...#',
    '#...#',
    '.####',
    '....#',
    '....#'),
  _char(   #'r'
    '.....',
    '.....',
    '#.##.',
    '##..#',
    '#....',
    '#....',
    '#....',
    '.....'),
  _char(   #'s'
    '.....',
    '.....',
    '.###.',
    '#....',
    '.###.',
    '....#',
    '####.',
    '.....'),
  _char(   #'t'
    '.#...',
    '.#...',
    '###..',
    '.#...',
    '.#...',
    '.#..#',
    '..##.',
    '.....'),
  _char(   #'u'
    '.....',
    '.....',
    '#...#',
    '#...#',
    '#...#',
    '#..##',
    '.##.#',
    '.....'),
  _char(   #'v'
    '.....',
    '.....',
    '#...#',
    '#...#',
    '#...#',
    '.#.#.',
    '..#..',
    '.....'),
  _char(   #'w'
    '.....',
    '.....',
    '#...#',
    '#...#',
    '#.#.#',
    '#.#.#',
    '.#.#.',
    '.....'),
  _char(   #'x'
    '.....',
    '.....',
    '#...#',
    '.#.#.',
    '..#..',
    '.#.#.',
    '#...#',
    '.....'),
  _char(   #'y'
    '.....',
    '.....',
    '#...#',
    '#...#',
    '#...#',
    '.####',
    '....#',
    '.###.'),
  _char(   #'z'
    '.....',
    '.....',
    '#####',
    '...#.',
    '..#..',
    '.#...',
    '#####',
    '.....'),
  _char(   #'{'
    '..##.',
    '.#...',
    '.#...',
    '#....',
    '.#...',
    '.#...',
    '..##.',
    '.....'),
  _char(   #'|'
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '..#..',
    '.....'),
  _char(   #'}'
    '.##..',
    '...#.',
    '...#.',
    '....#',
    '...#.',
    '...#.',
    '.##..',
    '.....'),
  _char(   #'~'
    '.#...',
    '#.#.#',
    '...#.',
    '.....',
    '.....',
    '.....',
    '.....',
    '.....'),
  _char(   #'\x7f'
    '#####',
    '#####',
    '#####',
    '#####',
    '#####',
    '#####',
    '#####',
    '.....')
]
