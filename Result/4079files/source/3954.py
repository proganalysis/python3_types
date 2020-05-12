#!/usr/bin/env python3
import argparse
import json
import os
from PIL import Image


class IconGenerator:
    def __init__(self):
        # default parameters
        self.platform = 'ios'
        self.quality = 100
        self.output = os.getcwd()
        self.anti_alias = True
        self.image = None


    def generate_icon(self):
        real_path = os.path.split(os.path.realpath(__file__))[0]

        platform_json_file = {
            'ios': 'ios',
            'iphone': 'iphone',
            'ipad': 'ipad',
            'macos': 'macos',
            'watchos': 'watchos',
            'mac': 'macos',
            'watch': 'watchos'
        }

        with open(os.path.join(real_path, 'config', platform_json_file[self.platform], 'Contents.json'), 'r') as f:
            content_json = json.load(f)

        self.output = os.path.join(self.output, 'AppIcon.appiconset')
        if not os.path.isdir(self.output):
            os.mkdir(self.output)


        for item in content_json['images']:
            size_tuple = str(item['size']).split('x')
            size = (float(size_tuple[0]), float(size_tuple[1]))
            scale = float(str(item['scale']).split('x')[0])
            file_name = self.resize_image(True, size, scale)
            item['filename'] = file_name

        with open(os.path.join(self.output, 'Contents.json'), 'w') as w:
            json.dump(content_json, w, indent=4)

        print('🎉 Done: Iconset generated successfully.')


    def generate_image_set(self, name: str, target_size: (float, float)):
        real_path = os.path.split(os.path.realpath(__file__))[0]
        with open(os.path.join(real_path, 'config', 'imageset', 'Contents.json'), 'r') as f:
            image_set_json = json.load(f)

        self.output = os.path.join(self.output, name + '.imageset')
        if not os.path.isdir(self.output):
            os.mkdir(self.output)

        image_size = self.image.size

        if target_size != None:
            if target_size[0] > 0 and target_size[1] == 0:
                target_size = (target_size[0], image_size[1] * target_size[0] / image_size[0])
            elif target_size[1] > 0 and target_size[0] == 0:
                target_size = (image_size[0] * target_size[1] / image_size[1], target_size[1])

        for item in image_set_json['images']:
            scale = float(str(item['scale']).split('x')[0])
            if target_size == None or target_size == (0, 0):
                # 3x size is given
                file_name = self.resize_image(False, image_size, scale)
            else:
                # 1x size is given
                file_name = self.resize_image(True, target_size, scale)

            item['filename'] = file_name

        with open(os.path.join(self.output, 'Contents.json'), 'w') as w:
            json.dump(image_set_json, w, indent=4)

        print('🎉 Done: Imageset generated successfully.')



    def resize_image(self, target_size_given: bool, size: (float, float), scale: float) -> str:
        if str(size[0]).endswith('.5'):
            size_str = str(size[0])
        else:
            size_str = str(int(size[0]))

        scale_str = str(int(scale))

        # Whether 1x size is given
        if target_size_given:
            if self.anti_alias:
                new_image = self.image.resize(tuple([int(size[0] * scale), int(size[1] * scale)]), Image.ANTIALIAS)
            else:
                new_image = self.image.resize(tuple([int(size[0] * scale), int(size[1] * scale)]))
        else:
            if self.anti_alias:
                new_image = self.image.resize(tuple([int(size[0] * scale / 3.0), int(size[1] * scale / 3.0)]),
                                         Image.ANTIALIAS)
            else:
                new_image = self.image.resize(tuple([int(size[0] * scale / 3.0), int(size[1] * scale / 3.0)]))

        image_file_name = 'Icon-' + size_str + '@' + scale_str + 'x.png'
        new_image_name = os.path.join(self.output, image_file_name)
        new_image.save(new_image_name, quality=self.quality)
        return image_file_name


if __name__ == '__main__':
    # Define arguments
    parser = argparse.ArgumentParser(prog='IconPy')
    parser.add_argument('input', help='input image of the icon. For Imageset, please input an image of 3x scale.', type=str)
    parser.add_argument('output', help='directory of output file.', type=str)
    parser.add_argument('-p', '--platform', help='platform for icon set. Following parameter should be ios/iphone/ipad/macos/watchos. Default is iOS (Universal icon for iPhone and iPad).')
    parser.add_argument('-q', '--quality', help='quality of resized icons. Integer from 0 to 100.', type=int)
    parser.add_argument('-n', '--nonantialiasing', help='disable anti-aliasing but may decrease quality. Enabling anti-aliasing may increase the size.', action='store_true')
    parser.add_argument('-i', '--imageset', help='export Imageset instead of Appiconset. Following parameter should be the name of the icon.')
    parser.add_argument('-w', '--width', help='1x width of exported Imageset', type=float)
    parser.add_argument('-l', '--length', help='1x height of exported Imageset', type=float)

    # Parse arguments
    args = parser.parse_args()

    icon_generator = IconGenerator()
    input_image = os.path.expanduser(args.input)

    output_directory = os.path.expanduser(args.output)
    if output_directory:
        icon_generator.output = output_directory

    if not (not args.quality or args.quality < 0 or args.quality > 100):
        icon_generator.quality = args.quality

    if args.nonantialiasing:
        icon_generator.anti_alias = False

    if args.platform:
        icon_generator.platform = args.platform

    # Basic checks
    if not os.path.isdir(output_directory):
        print('❌ Exit: Please input a valid output path.')
        exit()

    if os.path.isfile(input_image):
        try:
            icon_generator.image = Image.open(input_image)
        except:
            print('❌ Exit: Input file is not a valid image.')
            exit()
    else:
        print('❌ Exit: Input image does not exist.')
        exit()

    # Execute functions
    if args.imageset == None:
        if args.width:
            print('⛔️ Warning: Width parameter is ignored when target is iconset.')
        if args.length:
            print('⛔️ Warning: Length parameter is ignored when target is iconset.')
        icon_generator.generate_icon()
    else:
        if args.width == None:
            width = 0
        elif args.width <= 0:
            width = 0
            print('⛔️ Warning: Width parameter is ignored because it must be greater than 0.')
        else:
            width = args.width

        if args.length == None:
            length = 0
        elif args.length <= 0:
            length = 0
            print('⛔️ Warning: Length parameter is ignored because it must be greater than 0.')
        else:
            length = args.length

        target_size = (width, length)
        icon_generator.generate_image_set(args.imageset, target_size)
