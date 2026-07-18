import requests
from bs4 import BeautifulSoup
import pandas as pd



def extractor(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
 


    spans = soup.find_all('span',class_ = "Progress-item color-bg-success-emphasis")
    sp= list(spans)


    # for i in range(len(spans)):
    #     print(s.iloc[i:167])
    # print(len(sp))

    mylistper = []
    deflen=len(str(spans[0]))

    # print(deflen)
    if(deflen==168):
        deflen = 168
    elif(deflen==166):
        deflen = 166
    else:
        deflen = 167


    for i in range(0,len(sp)):
        newstr = str(sp[i])
    # print(len(str(i)))
        if deflen == 168:
            mylistper.append(newstr[152:157])  
            if i >= len(sp)-1:
                break
            else:
                deflen = len(newstr[i+1])
        elif deflen == 167:
            mylistper.append(newstr[152:156])  
        
            if i >= len(sp)-1:
                break
            else:
                deflen = len(newstr[i+1])
        else:
            mylistper.append(newstr[152:155])  
    # newstr =str(sp[0])
    # mylistper.append(newstr[10:13])
    # print(mylistper)
    


    mylistlan = []
    spans = soup.find_all('span',class_ = "color-fg-default text-bold mr-1")
    for i in range(len(spans)):
        mylistlan.append(spans[i].text)

    # print(mylistlan)




    # for i in list(spans):
        # print(i.get("style"))
        # print(i.attrs['style'])
        # print(type(i['style']))




    df = pd.DataFrame(mylistper,mylistlan)
    
    return df

print(extractor("https://github.com/torvalds/linux"))