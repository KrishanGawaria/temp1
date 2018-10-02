# import requests, threading, re

class PdClass(object):
    def __init__(self, soup):
        self.soup = soup

    def get_baselang(self):
        try:
            baselang = self.soup.find("meta", {"name": "LANGUAGE"})['content']
        except:
            baselang = "Not Present"

        return baselang

    def get_browsertitle(self):
        try:
            browserTitle = self.soup.title.string.strip()
        except:
            browserTitle = "Not Present"

        return browserTitle

    def get_metaDescription(self):
        try:
            metaDescription = self.soup.find("meta", {"name": "DESCRIPTION"})['content']
        except:
            metaDescription = "Not Present"

        return metaDescription

    def get_metaKeywords(self):
        try:
            metaKeywords = self.soup.find("meta", {"name": "KEYWORDS"})['content']
        except:
            metaKeywords = "Not Present"

        return metaKeywords

    def get_breadcrumb(self):
        breadcrumb_list = []
        try:
            div = self.soup.find('ol', {'class': 'breadcrumb'})
            list = div.find_all('li')
            for x in list:
                y = x.text.strip()
                breadcrumb_list.append(y)
        except:
            breadcrumb_list.append("Not Present")

        return breadcrumb_list

    def get_pagetitle(self):
        try:
            pageTitle = self.soup.find('h1', {'id': 'sharedPdPageProductTitle'}).text.strip()
        except:
            pageTitle = "Not Present"

        return pageTitle

    def get_cta(self):
        try:
            CTA = self.soup.find('a', {'class': re.compile('btn btn-success.*')})
            CTA1 = CTA.text.strip
        except:
            CTA1 = "Not Present"

        return CTA1

    def get_herotitle(self):
        try:
            heroTitle1 = self.soup.find('div', {'class': 'col-sm-7 col-md-5 povw-hero-description'})
            heroTitle = heroTitle1.find('h2').text.strip()
        except:
            try:
                heroTitle1 = self.soup.find('div', {'class': 'xs-text-centered'})
                heroTitle = heroTitle1.find('h2').text.strip()
            except:
                heroTitle = "Not Present"

        return heroTitle

    def get_herodescription(self):
        try:
            heroDescription1 = self.soup.find('div', {'class': 'col-sm-7 col-md-5 povw-hero-description'})
            heroDescription = heroDescription1.find('p').text.strip()
        except:
            try:
                heroDescription1 = self.soup.find('div', {'class': 'xs-text-centered'})
                heroDescription = heroDescription1.find('p').text.strip()
            except:
                heroDescription = "Not Present"

        return heroDescription

    def get_pricing(self):
        try:
            pricing = self.soup.find('div', {'class': 'col-sm-7 col-md-5 povw-hero-description'})
            price = pricing.find('h4').text.strip()
        except:
            price = "Not Present"

        return price

    def get_heroimagelink(self):
        try:
            heroImage = self.soup.find('section', {'id': 'hero-container'})
            heroILink = heroImage.find('img')
            heroImageLink = heroILink.attrs['src']
        except:
            heroImageLink = "Not Present"

        return heroImageLink
    def get_herovideo(self):
        heroVideo = ""
        try:
            hero_video = self.soup.find('section', {'id': 'hero-container'})
            try:
                video = hero_video.find('input').attrs
                vcode = video['data-code']
                heroVideo = 'http://cf.c.ooyala.com/' + vcode + '/DOcJ-FxaFrRg4gtDEwOjYyOjBhOyD0Uk'
            except:
                pass
        except:
            heroVideo = "Not Present"

        return heroVideo

    def get_techspecs(self):
        tech_list = []
        try:
            techspecs_parent_div = self.soup.find("div", {"id": "techspecs"})
            tech_specs_div = techspecs_parent_div.find_all("div", {'class': 'specs'})
            if tech_specs_div:
                for tech_spec in tech_specs_div:
                    tech_specs = re.sub('\n+', '\n', str(tech_spec.text.strip()))
                    tech_specs = tech_specs.split('\n')
                    if tech_specs is not "":
                        tech_list.append(tech_specs[0])
                        tech_list.append(tech_specs[1])
            else:
                tech_specs_div = techspecs_parent_div.find_all("div", {'class': 'povw-spec'})
                for tech_spec in tech_specs_div:
                    tech_specs = re.sub('\n+', '\n', str(tech_spec.text.strip()))
                    tech_specs = tech_specs.split('\n')
                    if len(tech_specs) == 2:
                        tech_list.append(tech_specs[0])
                        tech_list.append(tech_specs[1])
                    else:
                        tech_list.append(tech_specs[0])

        except:
            tech_list.append("Not Present")

        return tech_list

    def get_overview(self):
        overview_list = []
        try:
            features_div = self.soup.find("div", {"id": "features"})
            features = features_div.findAll("div", {"class": re.compile('row xs-pad-offset-15.*')})
            for feature in features:
                final = re.sub('\n+', '\n', str(feature.get_text().strip()))
                check = re.compile("window._ooyalaVersion.*")
                result = check.findall(final)
                if final:
                    if not result:
                        overview_list.append(final)
        except:
            overview_list.append("Not Present")

        return overview_list

    def get_awards(self):
        awards_list = []
        try:
            awardsdiv = self.soup.find('div', {'id': 'awards'})
            awards = awardsdiv.find_all('p')
            for award in awards:
                final = re.sub('\n+', '\n', str(award.get_text().strip()))
                if final:
                    if final not in awards_list:
                        awards_list.append(final)
        except:
            awards_list.append("Not Present")

    def get_services(self):
        service_list = []
        try:
            servicesdiv = self.soup.find('div', {'id': 'services'})
            services = servicesdiv.findAll("div", {"class": re.compile('row xs-pad-offset-15.*')})
            for service in services:
                final = re.sub('\n+', '\n', str(service.get_text().strip()))
                service_list.append(final)
        except:
            service_list.append("Not Present")

    def get_support(self):
        support_list = []
        try:
            supportdiv = self.soup.find('div', {'id': 'support'})
            support = supportdiv.findAll("div", {"class": re.compile('row xs-pad-offset-15.*')})
            for sup in support:
                final = re.sub('\n+', '\n', str(sup.get_text().strip()))
                support_list.append(final)
        except:
            support_list.append("Not Present")