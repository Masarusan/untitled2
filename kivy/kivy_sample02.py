# -*- coding: utf-8 -*-

from kivy.app import App
from kivy.uix.label import Label

class TestApp(App):
    def build(self):
        return Label(text="Hello,World!!")
TestApp().run()

if __name__ == "__main__":
    pass