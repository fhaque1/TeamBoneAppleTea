from urllib2 import urlopen, URLError
from json import loads

class censusAPIManager:

    def __init__(self, link, apiKey):
        self.apiKey = "4cd111bdf8258f571273b5a7b85c507b675bd04f"

    def getUrlContent(self, link):
        urlFile = urlopen(link)
        urlContent = urlFile.read()
        return urlContent

    def getAPIData(self, link, needAPIKey=False):
        if needAPIKey:
            link += '&key=' + self.apiKey
        apiData = self.getUrlContent(link)
        return apiData        
