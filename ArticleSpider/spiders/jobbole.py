# -*- coding: utf-8 -*-
import re
import scrapy


class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章并交给解析函数执行具体字段的解析
        2. 获取下一页的url并交给w
        """

        # re_selector1 = response.xpath("/html/body/div[1]/div[3]/div[1]/div[1]/h1")
        # re_selector2 = response.xpath('//*[@id="post-110595"]/div[1]/h1/text()')
        # re_selector3 = response.xpath("//div[@class='entry-header']/h1/text()")
        title  = response.xpath("//div[@class='entry-header']/h1/text()").extract()[0]
        create_date = response.xpath("//p[@class='entry-meta-hide-on-mobile']/text()").extract()[0].strip().replace("·","").strip()
        praise_nums = response.xpath("//span[contains(@class, 'vote-post-up')]//h10/text()").extract()[0]
        fav_nums = response.xpath("//span[contains(@class, 'bookmark-btn')]/text()").extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)
        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)

        content = response.xpath("//div[@class='entry']").extract()[0]
        tag_list = response.xpath("//p[@class='entry-meta-hide-on-mobile']/a/text()").extract()
        tag_list = [ element for element in tag_list if not element.strip().endswith("评论") ]
        tags = ",".join(tag_list)


        # 通过css选择器提取字段
        title = response.css(".entry-header h1::text").extract()[0]
        create_date = response.css(".entry-meta-hide-on-mobile::text").extract()[0].strip().replace("·","").strip()
        praise_nums = response.css("div.post-adds h10::text").extract()[0]

        # fav_nums = response.css("span[class*='bookmark-btn']::text").extract()[0]
        fav_nums = response.css(".bookmark-btn::text").extract()[0]
        match_re = re.match(".*?(\d+).*", fav_nums)
        if match_re:
            fav_nums = match_re.group(1)

        # comment_nums = response.css("span[class='btn-bluet-bigger href-style hide-on-480']::text").extract()[0]
        comment_nums = response.css("a[href='#article-comment'] span::text").extract_first()
        match_re = re.match(".*?(\d+).*", comment_nums)
        if match_re:
            comment_nums = match_re.group(1)
        content = response.css(".entry").extract()[0]
        tag_list = response.css("p.entry-meta-hide-on-mobile a::text").extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tags = ",".join(tag_list)
        pass
