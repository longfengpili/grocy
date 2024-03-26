# -*- coding: utf-8 -*-
# @Author: longfengpili
# @Date:   2024-03-08 10:28:55
# @Last Modified by:   longfengpili
# @Last Modified time: 2024-03-25 14:56:48
# @github: https://github.com/longfengpili

import os
import sys

import colorlog
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

LOG_BASE_PATH = os.path.expanduser('~')  # 可以user目录下查看日志

LOGGING_CONFIG = {
    'version': 1,  # 保留字
    'disable_existing_loggers': False,  # 禁用已经存在的logger实例
    # 日志文件的格式
    'formatters': {
        # 详细的日志格式
        'standard': {
            'format': '%(asctime)s.%(msecs)03d - %(threadName)s:%(thread)d - %(name)s - %(levelname)s - %(pathname)s - %(lineno)d - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        # 简单的日志格式
        'simple': {
            'format': '%(asctime)s.%(msecs)03d - %(threadName)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        # 定义一个特殊的日志格式
        'collect': {
            'format': '%(message)s'
        },
        # color
        'color': {
            '()': colorlog.ColoredFormatter,
            'format': '%(asctime)s.%(msecs)03d - %(threadName)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)d - %(log_color)s%(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'log_colors': {
                'CRITICAL': 'bold_red',
                'ERROR': 'red',
                'WARNING': 'purple',
                'INFO': 'green',
                'DEBUG': 'yellow'
            }
        },
    },
    # 过滤器
    'filters': {
    },
    # 处理器
    'handlers': {
        # 在终端打印
        'console': {
            'level': 'DEBUG',
            'filters': [],
            'class': 'logging.StreamHandler',  #
            'formatter': 'color' if sys.stdout.isatty() or any("ipython" in arg for arg in sys.argv) else 'simple'
        },
        # 默认的
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',  # 能够判断创建日持文件
            'filename': os.path.join(LOG_BASE_PATH, 'default.log'),  # 日志文件
            'when': 'd',  # 每天备份
            'interval': 1,
            'backupCount': 30,  # 最多备份几个
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['console', 'default'],
            'level': 'INFO',
            'propagate': True,  # 向不向更高级别的logger传递
        },
    },
}


import logging.config  # noqa: E402
logging.config.dictConfig(LOGGING_CONFIG)
