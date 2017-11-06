#!/usr/bin/env python3


import os
import pickle
import pytest
import pyquery
import lxml

# Package Imports
import getalltweets.parser as tp

@pytest.fixture
def response():
    """
    Example Twitter Response
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'response.pickle')

    with open(file_path, 'rb') as response_file:
        resp = pickle.load(response_file)

    return resp

@pytest.fixture
def failed_response():
    """
    Example Twitter Response
    """

    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, 'fail.pickle')

    with open(file_path, 'rb') as response_file:
        resp = pickle.load(response_file)

    return resp

def test_tweetcriteria_parse_typecheck(response):
    """
    Test that parse type is OK and all tweets are returned
    """

    parser = tp.TweetParser()

    actual_parse = parser.parse(response)

    assert(len(actual_parse) == 20)
    assert(isinstance(actual_parse, list))
    assert(isinstance(actual_parse[0], dict))

def test_tweetcriteria_dict(response):
    """
    Test format of parse
    """

    parser = tp.TweetParser()

    tweets = pyquery.PyQuery(response['items_html'])('div.js-stream-tweet')
    tweet_pyquery = pyquery.PyQuery(tweets[0])

    tweet_dict = parser.create_dict(tweet_pyquery)

    # TODO: Why is the lang 'und' ?
    excpected_dict = {'created_at': 1496385758,
                      'text': 'https:// youtu.be/XAi3VTSdTxU @ realDonaldTrump',
                      'lang': 'und',
                      'user': {'screen_name': 'zweipunknull', 'id': '704036908297543686'},
                      'id': '870531084437606402'}

    assert(excpected_dict == tweet_dict)

def test_tweetcriteria_empty(failed_response):
    """
    Test format of parse
    """

    parser = tp.TweetParser()
    actual_parse = parser.parse(failed_response)

    assert(actual_parse == [])

def test_tweetcriteria_exception(capsys):
    """
    Test what happens when pyquery fails to parse
    """

    parser = tp.TweetParser()

    actual_parse = parser.parse('')
    assert(actual_parse == [])
