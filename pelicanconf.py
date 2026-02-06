AUTHOR = "SRCF"
SITENAME = "SRCF Comms"
SITEURL = ""

PATH = "content"
TIMEZONE = "Europe/London"
DEFAULT_LANG = "en"

THEME = "simple"

# Per-post HTML permalinks (canonical URLs)
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

# Atom feed
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None

# No timeline / no listing pages
INDEX_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
AUTHOR_SAVE_AS = ""

# Keep pages for a minimal root/about
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
