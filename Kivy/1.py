from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition, CardTransition, SwapTransition
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown

class Menu(Screen):
    pass

class Play1(Screen):
    pass

class MainApp(App):
    def build(self):
        sm = ScreenManager(transition = SwapTransition())
        sm.add_widget(Menu(name = "menu"))
        sm.add_widget(Play1(name = "play1"))
        return sm


if __name__ == "__main__":
    MainApp().run()