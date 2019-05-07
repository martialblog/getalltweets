#!/usr/bin/env python3

"""
Handles the HTTP Requests to the Twitter Search Query
"""

from sys import stderr
from urllib import request, parse, error
from json import loads


class TweetScraper:
    """
    Handles the HTTP Requests to the Twitter Search Query
    """

    def __init__(self):
        """
        Just setting up the Twitter Search URL
        """

        self.baseurl = 'https://twitter.com/i/search/timeline'
        self.query = '?f=tweets&q={}&src=typd&{}max_position={}'
        self.url = self.baseurl + self.query

    def build_url(self, criteria, cursor):
        """
        Builds the final URL for the HTTP Request.

        :param TweetCriteria: Criteria Object for Tweets
        :param cursor: Position of cursor to navigate Twitter API
        :return: Full Twitter URL with criteria as query
        :rtype: str
        """

        url_data = ''
        url_language = ''

        if criteria.username:
            url_data += ' from:' + criteria.username

        if criteria.query:
            url_data += ' ' + criteria.query

        if criteria.language:
            url_language = 'lang=' + criteria.language + '&'

        url = self.url.format(parse.quote(url_data), url_language, cursor)

        return url

    @staticmethod
    def build_headers(url):
        """
        Builds the HTTP Headers for the Request

        :param url: Full Twitter URL with criteria as query
        :return: HTTP Headers for HTTP Request
        :rtype: list
        """

        return [
            ('Host', "twitter.com"),
            ('User-Agent', "Mozilla/5.0 (Windows NT 6.1; Win64; x64)"),
            ('Accept', "application/json, text/javascript, */*; q=0.01"),
            ('Accept-Language', "de,en-US;q=0.7,en;q=0.3"),
            ('X-Requested-With', "XMLHttpRequest"),
            ('Referer', url),
            ('Connection', "keep-alive")
        ]

    def scrap(self, criteria, cursor, cookiejar):
        """
        Call Twitter API with search query and return JSON response.
        This response contains the HTML of the Twitter Search Page

        :param TweetCriteria: Criteria Object for Tweets
        :param cursor: Position of cursor to navigate Twitter API
        :param cookiejar: Cookie Handling with http.cookiejar
        :return: JSON Object containing the reponse from Twitter
        :rtype: json

        Example response:
        {
         'min_position': "Cursor Position",
         'items_html': "HTML of Search Page",
         'has_more_items': "Boolean"
        }
        """

        url = self.build_url(criteria, cursor)
        headers = self.build_headers(url)

        opener = request.build_opener(request.HTTPCookieProcessor(cookiejar))
        opener.addheaders = headers

        try:
            response = opener.open(url)
            json_response = response.read()
        except error.HTTPError as exception:
            print('Failed to open {}'.format(self.baseurl), file=stderr)
            print(exception, file=stderr)

            return None

        return loads(json_response.decode())
