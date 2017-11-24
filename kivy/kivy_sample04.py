# -*- coding: utf-8 -*-

from kivy.lang import Builder
from kivy.app import App

root = Builder.load_file('box.kv')


class TestApp_1(App):
    def build(self):
        return root

if __name__ == "__main__":
    TestApp_1().run()
