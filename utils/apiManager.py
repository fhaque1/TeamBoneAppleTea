from urllib2 import urlopen, URLError
from json import loads

class censusAPIManager:

    def __init__(self, link):
        self.mainUrl = link
        self.apiKey = self.getAPIKey()
        
    def getAPIKey(self):
        with open('../apiKey.txt') as file_:
            key = file_.read().split("\n")[0]
        return key
    
    def getUrlContent(self, link):
        urlFile = urlopen(link)
        urlContent = urlFile.read()
        return urlContent

    def getAPIData(self, year, request, needAPIKey=False):
        apiUrl = self.mainUrl + year + '/' + request
        if needAPIKey:
            apiUrl += '&key=' + self.apiKey
        apiData = self.getUrlContent(apiUrl)
        return eval(apiData) 

		
