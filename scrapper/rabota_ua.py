#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
import webbrowser as wb
# my own files
from scrapper_utils import UtilsRabotaUa
from scrapper_constants import *

ua = UtilsRabotaUa(PROF, FIRST_PAGE, LAST_PAGE)
jobs_title = list() # create a list for job's titles
jobs_urls = list() # create a list for job's URLs

for url in ua:
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    list_of_jobs = soup.findAll("h3", 
        {"class": "fd-beefy-gunso f-vacancylist-vacancytitle"})

    for job in list_of_jobs:
        job_title = str(job.a.string) # for crop "\n\r" and others. see below
        
        # this is for avoid "None" values(a hot vacancy)
        if len(job_title) >= 5:
            jobs_title.append(job_title.strip()) # crop and add job for list
            jobs_urls.append(URL+job.a['href']) # add "base" url for tag' arg

for i in range(0, len(jobs_urls)):
    title = jobs_title[i]
    url = jobs_urls[i]
    print("{}) {}({})".format(i, title, url))

# this block of code ask user of intresting job(a number of job in list)
# and then open new tab in browser (now is "firefox")
num = int(input("Please, enter a number: "))
url = jobs_urls[num]
print("Openning "+url)
wb.get('firefox').open_new_tab(url)

