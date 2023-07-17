
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
import random

from optparse import OptionParser
from nltools  import misc

from annoy import AnnoyIndex

PROC_TITLE        = 'kb_index'

EMB_DIR           = 'data/kb/%s/emb'

NUM_TREES         = 10 # FIXME
SEARCH_K          = 2  # FIXME
DIMENSIONS        = 512
INDEX_FN          = 'data/kb/%s/idx.ann'

#
# init
#