#!/usr/bin/env python
# encoding: utf-8
"""
Unit tests for everywordbot.py
"""
from __future__ import print_function, unicode_literals
import os.path
import unittest
import sys
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from everywordbot import EverywordBot


class TestIt(unittest.TestCase):

    def test_3sentiljoonaa(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "test/test_source.txt", "index_file")
        index = 1

        # Act
        line = bot._get_current_line(index)

        # Assert
        self.assertEqual(line, "word2")


if __name__ == '__main__':
    unittest.main()

# End of file
