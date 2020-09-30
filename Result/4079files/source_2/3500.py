import sys
sys.path.append('../modules')
import gl_main
import stateSystem
#import yaml
#import mega
import ByteFont

def std_keypress(key_sym, world=None):
    keyboard_fun = {
            'H':lambda x, y: x,
            }
    keyboard_fun.get(key_sym, lambda x, y: x)(key_sym, world)

def std_draw(_):
    ByteFont.draw_text('a', y=0, x=1, color=(1, 1, 1))

####
def init():
    stateSystem.addState('std')
    stateSystem.changeState('std')
    stateSystem.setEventHandler('std', 'keypress', std_keypress)
    stateSystem.setEventHandler('std', 'draw', std_draw)
    font = ByteFont.init_font(ByteFont.font_file, 10, 16)
    font10x16 = ByteFont.init_font(ByteFont.font_file10x16, 10, 16)
    ByteFont.set_fonts(font, font10x16)

def DrawGLScene():
    gl_main.gl_draw_pre()
    stateSystem.handleEvent('draw', None)
    gl_main.gl_error_msg()

def keyPressed(*args):
    if args[0] == gl_main.ESCAPE:
        sys.exit()
    if ord(args[0]) > 127:
        print('Switch to Latin keyboard layout. Переключите на латинскую раскладку.')
        return
    key_sym = bytes.decode(args[0])
    #print(key_sym, ord(args[0]))
    stateSystem.handleEvent('keypress', key_sym, None)

def main():
    gl_main.gl_main(name='menvod', draw_func=DrawGLScene, key_func=keyPressed)
    init()
    gl_main.gl_start()

if __name__=='__main__':
    main() 
