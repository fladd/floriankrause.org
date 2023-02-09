import os
import glob
from datetime import date

import pymdownx.emoji


YEAR = date.today().year

# HTML output directory
# Takes absolute path or relative to this file
output_dir = "../build"

# (Sub)directories to not build pages from
# Takes absolute paths or relative to this file; not applied recursively
ignore_dirs = glob.glob(f"{output_dir}/**/", recursive=True)
ignore_dirs.extend(glob.glob(f"../blog/**/", recursive=True))

# Default settings
# Can be overwritten by meta data
defaults = {
    "title":        None,  # None will set title to file/directory name
    "description":  "Cognitive/Affective Neuroscientist",
    "author":       "Florian Krause",
    "authorlink":   "https://www.floriankrause.org",
    "date":         "",
    "copy_year":    f"2018-{YEAR}" if YEAR > 2018 else f"{YEAR}",
    "style":        os.path.abspath("styles/default.css"),
    "settings":     "nonav",
    "favicon":      "favicon.ico"
}

# HTML Head
# Can make use of defaults/meta data (lowercase, prefixed with $)
html_head = [
    '<meta charset="UTF-8">',
    '<meta name="viewport" content="width=device-width, initial-scale=1">',
    '<title>$title | Florian Krause</title>',
    '<meta name="author" content="$author">',
    '<meta name="description" content="$description">',
    '<link href="$style" rel="stylesheet" media="screen">',
    '<link rel="stylesheet" href="https://cdn.rawgit.com/jpswalsh/academicons/master/css/academicons.min.css">',
    #'<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fork-awesome@1.2.0/css/fork-awesome.min.css" integrity="sha256-XoaMnoYC5TH6/+ihMEnospgm0J1PM/nioxbOUdnM8HY=" crossorigin="anonymous">',
    '<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">',
    '<link rel="icon" href="$favicon" type="image/x-icon" />'
]

# HTML navigation
# Can make use of defaults/meta data (lowercase, prefixed with $) and listings
html_nav = [
    '[BREADCRUMB]',
]

# HTML Header
# Can make use of defaults/meta data (lowercase, prefixed with $) and listings
html_header = [
    '<a href="floriankrause.jpg"><img src="floriankrause_100x100.jpg" style="border-radius: 10%;"></a>',
    '',
    '<h1>Florian Krause</h1>',
    '<p>$description</p>',
    '<small>',
    f'**[About me]({os.path.abspath("../index.md")})**',
    '|',
    f'**[Research]({os.path.abspath("../research.md")})**',
    '|',
    f'**[Publications]({os.path.abspath("../publications.md")})**',
    '|',
    f'**[Open Science]({os.path.abspath("../open-science.md")})**',
    '|',
    #f'**[Blog]({os.path.abspath("../blog.md")})**',
    #'|',
    f'**[Contact]({os.path.abspath("../contact.md")})**',
    '</small>',
]

# HTML Footer
# Can make use of defaults/meta data (lowercase, prefixed with $) and listings
html_footer = [
    '<p>',
    '<a href="https://orcid.org/0000-0002-2754-3692"><i class="ai ai-orcid-square ai-3x"></i></a>',
    '<a href="https://researcherid.com/rid/C-2745-2013"><i class="ai ai-researcherid-square ai-3x"></i></a>',
    '<a href="https://researchgate.net/profile/Florian_Krause"><i class="ai ai-researchgate-square ai-3x"></i></a>',
    '<a href="https://scholar.google.com/citations?hl=en&user=nlx-2QsAAAAJ"><i class="ai ai-google-scholar-square ai-3x"></i></a>',
    '<a rel="me" href="https://qoto.org/@floriankrause" class="fa-stack fa-2x" style="font-size: 1.5em; margin:0px -0.4em; vertical-align:top;">',
        '<i class="fa fa-square fa-stack-2x"></i>',
        '<i class="fab fa-mastodon fa-stack-1x fa-inverse" style="font-size: 1.5em"></i>',
    '</a>',
    '<a href="https://www.linkedin.com/in/florian-krause-46736654"><i class="fab fa-linkedin fa-3x"></i></a>',
    '<a href="https://www.twitter.com/fladd"><i class="fab fa-twitter-square fa-3x"></i></a>',
    '<a href="https://github.com/fladd"><i class="fab fa-github-square fa-3x"></i></a>',
    '</p>',
    '<p>',
    '<strong>&copy; $copy_year <a href="$authorlink">$author</a></strong>',
    '<br>',
    '<em>$date</em>',
    '</p>',
    '<p>',
    'Created with <a href="https://github.com/fladd/StuffPages">'\
    'StuffPages</a>',
    '</p>',
]

# Format for each item in pages listings ([PAGES])
# Can make use of defaults/meta data (lowercase, prefixed with $)
# $LINK will be replaced by a (relative) link to page
pagelisting_format = '<p><a href="$LINK">$title</a><br />$description<br /><small><em>$date</em></small></p>'

# Format for each item in breadcrumb listings ([BREADCRUMB])
# Can make use of defaults/meta data (lowercase, prefixed with $)
# $LINK will be replaced by (relative) link to page
breadcrumb_format = '<a href="$LINK">$title</a>'

# Additional 'extras' to be used by the Python 'markdown' package
extras = [
    'markdown.extensions.def_list',    # Definition Lists
    'markdown.extensions.footnotes',   # Footnotes
    'markdown.extensions.md_in_html',  # Markdown within HTML
    'markdown.extensions.tables',      # Tables
    'markdown.extensions.toc',         # Table of Contents
    'pymdownx.betterem',               # Improved emphasis handling
    'pymdownx.caret',                  # Insert and superscript
    'pymdownx.emoji',                  # Emoji
    'pymdownx.highlight',              # Syntax highlighting
    'pymdownx.magiclink',              # Generate links from raw URLs
    'pymdownx.superfences',            # Fenced Code Blocks
    'pymdownx.tasklist',               # Task Lists
    'pymdownx.tilde',                  # Delete and subscript
    # Add more 'extras' here
]

# Configuration for additional 'extras'
extras_configs = {
    'markdown.extensions.footnotes': {
        'BACKLINK_TEXT': u"&#8617;&#65038;",
    },
    'markdown.extensions.toc': {
        #'anchorlink': True,
        'permalink': "#"
    },
    "pymdownx.emoji": {
        "emoji_generator": pymdownx.emoji.to_alt,
        "alt": "unicode",
    },
    'pymdownx.tilde': {
         'subscript': False
    }
}
