'''
Created on 2014. 4. 13.

@author: cho
'''
import xml.etree.ElementTree as ET

from weather.dom.LocalWeather import LocalWeather
from weather.dom.Weather import Weather

if __name__ == '__main__':
    fileName = r"C:\workspace\WeatherXML\src\weather\source\sfc_web_map.xml"
    
    tree = ET.parse(fileName)
    
    root = tree.getroot()
    
    toDayWeather = None
    
    for weatherDOM in root:
        toDayWeather = Weather(year=weatherDOM.attrib['year'], month=weatherDOM.attrib['month'], day=weatherDOM.attrib['day'], hour=weatherDOM.attrib['hour'])
                
        localWeathers = []
        
        for localDOM in weatherDOM:
            
            stnId = localDOM.attrib["stn_id"]
            desc = localDOM.attrib["desc"]
            ta = localDOM.attrib["ta"]
            tag = localDOM.tag
            localName = localDOM.text
            
            localWeather = LocalWeather(stdId=stnId, desc=desc, ta=ta, localName=localName)
            
            localWeathers.append(localWeather)
            
        toDayWeather.setLocalWeathers(localWeathers)
    
    
    toDayWeather.printWeatherInfo()