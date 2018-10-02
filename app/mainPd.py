from bs4 import BeautifulSoup
import requests
import threading

from app.PdClass import PdClass

OBJs = []
ThreadOBJs = []

def filterURLsPd(input_urls):

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

    pdClassLive = PdClass(soupLive)
    pdClassWip = PdClass(soupWip)

    data = {}
    data['url'] = url
    livePdDict = {}
    wipPdDict = {}
    differencePdDict = {}

    # Storing Live Data
    livePdDict['Base Lang']= pdClassLive.get_baselang()
    livePdDict['Browser Title']= pdClassLive.get_browsertitle()
    livePdDict['Meta Description']= pdClassLive.get_metaDescription()
    livePdDict['Meta Keywords']= pdClassLive.get_metaKeywords()
    livePdDict['Breadcrumb List']= pdClassLive.get_breadcrumb()
    livePdDict['Page Title']= pdClassLive.get_pagetitle()
    livePdDict['CTA']= pdClassLive.get_cta()
    livePdDict['Hero Title']= pdClassLive.get_herotitle()
    livePdDict['Hero Description']= pdClassLive.get_herodescription()
    livePdDict['Price']= pdClassLive.get_pricing()
    livePdDict['Hero Image Link']= pdClassLive.get_heroimagelink()
    livePdDict['Hero Video']= pdClassLive.get_herovideo()
    livePdDict['Tech List']= pdClassLive.get_techspecs()
    livePdDict['Overview List']= pdClassLive.get_overview()
    livePdDict['Awards List']= pdClassLive.get_awards()
    livePdDict['Service List']= pdClassLive.get_services()
    livePdDict['Support List']= pdClassLive.get_support()


    # Storing WIP Data
    wipPdDict['Base Lang']= pdClassWip.get_baselang()
    wipPdDict['Browser Title']= pdClassWip.get_browsertitle()
    wipPdDict['Meta Description']= pdClassWip.get_metaDescription()
    wipPdDict['Meta Keywords']= pdClassWip.get_metaKeywords()
    wipPdDict['Breadcrumb List']= pdClassWip.get_breadcrumb()
    wipPdDict['Page Title']= pdClassWip.get_pagetitle()
    wipPdDict['CTA']= pdClassWip.get_cta()
    wipPdDict['Hero Title']= pdClassWip.get_herotitle()
    wipPdDict['Hero Description']= pdClassWip.get_herodescription()
    wipPdDict['Price']= pdClassWip.get_pricing()
    wipPdDict['Hero Image Link']= pdClassWip.get_heroimagelink()
    wipPdDict['Hero Video']= pdClassWip.get_herovideo()
    wipPdDict['Tech List']= pdClassWip.get_techspecs()
    wipPdDict['Overview List']= pdClassWip.get_overview()
    wipPdDict['Awards List']= pdClassWip.get_awards()
    wipPdDict['Service List']= pdClassWip.get_services()
    wipPdDict['Support List']= pdClassWip.get_support()


    # Storing differences data
    for key, value in livePdDict.items():
        if value == wipPdDict[key]:
            differencePdDict[key] = 'Pass'
        else:
            differencePdDict[key] = 'Fail'

    data['livePdDict'] = livePdDict
    data['wipPdDict'] = wipPdDict
    data['differencePdDict'] = differencePdDict

    OBJs.append(data)
