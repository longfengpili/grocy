# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-15 11:51:46
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-25 14:59:09
# @github: https://github.com/longfengpili

import os
from products.grocy.grocyapi import GrocyAPI


class TestGAPI:

    def setup_method(self, method):
        self.apikey = os.getenv("GAPIKEY")
        self.gapi = GrocyAPI(apikey=self.apikey)

    def teardown_method(self, method):
        pass

    def test_get_product_barcode(self):
        res = self.gapi.get_pinfo(apiname='barcode', pid='2')
        print(res)

    def test_get_product(self):
        res = self.gapi.get_pinfo(apiname='product', pid='2')
        print(res)

    def test_update_pinfo(self):
        res = self.gapi.update_pinfo(pid='2', name='test', desc='测试')
        print(res)
