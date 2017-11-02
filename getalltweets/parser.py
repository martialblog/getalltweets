#!/usr/bin/env python3

"""
Parses the HTML Response from the Twitter Search page
"""

from pyquery import PyQuery


class TweetParser:
    """
    Parses the HTML Response from the Twitter Search page
    """

    @staticmethod
    def create_dict(tweet):
        """
        Formats a PyQuery parsed tweet into a Twitter API like dict
        """

        return {
            'created_at': int(tweet("small.time span.js-short-timestamp").attr("data-time")),
            'id': tweet.attr("data-tweet-id"),
            'lang': tweet("div.js-tweet-text-container p").attr("lang"),
            'text': tweet("p.js-tweet-text").text(),
            'user': {
                'id': tweet("div.stream-item-header a").attr("data-user-id"),
                'screen_name': tweet("span:first.username.u-dir b").text()
            },
        }

    @staticmethod
    def parse(html=None):
        """
        Parses the HTML response from Twitter into a list of tweets

        :param html: String of HTML data
        """

        final_tweets = []

        try:
            tweets_parsed = PyQuery(html['items_html'])('div.js-stream-tweet')
            has_tweets = len(tweets_parsed) > 0
        except Exception as exception:
            print('Failed to open parse HTML')
            print(exception)

            return final_tweets

        if not has_tweets:
            return final_tweets

        for tweet in tweets_parsed('div.js-stream-tweet'):
            tweet_parsed = PyQuery(tweet)
            tweet_dict = TweetParser.create_dict(tweet_parsed)
            final_tweets.append(tweet_dict)

        return final_tweets
