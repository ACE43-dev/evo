import requests
from bs4 import BeautifulSoup
url = 'https://github.com/ACE43-dev/data-analysis'


response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
 


spans = soup.find_all('span',class_ = "Progress-item color-bg-success-emphasis")
sp= list(spans)


# for i in range(len(spans)):
#     print(s.iloc[i:167])

mylistper = []
deflen=len(spans[0])
if(deflen==168):
    deflen = 168
elif(deflen==166):
    deflen = 166
else:
    deflen = 167


for i in range(len(sp)):
    newstr = str(sp[i])
    # print(len(str(i)))
    if deflen == 168:
        mylistper.append(newstr[152:157])  
        deflen = len(sp[i+1])
    elif deflen == 167:
        mylistper.append(newstr[152:156])  
        deflen = len(sp[i+1])
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



import pandas as pd
df = pd.DataFrame(mylistper,mylistlan)
print(df)