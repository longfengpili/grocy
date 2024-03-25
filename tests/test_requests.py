# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-08 16:10:00
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-25 14:47:59
# @github: https://github.com/longfengpili


from products.utils.brequests import BaseAPI


class TestRequest:

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_get_product_barcodes(self):
        url = 'https://www.baidu.com'
        bapi = BaseAPI()
        res = bapi.request_api(url)
        print(res[:100])
