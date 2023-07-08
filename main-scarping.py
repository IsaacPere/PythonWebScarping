from bs4 import BeautifulSoup as souping_mechanism
import requests as scarping_mechanism_modules

url_website = scarping_mechanism_modules.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=").text
souping_the_website = souping_mechanism(url_website, 'lxml')
find_the_jobs = souping_the_website.find('li', class_ = "clearfix job-bx wht-shd-bx")
name_of_company = find_the_jobs.find('h3', class_ = 'joblist-comp-name').text
jobs_requirement_skills = find_the_jobs.find('span', class_ = "srp-skills").text.replace(' ', '')
jobs_published_date = find_the_jobs.find('span', class_ = "sim-posted").text


print(f'''
	Company Name: {name_of_company}
	Required Skills: {jobs_requirement_skills}
	Job Pulibshed Date : {jobs_published_date}
	'''
)
 