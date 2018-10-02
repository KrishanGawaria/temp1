
class DealsClass(object):
    def __init__(self, soup):
        self.soup = soup

    def get_intel_banner(self, soup):   # Modified
        mainlist = []
        maindict = dict()
        banner_section = soup.find('section', {'id':'agreement-container'})
        banner_text_row = banner_section.find('div',{'class': 'display-table-row'})
        banner_text = banner_text_row.text
        maindict['banner_text'] = banner_text.strip()
        banner_cta = banner_section.find('div', {'class':'display-table-column agreement-logo-pad'})
        if banner_cta:
            banner_cta_link = banner_cta.find('a')
            maindict['Banner CTA'] = banner_cta_link.get('href')
            banner_image_link = banner_cta.find('img')
            maindict['Banner Image'] = banner_image_link['src']
        else:
            maindict['Banner CTA'] = ''
            maindict['Banner Image'] = ''
        mainlist.append(maindict)
        return mainlist

    def get_piglet(self, soup):
        mainlist = []
        piglet_section = soup.find('div',{'class':'tabs-carousel'})
        image_section = piglet_section.findAll('div',{'class':'display-table-xs table-layout-fixed-xs width-100-percent'})
        for img in image_section:
            images = img.findAll('img')
            texts = img.findAll('h4')
            for i in images:
                maindict = dict()
                maindict['Piglet Image'] = i['data-original']
                mainlist.append(maindict)
            for t in texts:
                maindict = dict()
                maindict['Piglet Text'] = t.text
                mainlist.append(maindict)
        return mainlist

    def main_function(self):
        deals_page_data = dict()
        deals_page_data['Intel Banner'] = self.get_intel_banner(self.soup)
        deals_page_data['Piglet Information'] = self.get_piglet(self.soup)
        return deals_page_data
