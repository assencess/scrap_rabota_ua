# scrap_rabota_ua
Scrapper for rabota.ua
This scrapper can be used for finding jobs on site rabota.ua
Example how to use it:
# scrapper rabota_ua
ua = UtilsRabotaUa(PROF, FIRST_PAGE, LAST_PAGE)
jobs = list() # create a list for saving jobs
for url in ua:    
  html = urlopen(url)    
  soup = BeautifulSoup(html, "html.parser")    
  list_of_jobs = soup.findAll("h3", {"class": "fd-beefy-gunso f-vacancylist-vacancytitle"})    
  for job in list_of_jobs:        
    job_title = str(job.a.string) # for crop "\n\r" and others. see below                
    
    # this is for "None" values(a hot vacancy)        
    if len(job_title) >= 5:            
      jobs.append("{}({})".format(job_title.strip(), URL+job.a['href']))
      
for job in jobs:
  print(job)
