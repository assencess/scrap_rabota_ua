#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
# my files
from scrapper_utils import UtilsRabotaUa
from scrapper_constants import *

ua = UtilsRabotaUa(PROF, FIRST_PAGE, LAST_PAGE)
jobs = list() # create a list for saving jobs

for url in ua:
    html = urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    list_of_jobs = soup.findAll("h3", 
        {"class": "fd-beefy-gunso f-vacancylist-vacancytitle"})

    for job in list_of_jobs:
        job_title = str(job.a.string) # for crop "\n\r" and others. see below
        
        # this is for "None" values(a hot vacancy)
        if len(job_title) >= 5:
            jobs.append("{}({})".format(job_title.strip(), URL+job.a['href']))

for job in jobs:
    print(job)

