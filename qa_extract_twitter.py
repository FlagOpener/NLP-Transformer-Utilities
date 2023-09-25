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
import hashlib
import tqdm
import random

import newspaper
from newspaper       import Article
from multiprocessing import Pool
from optparse        import OptionParser
from nltools         import misc

PROC_TITLE        = 'qa_extract_twitter'

TWITTER_CORPUSDIR = '/home/bofh/projects/ai/data/corpora/en/twitter'

QASRC_DIRFN       = 'data/qa_src'

# DEBUG_LIMIT       = 10
DEBUG_LIMIT       = 0

BLOCKLIST         = ['wapo.st', 'washingtonpost.com', 'twitter.com', 'tagesspiegel.de']

NUM_PROCS         = 32

USER_AGENTS = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
               'Mozilla/5.0 (Linux; Android 8.0.0; SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.372