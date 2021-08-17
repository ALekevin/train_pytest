#-*-coding:GBK -*-
import logging
import os
from datetime import datetime

from typing import List

import pytest


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    '''
    ��дhook���������ռ��������������Ʊ����ʽ���ó�֧�����ĸ�ʽ
    :param session:
    :param config:
    :param items:
    :return:
    '''
    for item in items:
        # ������
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        # ������·��
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


class plugins_logger:
    _all_log_level = ['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG', 'NOTSET']
    _logger_level = "INFO"

    def __init__(self):
        self.logger = logging.getLogger()

    def create(self):
        # logger�ȼ���д
        logger_level = self._logger_level.upper()
        # ���logger�ȼ����ڵȼ����÷�Χ���׳�ValueError�쳣
        if logger_level not in self._all_log_level:
            raise ValueError(f"_logger_level is not in range: {self._all_log_level}")
        # ������־�ȼ�
        self.logger.setLevel(logger_level)
        # ������־�ļ�����·���������ʽ
        f_file = logging.FileHandler(os.path.join(self.set_log_dir(), f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"), encoding='UTF-8')
        # ������־�����
        f_stream = logging.StreamHandler()
        # ��ȡ��־��ʽ
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s : %(message)s')
        f_file.setFormatter(formatter)
        f_stream.setFormatter(formatter)
        # ���handler
        self.logger.addHandler(f_file)
        self.logger.addHandler(f_stream)
        return self.logger

    def set_log_dir(self):
        #��ȡ��ǰ·��
        current_path = os.getcwd()
        #��ȡlog�ļ��洢�ļ���·��
        log_path = os.path.join(current_path, 'logs', str(datetime.now().date()))
        #�ж��Ƿ�����ļ��У��������ڴ����ļ���
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        return log_path


logger = plugins_logger().create()


