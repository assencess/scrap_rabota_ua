#!/usr/bin/env python3
from scrapper_constants import *

class UtilsRabotaUa():
    """
    This is helper class for main program. Aim of this class
    make urls as iterable objects for comfortable and 
    readable source code of main program.
    """
    _job_name = PROF # Search query | All regions
    _page_obj = FIRST_PAGE # With what page need to start
    _last_page = LAST_PAGE # How many pages need to scrap

    def __init__(self, job_name=PROF, page=FIRST_PAGE, pages=LAST_PAGE):
        self._job_name = job_name
        self._page_obj = page
        self._last_page = pages

    def make_url(self, page_num=0):
        """
        This is a helper method for creating url for page-by-page
        scrapping. Method takes one arguments, page_num - numbers
        of page what need to scrap.
        """
        url = "https://rabota.ua/jobsearch/vacancy_list?keyWords={}&pg={}"\
            .format(self._job_name, str(page_num))

        return url

    def __iter__(self):
        return self

    def __next__(self):
        url = ""
        if self._page_obj <= self._last_page:
            url = self.make_url(self._page_obj)
            self._page_obj += 1

            return url
        elif self._page_obj >= self._last_page:
            raise StopIteration

if __name__ == "__main__":
    """ an example how to use it """
    ua = UtilsRabotaUa("java", 1, 2)
    for p in ua:
        print(p)

