# !pip install flask-ngrok
# !pip install -q transformers
# !pip install pymongo[srv]
# !pip install tqdm
# !pip install dnspython==2.0.0

from transformers import pipeline
summarizer = pipeline('summarization')


import math
import psutil
import gc



def summ(context,lb=5,ub=5,lbm=2,ubm=2):
  if type(context) == list:
   context = ' '.join(context)
  return [summarizer(context,min_length=(math.ceil(len(context.split(' '))/lb)*lbm),max_length=(math.ceil(len(context.split(' '))/ub)*ubm))[0].get('summary_text')]
  gc.collect()



def summ_for_long(text,lb=4,ub=5,lbm=1,ubm=2):

  k=[]

  v=text

  v = v+'.' if not v.endswith('.') else v+''

  L = 600

  for i in range(math.floor(len(v.split(' '))/L)):
    c1 = v.split(' ')[L*i:L*(i+1)]
    c2 = v.split(' ')[L*(i+1):L*(i+2)]
    while not c1[-1].endswith('.'):
      # print(c1[-1])
      c1.append(c2[0])
      del(c2[0])
      
    k.append(summ(c1,lb=lb,ub=ub,lbm=lbm,ubm=ubm)[0])



  return k

import json
import pymongo
from tqdm.notebook import tqdm


client = pymongo.MongoClient("mongodb+srv://Pranav:Pranavpatela1-kop@cluster0.fn26y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.blog_project
summaries = db.summaries



BLOGS = ['TinkeredThinking', 'Naval', 'LifeMathMoney', 'BluntedBuddha', 'PaulGraham', 'JamesClear'] 


with open('combined_summaries.json','w'):
  for blog in tqdm(BLOGS):
    collection = json.load(open(f'{blog}.json','r'))
    for document in tqdm(collection):
      content = document['content']

      try:
        summary = summ(content)
      except Exception as e:
        summary = summ_for_long(content)

      document['content'] = " ".join(summary)
      print(document)
      summaries.insert_one(document)