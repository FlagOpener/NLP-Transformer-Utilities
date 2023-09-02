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
import re
import codecs
import time
import json
import logging
import datetime
import xml.etree.ElementTree as ET

from copy import copy
from optparse import OptionParser
from mako.template import Template


from nltools  import misc

PROC_TITLE        = 'qa_extract_skills'

QASRC_DIRFN       = 'data/qa_src'

# DEBUG_LIMIT       = 10
DEBUG_LIMIT       = 0

#
# init
#

misc.init_app(PROC_TITLE)

#
# commandline
#

parser = OptionParser("usage: %prog [options] corpus skill1.xml [skill2.xml ...]")

parser.add_option ("-l", "--lang", dest="lang", type = "str", default='en',
                   help="language (default: en)")

parser.add_option ("-v", "--verbose", action="store_true", dest="verbose",
                   help="verbose output")

(options, args) = parser.parse_args()

if options.verbose:
    logging.getLogger().setLevel(logging.DEBUG)
else:
    logging.getLogger().setLevel(logging.INFO)

if len(args)<2:
    parser.print_usage()
    sys.exit(1)

corpus_name = args[0]
skillfns = args[1:]

#
# cleanup / preparation
#
 
cmd = 'rm -rf %s/%s' % (QASRC_DIRFN, corpus_name)
logging.info(cmd)
os.system(cmd)

cmd = 'mkdir -p %s/%s' % (QASRC_DIRFN, corpus_name)
logging.info(cmd)
os.system(cmd)

#
# extract skills
#

    
def expand_choices(src):

    # turn choice switches %(% ... %|% ... %)%  into python lists

    srcl = []

    i = 0
    while i < len(src):

        choices_start = src[i:].find('%(%')
        if choices_start<0:         # no further choice switch -> finish
            srcl.append(src[i:])
            break
        else:

            choices_start += i

            if choices_start>0:
                srcl.append(src[i:choices_start]) # append text before choice switch
            choices_end = src[choices_start+3:].find('%)%')
            if choices_end < 0:
                logging.error ('%)% missing')
                break
            choices_end += choices_start+3

            choices = src[choices_start+3:choices_end]
            # logging.debug('%4d: [%d:%d] choices: %s', i, choices_start, choices_end, choices)

            srcl.