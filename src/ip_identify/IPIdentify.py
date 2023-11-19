import requests
from json import loads, dumps

class IPEnquireIPApi:
    def __init__(self, ipaddr = None):
        self._url = "http://ip-api.com/json"

        # Basic Initializations
        self.isp = None
        self.country = None
        self.region = None
        self.city = None

        if(ipaddr != None):
            # FIXME: There are possiblities of different types
            #        of errors
            resp = self.getRawDict(ipaddr)
            if(type(resp) == dict):
                self.setIsp(resp)
                self.setCountry(resp)
                self.setRegion(resp)
    def setIsp(self,resp):
        if("isp" in resp):
            self.isp = resp["isp"]
    def setCountry(self,resp):
        if("country" in resp):
            self.country = resp["country"]
    def setRegion(self,resp):
        if("region" in resp):
            self.region = resp["region"]+" "
        if("regionName" in resp):
            self.region += resp["regionName"]
        if(self.region != None):
            self.region = self.region.strip()
    def setCity(self, resp):
        if("city" in resp):
            self.city = resp["city"]
    def getRawDict(self,ip=None):
        if(ip == None):
            return None
        return loads(requests.get(self._url + "/" + ip).text)

# Indipendant Class to Enquire
def IPEnquire(ipaddr:str,api = "ip-api.com"):
    '''
        IPEnquire will require IP address and which API to use

        Supported api list
        "ip-api.com"

        Example:
            IPEnquire(ipaddr = "1.1.1.1", api = "ip-api.com")
    '''
    if(api == "ip-api.com"):
        return IPEnquireIPApi(ipaddr)


class IPLocation:
    def __init__(self):
        '''Object creation of this class is not necessary!'''
        pass
    @staticmethod
    def getISP(ipEnquiryData):
        '''Returns the name of the ISP given by the Enquiry driver'''
        return ipEnquiryData.isp
    @staticmethod
    def getRegion(ipEnquiryData):
        '''Returns the region data given by the Enquiry driver'''
        return ipEnquiryData.region
    @staticmethod
    def getCountry(ipEnquiryData):
        '''Returns the name of the Country given by the Enquiry driver'''
        return ipEnquiryData.country
    @staticmethod
    def getCity(ipEnquiryData):
        '''Returns the name of the City given by the Enquiry driver'''
        return ipEnquiryData.city