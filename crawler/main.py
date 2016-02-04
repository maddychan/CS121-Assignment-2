from Crawler4py.Crawler import Crawler
from MyCrawlerConfig import mycogfig

crawler = Crawler(mycogfig())

print (crawler.StartCrawling())

exit(0)