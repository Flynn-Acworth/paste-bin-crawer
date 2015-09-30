import requests
from bs4 import BeautifulSoup
import bs4

    
def archiveGrab(exceptionList):
    
    archiveUrl = "http://pastebin.com/archive"
    r = requests.get(archiveUrl)
    soup = BeautifulSoup(r.content)
    links = soup.find_all("a")
    print "Grabbing Links"
    found_links = []
    
    for i in links:
        for c in exceptionList:
            if c in i.text.lower():
                if i.text not in found_links:
                    found_links.append(i.text)
                    print "FOUND KEYWORD: " + c + " IN: " + i.text
                    check = raw_input("Do you want to fetch data y/n: ")
                    if check == "y":
                        pageGrab(i.get("href")) 
                    else:
                        pass
                else:
                    pass
            else:
                pass
            
    

def pageGrab(link):
    filename = raw_input("Enter filename to save to: ")
    file = open(filename, "w")
    url = "http://www.pastebin.com" + link
    req = requests.get(url)
    soup2 = BeautifulSoup(req.content)
    for i in soup2.find_all('div', {'class':'textarea_border'}):
        file.write(i.text)
    file.close()
        


exceptionList = [""] # add keywords here to search for them in pastebin titles

while True:
    archiveGrab(exceptionList)
    raw_input("Enter to run again")
