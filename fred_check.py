import re
import pycurl
import os.path
from io import BytesIO
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

def url_get_path(url):
        parsed = urlparse(url)
        path = parsed.path
        return path

def url_get_last_path(url):
        parsed = urlparse(url)
        path = parsed.path
        sections = []
        while path != '/':
                temp = os.path.split(path)
                path = temp[0]
                sections.append(temp[1])
        return sections[-1]

def check_NS(path_url):

def check_xalok(path_url):

def check_oldfred(path_url):

def check_elastic(id_article):

def check_google(id_article):


def url_clasifier(url):
	headers = StringIO()
	buffer = BytesIO()
	c = pycurl.Curl()
	header = ['Host: www.futbolred.com']
	c.setopt(pycurl.HTTPHEADER, header)
	c.setopt(c.URL, url)
	c.setopt(pycurl.WRITEFUNCTION, buffer.write)
	c.setopt(c.HEADER, 1)
	c.setopt(c.NOBODY, 1)
	c.setopt(c.HEADERFUNCTION, headers.write)
	c.perform()
	c.close()
	code_response = headers.getvalue().split('\n')[0].split(' ')[1]
	return code_response

def read_file_urls(path_file):
        f = open(path_file,"r")
        list_urls = []
        for line in f:
                list_urls.append(line)
        f.close()
        return list_urls

def write_report

if __name__ == "__main__":
	list_urls = read_file_urls()

