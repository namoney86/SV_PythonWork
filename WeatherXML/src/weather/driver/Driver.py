'''
Created on 2014. 4. 20.

@author: cho
'''
from weather.reader.WeatherInfoReader import WeatherInfoReader
from weather.connector.WeatherXMLResourceConnector import WeatherXMLResourceConnector
from weather.parser.WeahterXMLParser import WeatherXMLParser
from weather.parser.WeatherSAXParser import WeatherSAXParser

if __name__ == '__main__':
    
    fileName = r"http://www.kma.go.kr/XML/weather/sfc_web_map.xml"
    
    conn = WeatherXMLResourceConnector(fileName)
    
    #parser = WeatherXMLParser()
    
    parser = WeatherSAXParser()
    
    reader = WeatherInfoReader(conn=conn, parser=parser)
    
    todayWeather = reader.readWeatherInfo()
    
    todayWeather.printWeatherInfo()