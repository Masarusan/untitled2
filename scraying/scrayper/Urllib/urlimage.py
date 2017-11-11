# -*- coding: utf-8 -*-

from PIL import Image
import io
from urllib.request import urlopen

file =io.BytesIO(urlopen('http://xxeronetxx.info/img/20170906/m-83fd3fe45c96187853f19d960d61b0fbcec15dad.jpg').read())
img = Image.open(file)
img.show()