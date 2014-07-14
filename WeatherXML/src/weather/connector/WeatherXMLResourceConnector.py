'''
Created on 2014. 4. 20.

@author: cho
'''
from weather.connector.WeatherResourceConnector import WeatherResourceConnector

class WeatherXMLResourceConnector(WeatherResourceConnector):
    
    
    def __init__(self, locationUrl):
        self.__locationUrl = locationUrl
        
        
    def connectWeatherResource(self):
        
        import urllib.request
        
        conn = urllib.request.urlopen("http://www.kma.go.kr/XML/weather/sfc_web_map.xml");
        
        return conn