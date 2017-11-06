#!/usr/bin/env python3

"""
Criteria to build Query for Twitter Search
"""

class TweetCriteria:
    """
    Criteria to build Query for Twitter Search
    """

    def __init__(self, language=None, number_of_tweets=0, query=None, username=None):

        self.language = language
        self.number_of_tweets = int(number_of_tweets)
        self.query = query
        self.username = username
