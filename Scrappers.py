
import requests
from bs4 import BeautifulSoup
import json
import tqdm



#NAVAL SITE
 
def Naval():

	links = ['https://nav.al/multiverse','https://nav.al/error', 'https://nav.al/pessimism', 'https://nav.al/expand', 'https://nav.al/conjectural', 'https://nav.al/consensus', 'https://nav.al/the-aging-entrepreneur']
	content=''
	dic={}
	list=[]
	for link in links:
		z=''
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser')
		l = soup.find_all('div', {'class':'content'})[0].find_all('p') 
		titl = soup.find('h1', {'class':'blog-title'})
		title=titl.text


		for i in l:
			z+=content + i.text
			
		dic={
			'author':'Naval',
			'title':title,
			'link':link,
			'content': z,
			}


		list.append(dic)


	json.dump(list,open('ScrapedData/Naval.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)



def BluntedBuddha():
	links = ['https://bluntedbuddha.com/blog-1/2021/1/16/part-2-unity-of-consciousness','https://bluntedbuddha.com/blog-1/2020/8/20/duality-of-consciousness1',]
	content=''
	dic={}
	list=[]
	for link in links:
		z=''
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser')
		l = soup.find_all('div',{'class':'sqs-block-content'})
		k = soup.find('div', class_= 'newsletter-form-wrapper newsletter-form-wrapper--layoutFloat newsletter-form-wrapper--alignCenter')
		k.decompose()
		titl = soup.find('h1', {'class':'BlogItem-title'})
		t=titl.text
		for x in l:
			z+=content+x.text
			
			
		dic={
			'author':'BluntedBuddha',
			'title':t,
			'link':link,
			'content': z,
			}


		list.append(dic)


	json.dump(list,open('ScrapedData/BluntedBuddha.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)



def LifeMathMoney():
	links = ['https://lifemathmoney.com/advice-to-broke-third-world-student-with-financial-problems-due-to-lockdown/','https://lifemathmoney.com/management-lessons-from-the-ramayana-teachings-for-kings/','https://lifemathmoney.com/are-all-the-sacrifices-worth-it/', 'https://lifemathmoney.com/nothing-changes-if-nothing-changes/']
	content=''
	dic={}
	list=[]
	for link in links:
		z=''
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser')
		l = soup.find_all('div',{'class':'td-post-content td-pb-padding-side'})
		titl = soup.find('h1', {'class':'entry-title'})
		t=titl.text
		for x in l:
			z+=content+x.text
			

		dic={
			'author':'Harsh Strongman',
			'title':t,
			'link':link,
			'content': " ".join(z.split("\n")),
			}

		list.append(dic)
	json.dump(list,open('ScrapedData/LifeMathMoney.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)



def TinkeredThinking():
	links = ['https://www.tinkeredthinking.com/index.php?id=1129','https://www.tinkeredthinking.com/index.php?id=340','https://www.tinkeredthinking.com/index.php?id=703', 'https://www.tinkeredthinking.com/index.php?id=722']
	content=''
	dic={}
	list=[]
	for link in links:
		z=''
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser')
		l = soup.find_all('div',{'class':'raw-post'})
		titl = soup.find('a', {'class':'permalink-title'})
		t=titl.text
		for x in l:
			z+=content+x.text
			

		dic={
			'author':'TinkeredThinking',
			'title':t,
			'link':link,
			'content': " ".join(z.split("\n")),
			}

		list.append(dic)
	json.dump(list,open('ScrapedData/TinkeredThinking.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)



def PaulGraham():

	links = ['http://www.paulgraham.com/newideas.html', 'http://www.paulgraham.com/vb.html',
	'http://www.paulgraham.com/selfindulgence.html',
	'http://www.paulgraham.com/13sentences.html',
	'http://www.paulgraham.com/ecw.html', 'http://www.paulgraham.com/useful.html']
	content=''
	dic={}
	list=[]
	for link in links:
		z=''
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser') 
		l = soup.tr

		for x in l:
			z+=content+x.text
			
		dic={
			'author':'Paul Graham',
			'title':soup.find('title').text,
			'link':link,
			'content': " ".join(z.split("\n")),
			}

		list.append(dic)
	json.dump(list,open('ScrapedData/PaulGraham.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)



def JamesClear():

	links = ['https://jamesclear.com/giving-up', 'https://jamesclear.com/saying-no', 'https://jamesclear.com/creative-thinking', 'https://jamesclear.com/dont-start-from-scratch', 'https://jamesclear.com/shoshin']
	content=''
	dic={}
	list=[]
	for link in links:
		z=''
		html = requests.get(link)
		soup = BeautifulSoup(html.text, 'html.parser')
		l = soup.find('div', {'class':'page__content page-content-style'}).find_all('p')
		titl = soup.find('div', {'class':'page__header'}).find('h1').text

		for x in l:
			z+=content+x.text
			
		with open('f.txt','w') as f:
			f.write(z)
		dic={
			'author':'James Clear',
			'title':titl,
			'link':link,
			'content': " ".join(z.split("\n")),
			}

		list.append(dic)
	json.dump(list,open('ScrapedData/JamesClear.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)



funcs = [Naval, JamesClear, BluntedBuddha, LifeMathMoney, TinkeredThinking, PaulGraham]

for func in tqdm.tqdm(funcs):
	# print(func)
	func()

print('DONE')