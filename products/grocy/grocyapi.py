# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-15 11:21:28
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-25 15:04:02
# @github: https://github.com/longfengpili

from products.utils.brequests import BaseAPI

import logging
glogger = logging.getLogger(__name__)


class GrocyAPI(BaseAPI):

    def __init__(self, apikey: str):
        self.apikey = apikey

    @property
    def baseurl(self):
        baseurl = 'http://longfengpili.cn:39283/api'
        return baseurl

    @property
    def urlpaths(self):
        urlpaths = {
            'barcode': 'objects/product_barcodes?query[]=product_id=',
            'product': 'objects/products/'
        }
        return urlpaths

    @property
    def headers(self):
        headers = {
            'GROCY-API-KEY': self.apikey,
            "accept": "*/*",
            "Content-Type": "application/json",
        }
        return headers

    def get_url(self, apiname: str, pid: str = None):
        apipath = self.urlpaths.get(apiname)
        url = f"{self.baseurl}/{apipath}{pid}" if pid else f"{self.baseurl}/{apipath[:-1]}"
        return url

    def get_pinfo(self, apiname: str, pid: str = None):
        url = self.get_url(apiname, pid)
        res = self.request_api(url, method='get')
        return res

    def update_pinfo(self, pid: str, name: str, desc: str = None, **kwargs):
        url = self.get_url('product', pid)
        res = self.request_api(url, method='put', name=name, description=desc, **kwargs)
        ulog = f"update product: {pid}, name update to [{name}], description update to [{desc}], other {kwargs}"
        reslog = f'{ulog}, response: {res}' if res else f'{ulog}'
        glogger.info(reslog)
        return res
