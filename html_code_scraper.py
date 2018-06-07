from	bs4	import	BeautifulSoup
from	urllib.request	import	urlopen
my_address	=	"https://realpython.com/practice/dionysus.html"
html_page	=	urlopen(my_address)
html_text	=	html_page.read()	#	Py	3:	decode
my_soup	=	BeautifulSoup(html_text)