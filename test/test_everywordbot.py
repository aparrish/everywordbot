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


class TwitterStub(object):
    def __init__(self):
        self.status = None
        self.lat = None
        self.long = None
        self.place_id = None

    def twitter_update_status(self, status, lat=None, long=None,
                              place_id=None):
        self.status = status
        self.lat = lat
        self.long = long
        self.place_id = place_id


class TestIt(unittest.TestCase):

    def test__get_current_line(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "test/test_source.txt", "index_file")
        index = 1

        # Act
        line = bot._get_current_line(index)

        # Assert
        self.assertEqual(line, "word2")

    def test__get_current_index_file_not_exist(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "_source_file", "no_index_file")

        # Act
        index = bot._get_current_index()

        # Assert
        self.assertEqual(index, 0)

    def test__increment_index(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "_source_file", "test/test_index.txt")

        # Act
        bot._increment_index(0)

        # Assert
        index = bot._get_current_index()
        self.assertEqual(index, 1)

    def test__post(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "test/test_source.txt", "test/test_index.txt")
        stub = TwitterStub()
        bot.twitter.update_status = stub.twitter_update_status
        index_before = bot._get_current_index()

        # Act
        bot.post()

        # Assert
        index_after = bot._get_current_index()
        self.assertEqual(index_before + 1, index_after)

    def test__prefix(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "test/test_source.txt", "index_file",
                           prefix="aardvark ")
        bot._get_current_line = lambda index: "word"
        stub = TwitterStub()
        bot.twitter.update_status = stub.twitter_update_status

        # Act
        bot.post()

        # Assert
        self.assertEqual(stub.status, "aardvark word")

    def test__suffix(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "test/test_source.txt", "index_file",
                           suffix=" zebra")
        bot._get_current_line = lambda index: "word"
        stub = TwitterStub()
        bot.twitter.update_status = stub.twitter_update_status

        # Act
        bot.post()

        # Assert
        self.assertEqual(stub.status, "word zebra")

    def test__prefix_and_suffix(self):
        # Arrange
        bot = EverywordBot("consumer_key", "consumer_secret",
                           "access_token", "token_secret",
                           "test/test_source.txt", "index_file",
                           prefix="apple-", suffix="-zucchini")
        bot._get_current_line = lambda index: "word"
        stub = TwitterStub()
        bot.twitter.update_status = stub.twitter_update_status

        # Act
        bot.post()

        # Assert
        self.assertEqual(stub.status, "apple-word-zucchini")


if __name__ == '__main__':
    unittest.main()

# End of file
