import urllib2
from xml.etree import ElementTree

class Tour(object):
    """An instance of this class is to be instantiated with an arbitrary 
    number of US cities, and is used to fetch information from the web."""

    __googleAPI = "http://maps.googleapis.com/maps/api/distancematrix/xml"

    def __init__(self, *cities, **kwarg):
        self._lstCity = []
        for city in cities:
            self._lstCity.append(city)  
    
    # Get the total distance between the cities, default mode is driving.   
    def getDistance(self, mode="driving"):
        totalDistance = 0
        counter, nextCounter = 0,0
        
        #loop through all the city list to get the total distance
        for counter in range(0, len(self._lstCity) - 1):
            nextCounter = counter + 1
            url = self.__googleAPI
            url = url + "?origins={0}&destinations={1}&mode={2}&sensor=false".format(self._lstCity[counter].replace(" ","+").replace(",",""), self._lstCity[nextCounter].replace(" ","+").replace(",",""), mode)
            
            try:
                response = urllib2.urlopen(url).read()
                xmlResponse = ElementTree.fromstring(response)

                #from xml read the distance value
                distance = float(xmlResponse.find("row").find("element").find("distance").findtext("value"))
                totalDistance += distance

            except urllib2.HTTPError, err:
                if err.code == 404:
                       print "Page not found!"
                elif err.code == 403:
                    print "Access denied!"
                else:
                    print "An error has occured. Please try after sometime."
            except urllib2.URLError, err:
                print "An error has occured. Please try after sometime."
        
        return totalDistance

    def __str__(self):
        return str(self._lstCity)