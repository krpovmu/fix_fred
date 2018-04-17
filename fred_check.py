import pycurl
from io import BytesIO
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def check_NS()

def check_xalok()

def check_oldfred()

def check_elastic()


def url_clasifier(url):
	headers = StringIO()
	buffer = BytesIO()
	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(pycurl.WRITEFUNCTION, buffer.write)
	c.setopt(c.HEADER, 1)
	c.setopt(c.NOBODY, 1) # header only, no body
	c.setopt(c.HEADERFUNCTION, headers.write)
	c.perform()
	c.close()
	print headers.getvalue().split('\n')[0].split(' ')


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


