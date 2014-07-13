import os
import gzip
import storytracker


def open_archive_filepath(path):
    """
    Accepts a file path and returns a file object ready for analysis
    """
    # Split the file extension from the name
    name = os.path.basename(path)
    name, ext = os.path.splitext(name)
    # Extract the URL and timestamp from the file name
    url, timestamp = storytracker.reverse_archive_filename(name)
    # If it is gzipped, then open it that way
    if ext == '.gz':
        obj = gzip.open(path)
    # Otherwise handle it normally
    else:
        obj = open(path, "rb")
    return URL(url, timestamp, obj.read())


class URL(object):
    """
    An URL's archived HTML response with tools for analysis
    """
    def __init__(self, url, timestamp, html):
        self.url = url
        self.timestamp = timestamp
        self.html = html