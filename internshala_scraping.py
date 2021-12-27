from bs4 import BeautifulSoup
import pandas as pd
import requests

job_title = []
company_name=[]
location=[]
start_date=[]
duration=[]
stipends=[]



res = requests.get('https://internshala.com/internships/Analytics')
soup = BeautifulSoup(res.text, 'html.parser')
allposts=soup.findAll(True,{'class':"internship_meta"})
#print(allposts)

for post in allposts:
    job_title.append(post.find('a').text)
    company_name.append(post.find('a',{'class':'link_display_like_text'}).text.strip())
    location.append(post.find('a', {'class': 'location_link'}).text.strip())
    duration.append(post.find('span').text[1:])
    stipends.append(post.find('span',{'class':'stipend'}).text)
    start_date.append(post.find('span',{'class':'start_immediately_desktop'}).text)

df = pd.DataFrame({'Job title':job_title,'Company name':company_name,'loaction':location,'start date':start_date,'Duration':duration,'stipends':stipends})
print(df.head())



