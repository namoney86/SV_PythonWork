'''
Created on 2014. 4. 13.

@author: cho
'''

class LocalWeather:
    '''
     지역 정보를 담은 클래스
    '''


    def __init__(self, stdId, desc, ta,  localName):
        self.stnId = stdId
        self.desc = desc
        self.ta = ta
        self.localName = localName
        
        
    def printLocal(self):
        print("stnId:", self.stnId, "desc:", self.desc, "ta:", self.ta, "localName:", self.localName)