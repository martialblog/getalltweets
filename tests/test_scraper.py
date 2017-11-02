#!/usr/bin/env python3


import pytest
import unittest.mock as mock

# Package Imports
import getalltweets.scraper as ts
import getalltweets.criteria as tc


def test_tweetscraper():
    """
    Default Instance
    """

    tweet_scrap = ts.TweetScraper()

    exp_baseurl = 'https://twitter.com/i/search/timeline'
    exp_query = '?f=tweets&q={}&src=typd&{}max_position={}'
    exp_url = exp_baseurl + exp_query

    assert(tweet_scrap.baseurl == exp_baseurl )
    assert(tweet_scrap.query == exp_query )
    assert(tweet_scrap.url == exp_url )

def test_tweetscraper_build_url():
    """
    Build URL Function
    """

    tweet_crit = tc.TweetCriteria()
    tweet_scrap = ts.TweetScraper()

    # TODO: Make this a shared resource
    exp_baseurl = 'https://twitter.com/i/search/timeline'
    exp_query = '?f=tweets&q={}&src=typd&{}max_position={}'.format('QUERY', 'TYPD', 'POS')
    exp_url = exp_baseurl + exp_query

    assert(True)

def test_tweetscraper_build_headers():
    """
    Build Headers Function
    """

    exp_headers = [ ('Host', "twitter.com"),
            ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', 'THE_URL'),
            ('Connection', "keep-alive") ]

    tweet_scrap = ts.TweetScraper()
    act_headers = tweet_scrap.build_headers('THE_URL')

    assert(exp_headers == act_headers)

@mock.patch('urllib.request')
def test_tweetscraper_scrap(mock_request):
    """
    Scrap Function
    """

    tweet_scrap = ts.TweetScraper()
