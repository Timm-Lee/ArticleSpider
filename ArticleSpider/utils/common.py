# -*- coding:utf-8 -*-
__author__ = "Tim"
import hashlib


def get_md(url):
    if isinstance(url, str):
        url = url.encode("utf-8")

    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ == "__main__":
    print (get_md("http://jobbole.com"))