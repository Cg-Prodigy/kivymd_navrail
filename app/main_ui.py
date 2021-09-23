from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem


class EntryPoint(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(20):
            self.opt = OneLineListItem(
                text=f'Text Number {i}'
            )


class IntroScreen(MDScreen):
    pass
