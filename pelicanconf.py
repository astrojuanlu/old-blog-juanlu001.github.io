#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Juan Luis Cano Rodríguez"
SITENAME = "juanlu.space"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/Madrid"

DEFAULT_LANG = "en"
THEME = "./theme"

TAGS_URL = "tags.html"
ARCHIVES_URL = "archives.html"

PLUGINS = ["assets"]
PLUGIN_PATHS = ["./theme/plugins"]

STATIC_PATHS = ["extra/CNAME"]
EXTRA_PATH_METADATA = {"extra/CNAME": {"path": "CNAME"}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USER_LOGO_URL = "/theme/img/logo.svg"

# Blogroll
LINKS = [("Home", "/")]

SOCIAL = [
    ("GitHub", "https://github.com/Juanlu001"),
    ("GitLab", "https://gitlab.com/astrojuanlu"),
    ("LinkedIn", "https://www.linkedin.com/in/juanluiscanor/"),
    ("hello@juanlu.space", "mailto:hello@juanlu.space"),
]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
