import unittest
import os
from htmltestreport import HTMLTestReport
from tpsh_test_mode1.config import DIR_PATH

suite = unittest.defaultTestLoader.discover("./script")
file_path = DIR_PATH + os.sep + "report" + os.sep + "tpshop_auto.html"
HTMLTestReport(file_path).run(suite)