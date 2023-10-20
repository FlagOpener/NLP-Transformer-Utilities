
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Copyright 2019 Guenter Bartsch
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#

import os
import sys
import codecs
import time
import json
import logging
import bz2
import requests
import collections

from datetime import datetime
from pyquery  import PyQuery
from optparse import OptionParser
from nltools  import misc
from multiprocessing import Pool

PROC_TITLE        = 'twitterscrape'

TWITTER_CORPUSDIR = '/home/bofh/projects/ai/data/corpora/en/twitter'
DEFAULT_USER_STATS= '/home/bofh/projects/ai/data/corpora/en/twitter/user_stats.json'

DEFAULT_MAX_TWEETS = 0
DEFAULT_LANG       = 'en'
DEFAULT_QUERY      = ''
DEFAULT_SINCE      = ''
DEFAULT_UNTIL      = ''
DEFAULT_NEAR       = ''
DEFAULT_WITHIN     = ''

MAX_DUPES          = 64

NUM_PROCS          = 32

#
# init
#

misc.init_app(PROC_TITLE)

#
# commandline
#

parser = OptionParser("usage: %prog [options] corpus twitter_sources.txt")

parser.add_option ("-m", "--max_tweets", dest="max_tweets", type = "int", default=DEFAULT_MAX_TWEETS,
                   help="maximum number of tweets to scrape, default: %d" % DEFAULT_MAX_TWEETS)

parser.add_option ("-l", "--lang", dest="lang", type = "str", default=DEFAULT_LANG,
                   help="language, default: %s" % DEFAULT_LANG)

parser.add_option ("-n", "--near", dest="near", type = "str", default=DEFAULT_NEAR,
                   help="search tweets near location, default: none")

parser.add_option ("-w", "--within", dest="within", type = "str", default=DEFAULT_WITHIN,
                   help="search tweets within this distance of near location, default: none")

parser.add_option ("-q", "--query", dest="query", type = "str", default=DEFAULT_QUERY,
                   help="search query, default: none")

parser.add_option ("-s", "--since", dest="since", type = "str", default=DEFAULT_SINCE,
                   help="search for tweets since, default: no limit")

parser.add_option ("-u", "--until", dest="until", type = "str", default=DEFAULT_UNTIL,
                   help="search for tweets until, default: no limit")

parser.add_option ("-U", "--user-stats", dest="user_stats", type = "str", default=DEFAULT_USER_STATS,
                   help="user stats file, default: %s" % DEFAULT_USER_STATS)

parser.add_option ("-v", "--verbose", action="store_true", dest="verbose",
                   help="verbose output")

(options, args) = parser.parse_args()

if options.verbose:
    logging.getLogger().setLevel(logging.DEBUG)
else:
    logging.getLogger().setLevel(logging.INFO)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

if len(args) != 2:
    parser.print_usage()
    sys.exit(1)

corpus_name     = args[0]
twitter_sources = args[1]
user_stat_fn    = options.user_stats

#
# corpus preparation
#

dirfn = '%s/%s' % (TWITTER_CORPUSDIR, corpus_name)
misc.mkdirs(dirfn)

user_stats = {}

try:
    with open(user_stat_fn, 'r') as user_stat_f:
        user_stats = json.loads(user_stat_f.read())
except:
    pass

#
# twitter scraping
#

def scrapeStatusPage(cursor, sess, lang='en', search_user='', search_query='', search_since='', search_until='', search_near='', search_within=''):

    logging.debug('scrapeStatusPage, user=%s, query=%s, since=%s, until=%s, cursor=%s' % (search_user, search_query, search_since, search_until, cursor))

    parUrl = ''
    if not search_user and not search_query:
        raise ValueError("User and Query, at least one of them must be specified.")
    else:
        if search_query:
            parUrl += " " + search_query
        if search_user:
            parUrl += ' from:' + search_user
        if search_until:
            parUrl += ' until:' + search_until
        if search_since:
            parUrl += ' since:' + search_since
        if search_near:
            if search_within:
                parUrl += " near:\"" + search_near + "\" within:" + search_within

    # logging.debug(parUrl)
    # logging.debug(cursor)

    # english
    headers_en = {
        'User-Agent': 'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
        'Accept-Language': "en-CA,en;q=0.8",
        'X-Requested-With': "XMLHttpRequest"
    }

    # french
    headers_fr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Language': "fr-CA,fr;q=0.8",
        'X-Requested-With': "XMLHttpRequest"
    }

    # german
    headers_de = {
        'User-Agent': 'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
        # 'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
        'Accept-Language': "de",
        'X-Requested-With': "XMLHttpRequest"
    }

    # english
    url_en = "https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&l=en&max_position=%s"

    # french
    url_fr = u"https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&l=fr&max_position=%s"

    # german
    url_de = u"https://twitter.com/i/search/timeline?f=tweets&q=%s&src=typd&l=de&max_position=%s"

    if lang == 'fr':
        url = url_fr
        headers = headers_fr
    elif lang == 'de':
        url = url_de 
        headers = headers_de
    else:
        url = url_en
        headers = headers_en

    url = url % (parUrl, cursor)

    logging.debug('scrapeStatusPage: url=%s' % url) 

    try:
        # print unicode(url)
        r = sess.get(url, headers=headers)
        # print r.url
        # print 'TEXT: -------------------------'
        # print r.text
        # print 'JSON: -------------------------'
        # print r.json()
        # print '-------------------------\n\n\n'
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error(u'ERROR while ripping %s: %s' % (url, e))

def scrapeCommentPage(user_name, tweet_id, cursor, sess, lang='en'):

    url = "https://twitter.com/i/%s/conversation/%s?include_available_features=1&include_entities=1&max_position=%s&reset_error_state=false"
    url = url % (user_name, tweet_id, cursor)
    # english
    headers_en = {
        'User-Agent': 'Opera/12.0(Windows NT 5.1;U;en)Presto/22.9.168 Version/12.00',
        'Accept-Language': "en-CA,en;q=0.8",
        'X-Requested-With': "XMLHttpRequest"
    }

    # french
    headers_fr = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept-Language': "fr-CA,fr;q=0.8",
        'X-Requested-With': "XMLHttpRequest"
    }

    if lang == 'fr':
        headers = headers_fr
    else:
        headers = headers_en

    try:
        r = sess.get(url, headers=headers)
        return r.json()
    except requests.exceptions.RequestException as e:
        logging.error( 'UNEXPECTED EXCEPTION in scapeCommentPage: url=%s : %s' % ( url, e))

def scrapeComments(user_name, tweet_id, cnt_replies, session, max_comments=0):
    cnt_c = 0
    cursor = ''
    total = 0
    has_more = True
    comments = []
    lim = cnt_replies
    if max_comments and lim >max_comments:
        lim = max_comments
    while has_more is True and total < lim:
        page = scrapeCommentPage(user_name, tweet_id, cursor, session)
        cnt_cp, has_more, cursor, pageTweets = scrapePage(page, session, isComment=True)
        if len(pageTweets) == 0:
            logging.debug('Weird, no comments!')
            break
        comments.extend(pageTweets)
        total += len(pageTweets)
        cnt_c += cnt_cp
    # cnt_c should be 0
    return cnt_c, comments

def scrapeTweet(tweetq, session, isComment=False):

    global user_stats

    """
    "" Read the document, and parse it with PyQuery
    """