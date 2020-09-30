#!/usr/bin/env python3
import wx
import wx.xrc
from iconpy import IconGenerator
import os
from PIL import Image


class ImageDrop(wx.FileDropTarget):
    def __init__(self, window):
        wx.FileDropTarget.__init__(self)
        self.window = window


    def OnDropFiles(self, x, y, filenames):
        if filenames:
            filename = filenames[0]
            self.window.input_text.SetValue(filename)
        return True


class Frame(wx.Frame):
    def __init__(self, parent=None):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='IconPy', pos=wx.DefaultPosition,
                          size=wx.Size(432, 430), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.icon_generator = None

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, "Input image", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        fgSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.input_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.input_text.SetMinSize(wx.Size(200, -1))
        fgSizer1.Add(self.input_text, 0, wx.ALL, 5)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, "or drag the image to the right", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        fgSizer1.Add(self.m_staticText7, 0, wx.ALL, 5)

        self.icon_image = wx.StaticBitmap(self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size(-1, -1), 0)
        self.icon_image.SetMinSize(wx.Size(135, 135))
        drop_target = ImageDrop(self)
        self.icon_image.SetDropTarget(drop_target)
        fgSizer1.Add(self.icon_image, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, "Platform", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        fgSizer1.Add(self.m_staticText2, 0, wx.ALL, 5)

        platform_choiceChoices = ["iOS (Universal)", "iPhone", "iPad", "macOS", "watchOS"]
        self.platform_choice = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, platform_choiceChoices, 0)
        self.platform_choice.SetSelection(0)
        fgSizer1.Add(self.platform_choice, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self, wx.ID_ANY, "Quality", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        fgSizer1.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.quality_slider = wx.Slider(self, wx.ID_ANY, 100, 0, 100, wx.DefaultPosition, wx.DefaultSize,
                                        wx.SL_HORIZONTAL)
        fgSizer1.Add(self.quality_slider, 0, wx.ALL, 5)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        fgSizer1.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.antialiasing_check = wx.CheckBox(self, wx.ID_ANY, "Antialiasing", wx.DefaultPosition, wx.DefaultSize, 0)
        self.antialiasing_check.SetValue(True)
        fgSizer1.Add(self.antialiasing_check, 0, wx.ALL, 5)

        self.m_staticText9 = wx.StaticText(self, wx.ID_ANY, "Width", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText9.Wrap(-1)
        fgSizer1.Add(self.m_staticText9, 0, wx.ALL, 5)

        self.width_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.width_text.SetMinSize(wx.Size(200, -1))

        fgSizer1.Add(self.width_text, 0, wx.ALL, 5)

        self.m_staticText11 = wx.StaticText(self, wx.ID_ANY, "Height", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText11.Wrap(-1)
        fgSizer1.Add(self.m_staticText11, 0, wx.ALL, 5)

        self.height_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.height_text.SetMinSize(wx.Size(200, -1))

        fgSizer1.Add(self.height_text, 0, wx.ALL, 5)

        self.iconset_btn = wx.Button(self, wx.ID_ANY, "Export AppIconset", wx.DefaultPosition, wx.DefaultSize, 0)
        self.iconset_btn.SetMinSize(wx.Size(144, -1))

        fgSizer1.Add(self.iconset_btn, 0, wx.ALL, 5)

        self.imageset_btn = wx.Button(self, wx.ID_ANY, "Export ImageSet", wx.DefaultPosition, wx.DefaultSize, 0)
        self.imageset_btn.SetMinSize(wx.Size(144, -1))

        fgSizer1.Add(self.imageset_btn, 0, wx.ALL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # bind events
        self.iconset_btn.Bind(wx.EVT_BUTTON, self.export_iconset)
        self.imageset_btn.Bind(wx.EVT_BUTTON, self.export_imageset)
        self.input_text.Bind(wx.EVT_TEXT, self.text_on_change)


    def export_imageset(self, event):
        with wx.FileDialog(self, 'Please choose a place to save Imageset', wildcard='ImageSet (*.imageset)|*.imageset',
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as save_dialog:
            if save_dialog.ShowModal() == wx.ID_CANCEL:
                return

            path = save_dialog.GetPath()
            image_set = os.path.basename(path)
            output = path[:-len(image_set)]

            self.construct_object(output)

            try:
                width = max(0, int(self.width_text.GetValue()))
            except:
                width = 0

            try:
                height = max(0, int(self.height_text.GetValue()))
            except:
                height = 0

            target_size = (width, height)
            self.icon_generator.generate_image_set(image_set[:-len('.imageset')], target_size)


    def export_iconset(self, event):
        with wx.DirDialog(self, 'Please choose a directory to save AppIconSet', '',
                          wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dlg:
            if dlg.ShowModal() == wx.ID_CANCEL:
                return

            output = dlg.GetPath()
            self.construct_object(output)
            self.icon_generator.generate_icon()


    def construct_object(self, output_path: str):
        self.icon_generator = IconGenerator()
        self.icon_generator.output = output_path

        input_image = str(self.input_text.GetValue())
        if os.path.isfile(input_image):
            try:
                self.icon_generator.image = Image.open(input_image)
            except:
                print('❌ Exit: Input file is not a valid image.')
                exit()
        else:
            print('❌ Exit: Input image does not exist.')
            exit()

        self.icon_generator.anti_alias = self.antialiasing_check.GetValue()
        self.icon_generator.quality = int(self.quality_slider.GetValue())
        self.icon_generator.platform = ['ios', 'iphone', 'ipad', 'macos', 'watchos'][self.platform_choice.GetSelection()]


    def __del__(self):
        pass


    def text_on_change(self, event):
        try:
            icon = wx.Image(self.input_text.GetValue(), wx.BITMAP_TYPE_ANY).Scale(135, 135, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
            self.icon_image.SetBitmap(icon)
        except:
            pass


class App(wx.App):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True


if __name__ == '__main__':
    app = App()
    app.MainLoop()
