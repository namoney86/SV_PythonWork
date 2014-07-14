'''
Created on 2014. 4. 13.

@author: cho
'''

class Weather:
    '''
    날씨 클래스
    '''
    __localWeathers = []
    

    def __init__(self, year, month, day, hour):
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        
    def setLocalWeathers(self, localWeathers):
        self.__localWeathers = localWeathers
        
    def printWeatherInfo(self):
        print('Year :', self.year, '\nMonth :', self.month, '\nDay :', self.day, '\nHour :', self.hour)
        print('\n')
        
        for localWeather in self.__localWeathers:
            localWeather.printLocal()