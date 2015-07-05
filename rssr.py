import feedparser
from lxml.html.clean import Cleaner
from time import strftime, strptime
from os import listdir, chdir, getcwd
from os.path import abspath

def html2text(html, allowed_tags=["a", "abbr", "article", "aside",
                                  "b", "base", "blockquote", "body",
                                  "br", "caption", "cite", "code", "col", "colgroup",
                                  "dd", "del", "dfn", "dl", "dt",
                                  "em", "embed", "figcaption", "figure", "footer",
                                  "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html",
                                  "i", "img",
                                  "li",
                                  "map", "mark", "math", "meta", "meter",
                                  "nav", "noscript",
                                  "object", "ol", "optgroup", "option", "output",
                                  "p", "param", "pre", "progress",
                                  "q", "rp", "rt", "ruby",
                                  "s", "samp", "section", "small", "source", "span", "strong", "sub", "sup", "svg",
                                  "table", "tbody", "td", "th", "thead", "tfoot", "time", "title", "tr", "track",
                                  "u", "ul",
                                  "var", "video",
                                  "wbr"]):
    cleaner = Cleaner()
    cleaner.allow_tags = allowed_tags
    cleaner.remove_unknown_tags = False
    return cleaner.clean_html(html)

def feeds_get(feeds):
    feedsr = []
    for feed in feeds:
        feedsr.append(feedparser.parse(feed))
    return feedsr

def rss_strftime(strf, strp):
    try:
        return strftime(strf, strptime(strp, "%a, %d %b %Y %H:%M:%S %z"))
    except ValueError:
        return strftime(strf, strptime(strp, "%a, %d %b %Y %H:%M:%S %Z"))

def htmlls(directory, reverse=False):
    basedir = getcwd()
    chdir(directory)

    ls = listdir()
    ls.sort(reverse=reverse)
    index = ""
    for art in ls:
            index += "<tr><td><a href = \"file://{}\">{}</a></td></tr>\n".format(abspath(art), art)

    chdir(basedir)
    return index
