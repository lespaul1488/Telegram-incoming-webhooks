# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import imgkit
from scrapy.exceptions import NotConfigured
from scrapy.exceptions import DropItem

class DaddyleaguesPipeline(object):


    def close_spider(self, spider):
        self.conn.close()

    def process_item(self, link, spider):
        #config = imgkit.config(wkhtmltoimage='/usr/local/bin/wkhtmltoimage')
        config = imgkit.config(wkhtmltoimage='/usr/bin/wkht
        options = {
            'crop-x': 3450,
            'crop-y': 200,
            'quality': 100,
            'height': 600,
            'width': 4400
        }
        imgkit.from_url(link, 'gameRecap.png', options=options, con

        js = """javascript:
        document.getElementById('gamesummary').className = 'tab-pane';
        document.getElementById('teamstats').className = 'tab-pane active';

        var x = document.getElementsByClassName ('card');
        x[5].style.setProperty('width', '245px');
        x[5].style.setProperty('height', '100px');
        x[5].style.setProperty('left', '45px');
        x[5].parentElement.style.setProperty('flex', '0 0 10%');


        x[6].style.setProperty('width', '245px');
        x[6].style.setProperty('height', '100px');
        x[6].style.setProperty('left', '-275px');
        x[6].parentElement.style.setProperty('flex', '0 0 10%');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[4];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[4];
        d.style.setProperty('display','none');

        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[5];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[5];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[6];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[6];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[7];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[7];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[8];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[8];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[9];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[9];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[10];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[10];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[11];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[11];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[12];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[12];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[13];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[13];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[14];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[14];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[15];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[15];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[18];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[18];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[19];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[19];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[20];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '120px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[20];
        d.style.setProperty('display','none');


        var x = document.getElementsByClassName ('ml-auto col wd-xxs text-right')[21];
        x.style.setProperty('position','absolute');
        x.style.setProperty('left', '350px');
        x.style.setProperty('margin-top', '-30px'); x.firstElementChild.style.setProperty('width', '50px');  x.firstElementChild.style.setProperty('font-size', '30px');
        var d = document.getElementsByClassName ('w-100')[21];
        d.style.setProperty('display','none');


        """
	    options = {
		'crop-x': 80,
        	'crop-y': 300,
        	'quality': 100,
        	'height': 830,
        	'width': 610,
            'run-script': js,
            'javascript-delay': 1000
            }

        imgkit.from_url(link, 'teamStats.png', options=options, config=config)

        url = "https://api.telegram.org//sendPhoto";
        files = {'photo': open('gameRecap.png', 'rb')}
        data = {'chat_id' : self.chat_id}
        requests.post(url, files=files, data=data)
        files = {'photo': open('teamStats.png', 'rb')}
        requests.post(url, files=files, data=data)

    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        return cls(**settings.getdict('TELEGRAM'))
