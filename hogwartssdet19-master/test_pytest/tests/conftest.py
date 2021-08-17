import threading
import time

import pytest


@pytest.fixture()
def get_unique_name():
    # 获取时间戳
    tag_name = str(time.time()) + threading.currentThread().name
    return tag_name
