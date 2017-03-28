# -*- coding:utf-8 -*-
__author__ = "Tim"
import hashlib


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")

    # hashlib 中有个方法叫 md5()
    m = hashlib.md5()
    m.update(url)
    # 抽取 m 的摘要
    return m.hexdigest()


if __name__ == "__main__":
    print (get_md5("http://jobbole.com"))