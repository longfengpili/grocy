# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-15 12:00:59
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-15 14:05:04
# @github: https://github.com/longfengpili


class GAttr:

    def __init__(self, name: str, value: any = None, **kwargs):
        self.name = name
        self.value = value
        self.kwargs = kwargs

    def __getattr__(self, name: str):
        return self.kwargs.get(name)

    def __getattribute__(self, name: str):
        return super(GAttr, self).__getattribute__(name)

    def __repr__(self):
        return f"{self.name}: {self.value:>5s}"
        

class CodeInfo:











{'id': 1, 'product_id': 1, 'barcode': '6972205226407', 'qu_id': 3, 'amount': 1, 'shopping_location_id': None, 'last_price': None, 'row_created_timestamp': '2024-03-04 13:02:13', 'note': None, 'userfields': None}


{'id': 1, 'name': '111', 'description': None, 'product_group_id': None, 'active': 1, 'location_id': 2, 'shopping_location_id' : None, 'qu_id_purchase': 3, 'qu_id_stock': 3, 'min_stock_amount': 0, 'default_best_before_days': 0, 'default_best_before_days_after_open': 0, 'default_best_before_days_after_freezing': 0, 'default_best_before_days_after_thawing': 0, 'picture_file_name': None, 'enable_tare_weight_handling': 0, 'tare_weight': 0, 'not_check_stock_fulfillment_for_recipes': 0, 'parent_product_id': None, 'calories': 0, 'cumulate_min_stock_amount_of_sub_products': 0, 'due_type': 1, 'quick_consume_amount': 1, 'hide_on_stock_overview': 0, 'default_stock_label_type': 0, 'should_not_be_frozen': 0, 'treat_opened_as_out_of_stock': 1, 'no_own_stock': 0, 'default_consume_location_id': 2, 'move_on_open': 0, 'row_created_timestamp': '2024-03-04 13:01:49', 'qu_id_consume': 3, 'auto_reprint_stock_label': 0, 'quick_open_amount': 1, 'qu_id_price': 3, 'userfields': None}
