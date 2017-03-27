# -*- coding: utf-8 -*-
import codecs
import json

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter

import MySQLdb
# import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(lines)
        return item
    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipeline(object):
    # 调用Scrapy提供的JsonExporter导出Json文件。
    def __init__(self):
        self.file = open('article_exporter.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding="utf-8", ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MysqlPipeline(object):
    def __init__(self):
        # self.conn = pymysql.connect(host='localhost', port=3306,
        #                             user='root', password='',
        #                             db='article_spider',
        #                             charset='utf8')

        self.conn = MySQLdb.connect(host='127.0.0.1', user='root', password='', db='article_spider', charset="utf8", use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):

        # insert_sql = "INSERT IGNORE INTO 'jobbole_artile' ('title', 'url', 'create_date', 'fav_nums') VALUES (%s, %s, %s, %s)"
        insert_sql = """
            insert into jobbole_article(title, url, create_date, fav_nums)
            VALUES (%s, %s, %s, %s)
        """

        self.cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))
        self.conn.commit()


class MysqlTwistedPipeline(object):

    @classmethod
    def from_settings(cls, settings):
        host = settings["MYSQL_HOST"]
        db = settings["MYSQL_DBNAME"]
        user = settings["MYSQL_USER"]
        passwd = settings["MYSQL_PASSWORD"]
        pass




class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value["path"]
            item["front_image_path"] = image_file_path
        return item

