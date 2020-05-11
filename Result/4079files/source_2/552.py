from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from ml_demo.screens import (
    MainScreen,
    NeuralNetworkScreen,
    DecisionTreeScreen,
    NeuralNetworkHelpScreen,
    DecisionTreeHelpScreen,
)


Builder.load_file('ml_demo/kv_files/mlgui.kv')

screen_manager = ScreenManager()

screen_manager.add_widget(MainScreen(name='main_screen'))
screen_manager.add_widget(NeuralNetworkScreen(name='nn_screen'))
screen_manager.add_widget(DecisionTreeScreen(name='dt_screen'))
screen_manager.add_widget(NeuralNetworkHelpScreen(name='nn_help'))
screen_manager.add_widget(DecisionTreeHelpScreen(name='dt_help'))


class MLGUIApp(App):

    def build(self):
        return screen_manager

mlgui = MLGUIApp()
mlgui.run()
