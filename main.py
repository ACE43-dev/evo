import requests
from bs4 import BeautifulSoup
# import numpy as np
import pandas as pd
x = pd.read_csv("websites.csv")
# Url = x.Name
Url = pd.Series(["https://github.com/codecrafters-io/build-your-own-x","https://github.com/sindresorhus/awesome","https://github.com/freeCodeCamp/freeCodeCamp","https://github.com/public-apis/public-apis"],name="Name")
class Tools:
    def __init__(self,Url:pd.Series):
        self.Url = Url
        # self.series1 = pd.Series([],name="Language")
        # self.series2 = pd.Series([],name="percentage")
        # self.dataUrl = pd.Series([],name="Url")
        self.series1 = []
        self.series2 = []
        self.dataUrl = []
        self.count = 0
        # self.df = pd.DataFrame()
    def vaildCheck(self):
        for url in self.Url:
            print(url)
    
    def extractor(self):
        for url in self.Url:
                    self.count = self.count+1
                    print(self.count)
                    self.response = requests.get(url)
                    self.soup = BeautifulSoup(self.response.text, 'html.parser')
                    
                    # data 1 is language data 
                    self.data1 = self.soup.find_all('span',class_ = "color-fg-default text-bold mr-1")
                    if(self.data1 != []):
                        for i in range(len(self.data1)):
                            self.series1.append(self.data1[i].text)
                            self.dataUrl.append(url)
                            
                            
                    # data 2 is percentage data 
                    self.data2 = (self.soup.find_all('span',class_ = "Progress-item color-bg-success-emphasis"))
                    if(self.data2 != []):

                        for i in range(len(self.data2)):
                            temp = str(self.data2[i])
                            x = len(temp)

                            if x == 168:
                                self.series2.append(temp[152:157])
                            elif x == 167:
                                self.series2.append(temp[152:156])
                            elif x == 166:
                                self.series2.append(temp[152:155])
                            else:
                                self.series2.append("problem")
             
        # print(self.series1)
        # print(self.series2)
        # print(self.dataUrl)
        return pd.DataFrame({
            "Languages":pd.Series(self.series1),
            "percentage":pd.Series(self.series2),
            "url":pd.Series(self.dataUrl)
        })
        
                    
                    
            
                
t1 = Tools(Url)
t1.extractor().to_csv("data.csv")