from bs4 import BeautifulSoup
import requests
import threading

from app.DealsClass import DealsClass

OBJs = []
ThreadOBJs = []

def filterURLsDeals(input_urls):

    inputURLs = input_urls.split('\r\n')
    filteredURLs = []
    for url in inputURLs:
        if "-wip" in url:
            url = url.replace("-wip", "")
            filteredURLs.append(url)
        else:
            filteredURLs.append(url)

    print(filteredURLs)
    create_workers(filteredURLs)
    return OBJs

def create_workers(filteredURLs):

    global OBJs
    OBJs = []
    global ThreadOBJs
    ThreadOBJs = []

    for url in filteredURLs:
        t = threading.Thread(target=work, args=(url,))
        t.daemon = True
        t.start()
        ThreadOBJs.append(t)

    for thread in ThreadOBJs:
        thread.join()


def work(url):

    wipUrl = url.replace('www', 'www-wip')

    responseObjectLive = requests.get(url)
    responseObjectWip = requests.get(wipUrl)

    sourceCodeLive = responseObjectLive.text
    sourceCodeWip = responseObjectWip.text

    soupLive = BeautifulSoup(sourceCodeLive, 'lxml')
    soupWip = BeautifulSoup(sourceCodeWip, 'lxml')

    # print('\n\n\nsourceLive'+ sourceCodeLive)

    dealsClassLive = DealsClass(soupLive)
    dealsClassWip = DealsClass(soupWip)

    data = {}
    data['url'] = url
    liveDealsDict = {}
    wipDealsDict = {}
    differenceDealsDict = {}

    # Storing live data
    liveDealsDict['Intel Banner'] = dealsClassLive.get_intel_banner(soupLive)
    liveDealsDict['Piglet'] = dealsClassLive.get_piglet(soupLive)

    # Storing Wip data
    wipDealsDict['Intel Banner'] = dealsClassWip.get_intel_banner(soupWip)
    wipDealsDict['Piglet'] = dealsClassWip.get_piglet(soupWip)


    # Storing differences data
    for key, value in liveDealsDict.items():
        if key == 'Intel Banner':
            factor = True
            if len(liveDealsDict[key]) != len(wipDealsDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveDealsDict[key]):
                    valLive1 = val['banner_text']
                    valLive2 = val['Banner CTA']
                    valLive3 = val['Banner Image'].rsplit('/', 1)[-1]

                    valWip1 = wipDealsDict[key][idx]['banner_text']
                    valWip2 = wipDealsDict[key][idx]['Banner CTA']
                    valWip3 = wipDealsDict[key][idx]['Banner Image'].rsplit('/', 1)[-1]

                    if valLive1.strip("%20").lower() != valWip1.strip("%20").lower():
                        factor = False
                    if valLive2.strip("%20").lower() != valWip2.strip("%20").lower():
                        factor = False
                    if valLive3.strip("%20").lower() != valWip3.strip("%20").lower():
                        factor = False

            if factor is True:
                differenceDealsDict[key] = 'Pass'
            else:
                differenceDealsDict[key] = 'Fail'

        elif key == 'Piglet':
            factor = True
            if len(liveDealsDict[key]) != len(wipDealsDict[key]):

                factor = False
            else:
                for idx, val in enumerate(liveDealsDict[key]):
                    valLive = ''
                    valWip = ''
                    for a, b in liveDealsDict[key][idx].items():
                        valLive = b
                        if a == 'Piglet Image':
                            valLive = valLive.rsplit('/', 1)[-1]

                    for a, b in wipDealsDict[key][idx].items():
                        valWip = b
                        if a == 'Piglet Image':
                            valWip = valWip.rsplit('/', 1)[-1]

                    if valLive.strip("%20").lower() != valWip.strip("%20").lower():
                        factor = False

            if factor is True:
                differenceDealsDict[key] = 'Pass'
            else:
                differenceDealsDict[key] = 'Fail'


    data['liveDealsDict'] = liveDealsDict
    data['wipDealsDict'] = wipDealsDict
    data['differenceDealsDict'] = differenceDealsDict

    OBJs.append(data)
