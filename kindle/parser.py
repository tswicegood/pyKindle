import datetime
import time

__all__ = ['parse', ]

KINDLE_FIRST_LINE_NOISE = "\xef\xbb\xbf"
KINDLE_DIVIDER = '='*10
KINDLE_DATE_FORMAT = '%A, %B %d, %Y, %I:%M %p'
LINE_BREAK = "\r\n"

def filter_title(title_meta):
    return title_meta[:title_meta.rfind(' (')]

def filter_author(title_meta):
    return title_meta[title_meta.rfind(' (')+2:title_meta.rfind(')')]

def filter_type(meta):
    return meta[2:meta.find(' Loc')]

def filter_location(meta):
    return meta[meta.find('Loc. ')+5:meta.find(' | ')]

def filter_date(meta):
    text_date = meta[meta.find('Added on ')+9:]
    return datetime.datetime(*time.strptime(text_date, KINDLE_DATE_FORMAT)[:-2])

def parse(filename,
          title_filter=filter_title,
          author_filter=filter_author,
          type_filter=filter_type,
          location_filter=filter_location,
          date_filter=filter_date):
    fp = open(filename, 'rb')
    contents = fp.read().lstrip(KINDLE_FIRST_LINE_NOISE)
    fp.close()

    contents = contents.strip().rstrip(KINDLE_DIVIDER)
    blocks = contents.split(KINDLE_DIVIDER)

    ret = []
    for block in blocks:
        title_meta, meta, _empty_line, notes, _empty_line = block.lstrip().split(LINE_BREAK)
        title = title_filter(title_meta)
        author = author_filter(title_meta)
        type = type_filter(meta)
        location = location_filter(meta)
        date = date_filter(meta)

        ret.append({
            "title": title,
            "type": type,
            "location": location,
            "date": date,
            "notes": notes.strip() if notes.strip() else None,
            "author": author,
        })
    return ret


