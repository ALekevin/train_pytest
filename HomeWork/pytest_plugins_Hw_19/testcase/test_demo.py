
import pytest

# from HomeWork.pytest_plugins_Hw_19.testcase.conftest import logger
from pytest_encode_logger import logger



class TestDemo:
    @pytest.mark.parametrize('a',['a'])
    def test_1(self,a):
        logger.info('info')
        logger.info('开始执行用例')
        print(a)