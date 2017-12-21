# -*- coding: utf-8 -*-
#!/usr/bin/python3

import tkinter as tk
from scrape_01 import Scrape


class scraype_gui(Scrape):

    def __init__(self):
        super(scraype_gui, self).__init__(url=['https://momon-ga.com/archives/60552468.html'])

    def main(self):
        root = tk.Tk()
        text = tk.Text(root, height=10, width=40)
        text.pack(side=tk.LEFT, fill=tk.Y)
        scroll = tk.Scrollbar(root)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)
        for i in super().get_link():
            text.insert(tk.END, i)

        root.mainloop()


if __name__ == "__main__":
    gui = scraype_gui()
    gui.main()