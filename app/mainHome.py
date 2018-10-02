from bs4 import BeautifulSoup
import requests
import threading

from app.HomeClass import HomeClass

OBJs = []
ThreadOBJs = []

def filterURLsHome(input_urls):

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

    homeClassLive = HomeClass(soupLive)
    homeClassWip = HomeClass(soupWip)

    data = {}
    data['url'] = url
    liveHomeDict = {}
    wipHomeDict = {}
    differenceHomeDict = {}

    # Storing Live Data
    liveHomeDict['Main Banner Links'] = homeClassLive.main_banner_links(soupLive)
    liveHomeDict['Main Banner Texts'] = homeClassLive.main_banner_text(soupLive)
    liveHomeDict['Popular Category Products'] = homeClassLive.popular_category_product(soupLive)
    liveHomeDict['Popular Category Subproducts'] = homeClassLive.popular_category_subproducts(soupLive)
    liveHomeDict['Featured Products'] = homeClassLive.get_featured_products(soupLive)
    liveHomeDict['Featured Products CTA'] = homeClassLive.get_featured_products_cta(soupLive)
    liveHomeDict['Large Content Teasers'] = homeClassLive.get_large_content_teaser(soupLive)
    liveHomeDict['Small Content Teasers'] = homeClassLive.get_smaller_content_teaser(soupLive)
    liveHomeDict['Legal Birdseed'] = homeClassLive.get_legal_birdseed(soupLive)

    # Storing Wip Data

    wipHomeDict['Main Banner Links'] = homeClassWip.main_banner_links(soupWip)
    wipHomeDict['Main Banner Texts'] = homeClassWip.main_banner_text(soupWip)
    wipHomeDict['Popular Category Products'] = homeClassWip.popular_category_product(soupWip)
    wipHomeDict['Popular Category Subproducts'] = homeClassWip.popular_category_subproducts(soupWip)
    wipHomeDict['Featured Products'] = homeClassWip.get_featured_products(soupWip)
    wipHomeDict['Featured Products CTA'] = homeClassWip.get_featured_products_cta(soupWip)
    wipHomeDict['Large Content Teasers'] = homeClassWip.get_large_content_teaser(soupWip)
    wipHomeDict['Small Content Teasers'] = homeClassWip.get_smaller_content_teaser(soupWip)
    wipHomeDict['Legal Birdseed'] = homeClassWip.get_legal_birdseed(soupWip)

    # Storing differences data

    for key, value in liveHomeDict.items():
        if key == 'Main Banner Links':  # List of URLs
            factor = True
            wipTemp = ''
            liveTemp = ''

            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    liveTemp = val
                    if "-wip" in wipHomeDict[key][idx]:
                        wipTemp = wipHomeDict[key][idx].replace("-wip", "")
                    else:
                        wipTemp = wipHomeDict[key][idx]

                    if liveTemp.strip("%20").lower() != wipTemp.strip("%20").lower():
                        factor = False

            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'

    #################################################################
        elif key == 'Popular Category Products':
            factor = True
            wipTemp = ''
            liveTemp = ''

            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    keyLive = ''
                    valLive = ''
                    for a, b in liveHomeDict[key][idx].items():
                        keyLive = a
                        valLive = b

                    keyWip = ''
                    valWip = ''
                    for a, b, in wipHomeDict[key][idx].items():
                        keyWip = a
                        valWip = b

                    # if keyLive.lower() != keyWip.lower():
                    #     print("ERRRRRROoooooooooooooooooooooRRRRR")

                    if keyLive == 'Link':
                        if "-wip" in valWip:
                            valWip = valWip.replace("-wip", "")

                    elif keyLive == 'Image Link':
                        valLive = valLive.rsplit('/', 1)[-1]
                        valWip = valWip.rsplit('/', 1)[-1]

                    if valLive.strip("%20").lower() != valWip.strip("%20").lower():
                        factor = False

            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'

    #####################################################################################3

        elif key == 'Popular Category Subproducts':
            factor = True
            wipTemp = ''
            liveTemp = ''

            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    if len(liveHomeDict[key][idx]) == 2:
                        valLive1 = ''
                        valLive2 = ''

                        valLive1 = liveHomeDict[key][idx]['Sub Product Text']
                        valLive2 = liveHomeDict[key][idx]['Sub Product Link']
                        valLive2 = valLive2.replace("-wip", "")

                        valWip1 = ''
                        valWip2 = ''

                        valWip1 = wipHomeDict[key][idx]['Sub Product Text']
                        valWip2 = wipHomeDict[key][idx]['Sub Product Link']
                        valWip2 = valWip2.replace("-wip", "")

                        if valLive1.strip("%20").lower() != valWip1.strip("%20").lower():
                            factor = False
                        if valLive2.strip("%20").lower() != valWip2.strip("%20").lower():
                            factor = False

                    elif len(liveHomeDict[key][idx]) == 1:
                        valLive = liveHomeDict[key][idx]['Sub ProductImage']
                        valWip = wipHomeDict[key][idx]['Sub ProductImage']

                        valLive = valLive.rsplit('/', 1)[-1]
                        valWip = valWip.rsplit('/', 1)[-1]

                        if valLive.strip("%20").lower() != valWip.strip("%20").lower():
                            factor = False


            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'

    ############################################################################################

        elif key == 'Featured Products':
            factor = True

            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    valLive1 = ''
                    valLive2 = ''

                    valLive1 = liveHomeDict[key][idx]['URL']
                    valLive2 = liveHomeDict[key][idx]['Image']

                    valLive1 = valLive1.replace("-wip", "")
                    valLive2 = valLive2.rsplit('/', 1)[-1]

                    valWip1 = ''
                    valWip2 = ''

                    valWip1 = wipHomeDict[key][idx]['URL']
                    valWip2 = wipHomeDict[key][idx]['Image']

                    valWip1 = valWip1.replace("-wip", "")
                    valWip2 = valWip2.rsplit('/', 1)[-1]

                    if valLive1.strip("%20").lower() != valWip1.strip("%20").lower():
                        factor = False
                    if valLive2.strip("%20").lower() != valWip2.strip("%20").lower():
                        factor = False


            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'

    ##########################################################################################################33

        elif key == "Featured Products CTA":
            factor = True
            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    valLive1 = ''
                    valLive2 = ''

                    valLive1 = liveHomeDict[key][idx]['Product_Module_CTA_text']
                    valLive2 = liveHomeDict[key][idx]['Product_Module_CTA_text_link']

                    valLive2 = valLive1.replace("-wip", "")


                    valWip1 = ''
                    valWip2 = ''

                    valWip1 = wipHomeDict[key][idx]['Product_Module_CTA_text']
                    valWip2 = wipHomeDict[key][idx]['Product_Module_CTA_text_link']

                    valWip2 = valWip1.replace("-wip", "")


                    if valLive1.strip("%20").lower() != valWip1.strip("%20").lower():
                        factor = False
                    if valLive2.strip("%20").lower() != valWip2.strip("%20").lower():
                        factor = False


            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'

    ###############################################################################################################3333
        elif key == 'Large Content Teasers':
            factor = True
            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    valLive = ''
                    valWip = ''
                    for a, b in liveHomeDict[key][idx].items():
                        if a == 'Large Content Teaser Link':
                            valLive = b.replace("-wip", "")
                            valWip = wipHomeDict[key][idx][a].replace("-wip", "")
                        else:
                            valLive = b
                            valWip = wipHomeDict[key][idx][a]

                            if valLive1.strip("%20").lower() != valWip1.strip("%20").lower():
                                factor = False
                            if valLive2.strip("%20").lower() != valWip2.strip("%20").lower():
                                factor = False

            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'



    ########################################################################################################33
        elif key == 'Small Content Teasers':
            factor = True
            if len(liveHomeDict[key]) != len(wipHomeDict[key]):
                factor = False
            else:
                for idx, val in enumerate(liveHomeDict[key]):
                    valLive = ''
                    valWip = ''
                    for a, b in liveHomeDict[key][idx].items():
                        if a == 'Smaller Content Teaser Link':
                            valLive = b.replace("-wip", "")
                            valWip = wipHomeDict[key][idx][a].replace("-wip", "")
                        else:
                            valLive = b
                            valWip = wipHomeDict[key][idx][a]

                            if valLive1.strip("%20").lower() != valWip1.strip("%20").lower():
                                factor = False
                            if valLive2.strip("%20").lower() != valWip2.strip("%20").lower():
                                factor = False

            if factor is True:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'



        else:
            if value == wipHomeDict[key]:
                differenceHomeDict[key] = 'Pass'
            else:
                differenceHomeDict[key] = 'Fail'



    data['liveHomeDict'] = liveHomeDict
    data['wipHomeDict'] = wipHomeDict
    data['differenceHomeDict'] = differenceHomeDict

    OBJs.append(data)
