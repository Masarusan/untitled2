#!/usr/bin/python
# -*- coding: utf-8 -*-

import test
print(test.__name__)

if test.__name__ == "test":
    test.test()
    print('モジュール名：{}'.format(test.__name__))  # 実行したモジュール名を表示する