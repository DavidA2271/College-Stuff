''' Retrieves staff info from the Shepherd Department Staff website page '''

import os
import requests
from bs4 import BeautifulSoup, Tag
import pandas
    

class web_scraper:
    ''' main class in charge of running the web scraper '''

    site = 'https://www.shepherd.edu/'
    staff = '/staff/'
    s_mems = []
    def scrape(self, dept):

        url = self.site + dept + self.staff
        self.rh = response_handler(url)
        if not self.rh.check_response():
            print('Invalid URL')
            return
        self.soup = bsoup(self.rh)
        staff = self.soup.get_staff()
        for st in staff:
           self.s_mems.append(staff_member(st).data)
        self.fh = file_handler()
        self.fh.save_data(self.s_mems)
        self.fh.read_data()
        
    
class file_handler:
    ''' class in charge of reading and writing files '''

    def __init__(self) -> None:
        cwd = os.getcwd()
        self.path = os.path.join(cwd, 'staff_info.csv')
    
    def save_data(self, data):
        ''' uses pandas to save a dataframe of staff information to a csv file '''

        df = pandas.DataFrame.from_records(data)
        df.to_csv(path_or_buf=self.path, index=False)

    def read_data(self):
        ''' reads a csv file into a pandas dataframe and prints it '''

        df = pandas.read_csv(filepath_or_buffer=self.path)
        print(df)


class response_handler:
    ''' uses the requests package to get a url request '''

    def __init__(self, url: str) -> None:
        self.get_response(url)

    def get_response(self, url: str):
        ''' gets a response from a url '''
        self.response = requests.get(url, allow_redirects=False)

    def check_response(self) -> bool:
        ''' checks if the response has a valid code 

            specifically checks for code 301. code 301 is a redirection code. no matter how invalid the url is, since it ends with /staff, the Shepherd website always redirects it and never gives a 404 not found error
        '''
        if self.response.status_code == 301:
            return False
        content_type = self.response.headers['Content-Type']
        return 'text/html' in content_type


class bsoup(BeautifulSoup):
    ''' inherits from BeatifulSoup class. adds the get_staff method '''
    def __init__(self, rh: response_handler) -> None:
        super().__init__(rh.response.text, features='html.parser')
    
    def get_staff(self):
        ''' returns a ResultSet of all staff-item objects in the html file '''
        return self.findAll('div', {'class' : 'staff-item'})
    

class staff_member:
    ''' container for data in the staff-item objects '''
    def __init__(self, obj: Tag) -> None:
        self.hdata = obj.table.find_all('tr')
        self.data = {}
        self.setup()

    def setup(self):
        ''' goes through the rows in the staff-item table and adds them to a dictionary '''
        size = len(self.hdata)
        for i in range(size):
            dat = self.hdata[i]
            if i == 0:
                val = self.get_links(dat.h2)
                self.data['Name'] = val
            elif i == size - 1:
                val = self.get_links(dat)
                self.data['Bio'] = val
            elif dat.th.text == 'Email':
                key = dat.th.text.strip()
                val: str = dat.td.text.strip()
                new_val = val.split('\t', 1)[0]
                self.data[key] = new_val
            else:
                key = dat.th.text.strip()
                val = self.get_links(dat.td)
                self.data[key] = val
    
    def get_links(self, dat: Tag) -> str:
        ''' adds embeded links to the end of the string '''
        links = dat.find_all('a', href=True)
        text = dat.text.strip()
        for link in links:            
            l = link['href']
            text += f' {l};'
        return text
    

if __name__ == '__main__':
    input = input('Type in a department:   ')
    ws = web_scraper()
    ws.scrape(input)
