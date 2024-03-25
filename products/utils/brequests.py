# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2023-07-17 17:12:49
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-25 14:46:44


import json
import requests

import logging
brequestlogger = logging.getLogger(__name__)


class BaseAPI:

    def __init__(self):
        pass

    @property
    def headers(self):
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json",
        }
        return headers

    def request_api(self, url: str, method: str = 'get', retries: int = 3, verify: bool = True, restype: str = 'text', **kwargs):

        def make_request(method: str, url: str, **kwargs):
            if method == 'post':
                res = requests.post(url, headers=self.headers, data=kwargs, verify=verify)
            elif method == 'put':
                res = requests.put(url, headers=self.headers, data=json.dumps(kwargs), verify=verify)
            else:  # Default to 'get'
                res = requests.get(url, headers=self.headers, params=kwargs, verify=verify)

            brequestlogger.debug(f"[{method.upper()}]{res.url}, params: {kwargs}")
            return res

        attempt = 0
        while attempt < retries:
            response = make_request(method, url=url, **kwargs)
            if response.status_code in (200, 204):
                break

            attempt += 1
            brequestlogger.error(f"[{method}] {url}, Attempt {attempt}, status_code: {response.status_code}")

        try:
            result = response.json()
        except Exception as e:
            # brequestlogger.info(e)
            result = response.text if restype == 'text' else response.content
        return result
