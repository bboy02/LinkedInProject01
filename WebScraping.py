import requests 
import bs4 
import time
print("Enter the skill you want to neglect")
unfamiliar_skill=input(">")
print(f"skill to be neglected is {unfamiliar_skill}")

def job_function():
    url = 'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation='
    request_result=requests.get( url ) 



    # Creating soup from the fetched request 
    soup = bs4.BeautifulSoup(request_result.text, "lxml") 
    job_list = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for jobs in job_list:
        published_date=jobs.find('span',class_='sim-posted').span.text
        
        
        if '1' in published_date:
            job =jobs.find('h3',class_='joblist-comp-name').text.strip()
            link=jobs.header.h2.a['href']
            skills_required=jobs.find('span',class_='srp-skills').text.replace(' ','').strip()
            if unfamiliar_skill not in skills_required:    
                    print(f"company name: {job}")
                    print(f"Skillset: {skills_required}")
                    print(f"posted on: {published_date}")
                    print(f"link to apply: {link}")
                    print(' ')

if __name__ =="__main__":
     while True:
          job_function()
          time.sleep(600)
