
import bs4
import requests
from bs4 import BeautifulSoup
jop_Titlee = []
Job_posterr = []
job_Descriptionn = []
job_Locationn = []
try:
    url='https://www.behance.net/joblist?tracking_source=nav20'
    HTMLpage= requests.get(url)
    soup = bs4.BeautifulSoup(HTMLpage.content, "html.parser")
    if (HTMLpage.status_code==200):
    #
        # print(soup.contents)
        Job_poster=soup.findAll("p",{"class":"JobCard-company-GQS"})
        job_Location=soup.findAll("p",{"class":"JobCard-jobLocation-sjd"})
        jop_Title=soup.find_all("h3",{"class":"JobCard-jobTitle-LS4"})
        job_Description=soup.findAll("p",{"class":"JobCard-jobDescription-SYp"})

        print("Welcome to my project :) we will scraping in behance site for freelancer jop there some about for it : ")
        for index,value in enumerate(Job_poster): #any list because the same size
            print()
            print(f"jop numper is :{index+1}")
            jop_Titlee.append(print(f'jop_Titlee is : { jop_Title[index].text}'))
            Job_posterr.append(print(f"Job_poster is : {value.text}"))
            job_Descriptionn.append(print(f"job_Description is :{job_Description[index].text}"))
            job_Locationn.append(print(f"job_Location is :{job_Location[index].text}"))

    elif(HTMLpage.status_code==404):
        print(f" NOT FONUD :Error {HTMLpage}")
    else:
        print(f"Website response is  {HTMLpage}")
except:
  print(" Obs :( \n There is an Error\n Check the code again\nmake sure you are connected to the internet ")


























