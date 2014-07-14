'''
Created on 2014. 4. 20.

@author: cho
'''
import xml.etree.ElementTree as ET
from weather.parser.WeatherParser import WeatherParser
from weather.dom.LocalWeather import LocalWeather
from weather.dom.Weather import Weather


class WeatherXMLParser(WeatherParser):



    def __init__(self):
        pass
    
    def parseWeatherResource(self, weatherResource):
        root = ET.fromstring(weatherResource)
        
        #root = tree.getroot()
        
        toDayWeather = None
        
        for weatherDOM in root:
            toDayWeather = Weather(year=weatherDOM.attrib['year'], month=weatherDOM.attrib['month'], day=weatherDOM.attrib['day'], hour=weatherDOM.attrib['hour'])
                
            localWeathers = []
        
            for localDOM in weatherDOM:
            
                stnId = localDOM.attrib["stn_id"]
                desc = localDOM.attrib["desc"]
                ta = localDOM.attrib["ta"]
                localName = localDOM.text
            
                localWeather = LocalWeather(stdId=stnId, desc=desc, ta=ta, localName=localName)
            
                localWeathers.append(localWeather)
                
        toDayWeather.setLocalWeathers(localWeathers)
        
        return toDayWeather
