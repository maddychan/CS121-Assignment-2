'''
@Author: Rohan Achar ra.rohan@gmail.com
'''
import re

try:
    # For python 2
    from urlparse import urlparse, parse_qs
except ImportError:
    # For python 3
    from urllib.parse import urlparse, parse_qs

from Crawler4py.Config import Config
class SampleConfig(Config):
    def __init__(self):
        Config.__init__(self)
        self.UserAgentString = "INF141 <28859606 76439804 50233729 71903006>"

    def GetSeeds(self):
        '''Returns the first set of urls to start crawling from'''
        return ["http://www.ics.uci.edu"]

    def HandleData(self, parsedData):
        
        '''Function to handle url data. Guaranteed to be Thread safe.
        parsedData = {"url" : "url", "text" : "text data from html", "html" : "raw html data"}
        Advisable to make this function light. Data can be massaged later. Storing data probably is more important'''
        print(parsedData["url"])
        f = open("data1.txt",'a')
        f.write(parsedData["url"]+'\n')
        f.write(str(parsedData["text"].encode("utf-8")).strip() + '\n')
        return

#prevent traps like calandar, paper, and publication.
#re.match(pattern, string, flags=0)
#.*\.() | $
        
    def ValidUrl(self, url):
        '''Function to determine if the url is a valid url that should be fetched or not.'''
        parsed = urlparse(url)
#       parsed.hostname = www.ics.uci.edu
#       This is parsed.path = /computing/account/new
#        print("This is parsed.path: ")
#        print(parsed.path.lower())
        try:
            return ".ics.uci.edu" in parsed.hostname \
                and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4|jpg"\
                + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf|rss" \
                + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
                + "|thmx|mso|arff|rtf|jar|csv"\
                + "|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower()) \
                and not re.match("calendar\w",parsed.hostname)

        except TypeError:
            print ("TypeError for ", parsed)