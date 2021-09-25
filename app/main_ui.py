from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem
from kivy.utils import get_color_from_hex


class EntryPoint(ScreenManager):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_rail(self):
        rail = self.ids.nav_rail
        if rail.rail_state == 'open':
            rail.rail_state = 'close'
        else:
            rail.rail_state = 'open'

    def set_item_color(self, instance):
        instance.color_active = get_color_from_hex('#ff4500')
        instance.color_normal = [1, 1, 1]

    def set_colors(self, instance):
        print(instance.children)


class IntroScreen(MDScreen):
    pass
