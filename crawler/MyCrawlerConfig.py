import re
from Crawler4py.Config import Config
try:
    # For python 2
    from urlparse import urlparse, parse_qs
except ImportError:
    # For python 3
    from urllib.parse import urlparse, parse_qs
    
class mycogfig(Config):
    
    def __init__(self):
        Config.__init__(self)
        self.UserAgentString = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    

    def GetSeeds(self):
        '''Returns the first set of urls to start crawling from'''
        return ["http://www.ics.uci.edu"]

    def HandleData(self, parsedData):
        '''Function to handle url data. Guaranteed to be Thread safe.
        parsedData = {"url" : "url", "text" : "text data from html", "html" : "raw html data"}
        Advisable to make this function light. Data can be massaged later. Storing data probably is more important'''
        '''print(parsedData["text"])'''
        print(parsedData["url"])
        #write url to a txt file
        file = open("Crawldata.txt","a")
        file.write(parsedData["url"])
        file.close()
        return

    def ValidUrl(self, url):
        '''Function to determine if the url is a valid url that should be fetched or not.'''
        parsed = urlparse(url)
        try:
            return "ics.uci.edu" in parsed.hostname \
                and not re.match(".*\.(css|js|bmp|gif|jpe?g|ico" + "|png|tiff?|mid|mp2|mp3|mp4"\
                + "|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf" \
                + "|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso|epub|dll|cnf|tgz|sha1" \
                + "|thmx|mso|arff|rtf|jar|csv"\
                + "|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

        except TypeError:
            print ("TypeError for ", parsed)
