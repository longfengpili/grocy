# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-20 11:23:28
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-05-14 15:13:55
# @github: https://github.com/longfengpili

import os
from datetime import datetime

from products.grocy.grocyapi import GrocyAPI
from products.barcode.barcode import BarCode

import logging
mlogger = logging.getLogger(__name__)

APIKEY = os.getenv("GAPIKEY")


def get_pinfo_by_code(code: str):
    today = datetime.today()
    today = today.strftime('%Y-%m-%d')

    bcapi = BarCode()
    pinfo = bcapi.get_pinfo(code=code)
    brandcn, gpcname, desc, special = pinfo.get('brandcn'), pinfo.get('gpcname'), pinfo.get('description'), pinfo.get('specification')
    name = f"[{brandcn}]{desc}" if brandcn else None
    desc = f"{gpcname}, {special}, update: {today}" if gpcname else None
    picname = pinfo.get('picname')
    return name, desc, picname


def get_grocy_products():
    gapi = GrocyAPI(apikey=APIKEY)
    products = gapi.get_pinfo(apiname='product')
    return products


def get_grocy_barcode(pid: str):
    gapi = GrocyAPI(apikey=APIKEY)
    items = gapi.get_pinfo(apiname='barcode', pid=pid)
    item = items[0]
    barcode = item.get('barcode')
    return barcode


def update_grocy(pid: str, name: str, desc: str = None, **kwargs):
    gapi = GrocyAPI(apikey=APIKEY)
    gapi.update_pinfo(pid, name, desc, **kwargs)


def update_products(products: list):
    for product in products:
        pid, desc = product.get('id'), product.get('description')
        if not desc or 'update' not in desc:
            mlogger.info(product)
            barcode = get_grocy_barcode(pid)
            name, desc, picname = get_pinfo_by_code(barcode)
            if name:
                update_grocy(pid, name, desc, picture_file_name=picname)


if __name__ == '__main__':
    products = get_grocy_products()
    update_products(products)
