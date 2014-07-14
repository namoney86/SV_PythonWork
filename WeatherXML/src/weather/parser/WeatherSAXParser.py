'''
Created on 2014. 4. 20.

@author: cho


'''
from weather.dom.LocalWeather import LocalWeather
from weather.dom.Weather import Weather
from weather.parser.WeatherParser import WeatherParser
import xml.sax

class WeatherSAXParser(WeatherParser):

    def __init__(self):
        pass
    
    def parseWeatherResource(self, weatherResource):
        
        handler = WeatherSAXHandler()
        
        xml.sax.parseString(weatherResource, handler)
        
        weather = handler.getWeatherInfo()
        
        return weather
    
class WeatherSAXHandler(xml.sax.ContentHandler):
    
    __weather = None
    
    __localWeathers = []
    
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        
    def startElement(self, name, attrs):
        
        if name == "weather":
            
            year = attrs.getValue('year')
            month = attrs.getValue('month')
            day = attrs.getValue('day')
            hour = attrs.getValue('hour')
            
            self.__weather = Weather(year=year, month=month, day=day, hour=hour)            
        
        if name == "local":
            
            stnId = attrs.getValue('stn_id')
            descDOM = attrs.getValue('desc')
            taDOM = attrs.getValue('ta')
            
            self.dic = dict(stnId=stnId, desc=descDOM, ta=taDOM)
        
    def endElement(self, name):
        
        if name == 'local':
            stnId = self.dic['stnId']
            desc = self.dic['desc']
            ta = self.dic['ta']
            
            localName = self.localName
            
            localWeather = LocalWeather(stnId, desc, ta, localName)
            
            self.__localWeathers.append(localWeather)
            
        elif name =='weather':
            self.__weather.setLocalWeathers(self.__localWeathers)
            
            
    def characters(self, content):
        self.localName = content
        
    def getWeatherInfo(self):
        return self.__weather
    