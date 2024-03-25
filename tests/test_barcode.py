# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-15 11:51:46
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-20 13:52:44
# @github: https://github.com/longfengpili


from products.barcode.barcode import BarCode


class TestRequest:

    def setup_method(self, method):
        self.bcapi = BarCode()

    def teardown_method(self, method):
        pass

    def test_get_product_barcode(self):
        res = self.bcapi.get_pinfo(code='6972205226407')
        print(res)
