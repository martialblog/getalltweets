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
