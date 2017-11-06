#!/usr/bin/env python3


import pytest

# Package Imports
import getalltweets.criteria as tc


def test_tweetcriteria():
    """
    Default Instance
    """

    tweet_crit = tc.TweetCriteria()

    assert(tweet_crit.language is None)
    assert(tweet_crit.query is None)
    assert(tweet_crit.username is None)
    assert(tweet_crit.number_of_tweets == 0)

def test_tweetcriteria_arguments():
    """
    Default Instance
    """

    tweet_crit = tc.TweetCriteria(
        username='zweipunknull',
        query='foo bar',
        number_of_tweets=42,
        language='de'
    )

    assert(tweet_crit.language == 'de' )
    assert(tweet_crit.query == 'foo bar')
    assert(tweet_crit.username == 'zweipunknull')
    assert(tweet_crit.number_of_tweets == 42)
