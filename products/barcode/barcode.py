# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-19 11:35:27
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-20 21:26:31
# @github: https://github.com/longfengpili


from fake_useragent import UserAgent

from products.utils.brequests import BaseAPI

import logging
bclogger = logging.getLogger(__name__)


class BarCode(BaseAPI):

    def __init__(self, pagesize: int = 30, pageindex: int = 1):
        self.pagesize = pagesize
        self.pageindex = pageindex

    @property
    def baseurl(self):
        baseurl = 'https://bff.gds.org.cn/gds/searching-api/ProductService/homepagestatistic'
        return baseurl

    @property
    def searchurl(self):
        searchurl = 'https://bff.gds.org.cn/gds/searching-api/ProductService/ProductListByGTIN'
        return searchurl

    @property
    def ua(self):
        ua = UserAgent() 
        return ua.random

    @property
    def headers(self):
        headers = {
            'Referer': 'http://www.gds.org.cn/',
            'User-Agent': self.ua,
        }
        return headers

    def get_url(self, code: str):
        url = f"{self.searchurl}?PageSize={self.pagesize}&PageIndex={self.pageindex}&SearchItem=0{code}"
        return url

    def get_pinfo(self, code: str):
        url = self.get_url(code)
        res = self.request_api(url, method='get')

        if isinstance(res, str):
            res = self.request_api(self.baseurl, method='get')
            res = self.request_api(url, method='get')

        if isinstance(res, dict):
            code, msg = res.get('Code'), res.get('Msg')
            if code == 2:
                bclogger.error(f"{url}, {msg}")

        pinfo = res['Data']['Items'][0] if 'Data' in res else {}

        if pinfo:
            picname = self.download_pic(pinfo)
            pinfo['picname'] = picname

        return pinfo

    def download_pic(self, pinfo: dict):
        gtin, picpath = pinfo.get('gtin'), pinfo.get('picture_filename')
        if not picpath:
            bclogger.error(f"No pic, {pinfo.get('keyword')}")
            return '000000000.jpg'

        picurl = f'https://oss.gds.org.cn/{picpath}'
        result = self.request_api(picurl, method='get', restype='content')
        picname = f"{gtin}.jpg"
        picpath = f"./productpictures/{picname}"
        with open(picpath, 'wb') as f:
            f.write(result)
        return picname
