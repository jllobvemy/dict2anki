import time
from unittest import TestCase

from dict2anki.utils import *

TAG = get_tag(__name__)

Log.level = Log.DEBUG


class TestUtils(TestCase):
    def test_valid_path(self):
        pass

    def test_Log(self):
        Log.level = Log.INFO
        Log.d(TAG, 'debug log')
        Log.i(TAG, 'info log')
        Log.w(TAG, 'warn log')
        Log.e(TAG, 'error log')
        Log.level = Log.DEBUG
        Log.d(TAG, 'debug log')
        Log.i(TAG, 'info log')
        Log.w(TAG, 'warn log')
        Log.e(TAG, 'error log')

    def test_progress_bar(self):
        bar = ProgressBar()
        bar.update()
        time.sleep(0.5)
        bar.increment(10)
        time.sleep(0.5)
        bar.increment(20)
        time.sleep(0.5)
        bar.extra = 'test extra'
        bar.progress += 69
        time.sleep(0.5)
        bar.increment(1)
        bar.done()
