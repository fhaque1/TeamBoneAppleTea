from urllib2 import urlopen, URLError
from json import loads

class censusAPIManager:

    def __init__(self, link):
        self.mainUrl = link
        self.apiKey = self.getAPIKey()
        
    def getAPIKey(self):
        #with open('../apiKey.txt') as file_:
        #    key = file_.read()
        #return key
		return "4cd111bdf8258f571273b5a7b85c507b675bd04f"
    
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
