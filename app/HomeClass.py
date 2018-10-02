

class HomeClass(object):
    def __init__(self, soup):
        self.soup = soup

    def get_masthead(self, soup):   # Modified
        mainlist = []
        maindict = dict()
        MastHead = soup.find('div', {'class': 'main-nav-section hidden-xs hidden-sm'})
        if MastHead:
            head_links = MastHead.findAll("li")

            for link in head_links:
                maindict['text'] = link.a.get_text().strip()
                maindict['url'] = link.a['href'].strip()
                mainlist.append(maindict)
        return mainlist

    def main_banner_links(self, soup):  # Modified
        mainlist = []
        banner_link = soup.find('ul', {'class': 'slides'})
        if banner_link:
            banner_sub_link = banner_link.findAll('li')
            for banner in banner_sub_link:
                banner_url = banner.a['href'].strip()
                mainlist.append(banner_url)
        return mainlist

    def main_banner_text(self, soup):
        mainlist = []
        banner_title_links = soup.findAll('div', {'class': 'item-caption-wrapper'})

        for banner_title in banner_title_links:
            banner_title_h2 = banner_title.h2.get_text().strip()
            mainlist.append(banner_title_h2)
        return mainlist

    def popular_category_product(self, soup):
        mainlist = []
        Feature_Image_Label = soup.findAll("div", {"class": "featured-product-container col-lg-2 col-md-2 col-sm-2 col-xs-6"})
        for Each_Label in Feature_Image_Label:
            Product_Name = Each_Label.h4.get_text().strip().lower()
            Anchor_Links = Each_Label.findAll('a', href=True)
            IMG_Src = Each_Label.findAll('img')
            maindict = dict()
            maindict['Product Name'] = Product_Name
            if maindict not in mainlist:
                mainlist.append(maindict)
            maindict = dict()
            for Links in Anchor_Links:
                maindict['Link'] = Links.get('href')
                if maindict not in mainlist:
                    mainlist.append(maindict)
            maindict = dict()

            for Src in IMG_Src:
                try:
                    maindict['Image Link'] = Src['data-original']
                    if maindict not in mainlist:
                        mainlist.append(maindict)
                except:
                    pass

        return mainlist

    def popular_category_subproducts(self, soup):
        mainlist = []
        SubProductLable1 = soup.findAll("div",{"class": "strip-tooltip hide"})
        for SubProductLableee in SubProductLable1:
            SubProductLable = SubProductLableee.findAll('div',{'class':'col-xs-6'})
            for each_lable in SubProductLable:
                All_a_Links = each_lable.findAll('a', href=True)
                All_IMG_Src = each_lable.findAll('img')
                maindict = dict()
                for each_link in All_a_Links:
                    Sub_Product = each_link.get_text().strip()
                    Sub_Product_link = each_link['href']
                    # Sub_Product_Img_link = each_link('img')['src']
                    maindict['Sub Product Text'] = Sub_Product
                    maindict['Sub Product Link'] = Sub_Product_link
                    # maindict['Sub ProductImage'] = Sub_Product_Img_link
                    if maindict not in mainlist:
                        mainlist.append(maindict)
                maindict = dict()
                for each_img in All_IMG_Src:
                    Sub_Product_Img_link = each_img['src']
                    maindict['Sub ProductImage'] = Sub_Product_Img_link
                    if maindict not in mainlist:
                        mainlist.append(maindict)
        return mainlist

    def get_featured_products(self, soup):
        mainlist = []
        Feature_Products_Module1 = soup.findAll("div", {'data-testid': 'featured_category_module'})
        for feature in Feature_Products_Module1:
            Feature_Products_Module = feature.findAll("div", {'class': 'feature-image'})
            maindict = dict()
            for each_module in Feature_Products_Module:
                each_module_url = each_module.a['href']
                each_module_img = each_module.img['data-original']
                maindict['URL'] = each_module_url
                maindict['Image'] = each_module_img
                if maindict not in mainlist:
                    mainlist.append(maindict)
        return mainlist

    def get_featured_products_cta(self, soup):
        mainlist = []
        Feature_Products_Module = soup.findAll("div", {'data-testid': 'featured_category_module'})
        for feature in Feature_Products_Module:
            Feature_Product_Module_CTA = feature.findAll('a', {'data-testid': 'featured_category_module_cta'})
            maindict = dict()
            for each_CTA in Feature_Product_Module_CTA:
                Feature_Product_Module_CTA_text = each_CTA.get_text()
                Feature_Product_Module_CTA_text_link = each_CTA['href']
                maindict['Product_Module_CTA_text'] = Feature_Product_Module_CTA_text
                maindict['Product_Module_CTA_text_link'] = Feature_Product_Module_CTA_text_link
                mainlist.append(maindict)
        return mainlist

    def get_large_content_teaser(self, soup): # Modified
        mainlist = []
        larger_content_teasers = soup.find('div', {'class': 'row module2 '})
        if larger_content_teasers:
            larger_content_teasers_a = larger_content_teasers.findAll('a')
            larger_content_teaser_text = larger_content_teasers.findAll('div',{'class':'caption overlay'})
            for each_teaser in larger_content_teasers_a:
                maindict = dict()
                c_href = each_teaser['href']
                maindict['Large Content Teaser Link'] = c_href
                if maindict not in mainlist:
                    mainlist.append(maindict)
            maindict = dict()
            try:
                cta_teasers_text = larger_content_teasers.find('div',{'class': re.compile('cta btn hidden-xs.*')}).text
                if cta_teasers_text:
                    maindict['Large Content Teaser CTA Text'] = cta_teasers_text
                else:
                    maindict['Large Content Teaser CTA Text'] = ""
                if maindict not in mainlist:
                    mainlist.append(maindict)
            except:
                maindict['Large Content Teaser CTA Text'] = ""
                if maindict not in mainlist:
                    mainlist.append(maindict)

            for texts in larger_content_teaser_text:
                maindict = dict()
                banner_text = texts.find('h5').text
                maindict['Large Content Teaser Banner Text'] = banner_text
                if maindict not in mainlist:
                    mainlist.append(maindict)

        return mainlist

    def get_smaller_content_teaser(self, soup): # Modified
        mainlist = []
        bottom_chk = soup.find('div', {'class': 'row module4'})
        if bottom_chk:
            bottom_divs = bottom_chk.findAll('div', {'class': 'caption'})
            for each_Teaser in bottom_divs:
                maindict = dict()
                link_Teaser = each_Teaser.a['href']
                text_Teaser = each_Teaser.get_text().strip()
                maindict['Smaller Content Teaser Link'] = link_Teaser
                maindict['Smaller Content Teaser Text'] = text_Teaser
                if maindict not in mainlist:
                    mainlist.append(maindict)
        return mainlist

    def get_legal_birdseed(self, soup): # Modified
        maindict = dict()
        obj = soup.find('div',{'class':'legal-birdseed legal-text'})
        if obj:
            birdseed_text = obj.text
            maindict['Birdseed Text'] = birdseed_text
        return maindict

    def main_function(self):
        home_page_data = dict()
        home_page_data['Main Banner Link'] = self.main_banner_links(self.soup)
        home_page_data['Main Banner Text'] = self.main_banner_text(self.soup)
        home_page_data['Popular Category Product'] = self.popular_category_product(self.soup)
        home_page_data['Popular category subproduct'] = self.popular_category_subproducts(self.soup)
        home_page_data['Featured Product'] = self.get_featured_products(self.soup)
        home_page_data['Featured Product CTA'] = self.get_featured_products_cta(self.soup)
        home_page_data['Large Content Teaser'] = self.get_large_content_teaser(self.soup)
        home_page_data['Small Content Teaser'] = self.get_smaller_content_teaser(self.soup)
        home_page_data['Legal Birdseed'] = self.get_legal_birdseed(self.soup)

        return home_page_data

