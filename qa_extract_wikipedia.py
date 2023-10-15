
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

from __future__ import print_function

import os
import sys
import codecs
import time
import json
import logging
import re
import regex
import datetime

from optparse import OptionParser
from nltools  import misc

from xml.sax import make_parser, handler
from bz2file import BZ2File

PROC_TITLE        = 'qa_extract_wikipedia'

WIKIXML           = {
                      'en': '/home/bofh/projects/ai/data/corpora/en/enwiki-20181220-pages-articles-multistream.xml.bz2',
                      'de': '/home/bofh/projects/ai/data/corpora/de/dewiki-latest-pages-articles-multistream.xml.bz2'
                    }

DEFAULT_LANG      = 'en'

QASRC_DIRFN       = 'data/qa_src'