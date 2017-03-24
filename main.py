# -*- coding:utf-8 -*-
__author__ = "Tim"

from scrapy.cmdline import execute

import sys
import os

# 设置工程的目录，可以在任何路径下运行execute
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

execute(["scrapy", "crawl", "jobbole"])

"""
# 获取当前 main 文件的路径
print (os.path.abspath(__file__))

# 获取当前 main 文化所在路径
print (os.path.dirname(os.path.abspath(__file__)))

"""
