#!/usr/bin/env python

import base_filters

COPY_GOOGLE_DOC_KEY = '1oeXbiWwFtXe7ID5d0tKpEVHVVW2lQ3wRH35Dh5X16aY'

USE_ASSETS = True

# Use these variables to override the default cache timeouts for this graphic
# DEFAULT_MAX_AGE = 20
ASSETS_MAX_AGE = 30

JINJA_FILTER_FUNCTIONS = base_filters.FILTERS
