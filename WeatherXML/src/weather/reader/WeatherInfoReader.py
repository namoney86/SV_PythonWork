'''
Created on 2014. 4. 20.

@author: cho
'''

class WeatherInfoReader:

    def __init__(self, conn, parser):
        self.connector =  conn
        self.parser = parser
    
    
    def readWeatherInfo(self):
        
        conn = self.connector.connectWeatherResource()
        
        resource = conn.read()
        
        todayWeather = self.parser.parseWeatherResource(resource)
        
        conn.close()
        
        return todayWeather
        
    