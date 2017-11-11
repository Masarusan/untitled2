# -*- coding: utf-8 -*-
from filecmp import cmp
import os


file = cmp('image/m-0a32677dfa1634d1f07c468c84d57782c503804b.jpg', 'image/m-38e8702150edfc170f45fb1c8dd84765bdd57989.jpg')

print(file)

if __name__ == "__main__":
    pass