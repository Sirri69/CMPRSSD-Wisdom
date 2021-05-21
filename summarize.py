import json

import requests

API_TOKEN = 'api_XLhAFCPVrKgPpWELpHMJsHVEVOiyjnZslE'

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

# data = query(
#     {
#         "inputs": "The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side. During its construction, the Eiffel Tower surpassed the Washington Monument to become the tallest man-made structure in the world, a title it held for 41 years until the Chrysler Building in New York City was finished in 1930. It was the first structure to reach a height of 300 metres. Due to the addition of a broadcasting aerial at the top of the tower in 1957, it is now taller than the Chrysler Building by 5.2 metres (17 ft). Excluding transmitters, the Eiffel Tower is the second tallest free-standing structure in France after the Millau Viaduct.",
#     }
# )

# print(data)



import math

import gc



def summ(context,lb=4,ub=5,lbm=1,ubm=2):
  if type(context) == list:
   context = ' '.join(context)
  # return [summarizer(context,min_length=(math.ceil(len(context.split(' '))/lb)*lbm),max_length=(math.ceil(len(context.split(' '))/ub)*ubm))[0].get('summary_text')]
  return query({
		"inputs": context,
		"options": {"wait_for_model":True},
		"parameters": {
			"min_length": (math.ceil(len(context.split(' '))/lb)*lbm),
			"max_length": (math.ceil(len(context.split(' '))/ub)*ubm)
		}
	})






def summ_for_long(text,lb=4,ub=5,lbm=1,ubm=2):

  k=[]

  v=text

  v = v+'.' if not v.endswith('.') else v+''

  L = 600

  for i in range(math.floor(len(v.split(' '))/L)):
    # L = 200
    print(f'i {i}')
    c1 = v.split(' ')[L*i:L*(i+1)]
    c2 = v.split(' ')[L*(i+1):L*(i+2)]
    while not c1[-1].endswith('.'):
      print(c1[-1])
      c1.append(c2[0])
      del(c2[0])
      
    # k.append(summ(c1,lb=lb,ub=ub,lbm=lbm,ubm=ubm)[0].get('summary_text'))
    print(summ(c1,lb=lb,ub=ub,lbm=lbm,ubm=ubm))

    # k.append(c2)


  return k



context = '''
Wealth is assets that earn while you sleep

Naval is a prolific tech investor and founder of AngelList

Nivi: You probably know Naval from his Twitter account.

We’re going to talk about his tweetstorm, “How To Get Rich (without getting lucky).” We’ll go through most of the tweets in detail, give Naval a chance to expand on them and generally riff on the topic. He’ll probably throw in ideas he hasn’t published before.

Naval’s the co-founder of AngelList and Epinions. He’s also a prolific tech investor in companies like Twitter, Uber and many more.

I’m the co-founder of AngelList with Naval. And I co-authored the Venture Hacks blog with him back in the day.


Naval: The “How to Get Rich” tweetstorm definitely hit a nerve and went viral. A lot of people say it was helpful and reached across aisles.

People outside of the tech industry—people in all walks of life—want to know how to solve their money problems. Everyone vaguely knows they want to be wealthy, but they don’t have a good set of principles to do it by.

Wealth is assets that earn while you sleep

Nivi: What’s the difference between wealth, money and status?

Naval: Wealth is the thing you want. Wealth is assets that earn while you sleep; it’s the factory of robots cranking out things. Wealth is the computer program running at night that’s serving other customers. Wealth is money in the bank that is reinvested into other assets and businesses.

A house can be a form of wealth, because you can rent it out; although that’s a less productive use of land than running a commercial enterprise.

My definition of wealth is oriented toward businesses and assets that can earn while you sleep.

Wealth buys your freedom

You want wealth because it buys you freedom—so you don’t have to wear a tie like a collar around your neck; so you don’t have to wake up at 7:00 a.m. to rush to work and sit in commute traffic; so you don’t have to waste your life grinding productive hours away into a soulless job that doesn’t fulfill you.

The purpose of wealth is freedom; it’s nothing more than that. It’s not to buy fur coats, or to drive Ferraris, or to sail yachts, or to jet around the world in a Gulf Stream. That stuff gets really boring and stupid, really fast. It’s about being your own sovereign individual.

You’re not going to get that unless you really want it. The entire world wants it, and the entire world is working hard at it.

It is competitive to some extent. It’s a positive sum game—but there are competitive elements to it, because there’s a finite amount of resources right now in society. To get the resources to do what you want, you have to stand out.

Money is how we transfer wealth

Money is how we transfer wealth. Money is social credits; it’s the ability to have credits and debits of other people’s time.

If I do my job right and create value for society, society says, “Oh, thank you. We owe you something in the future for the work that you did. Here’s a little IOU. Let’s call that money.”

That money gets debased because people steal the IOUs; the government prints extra IOUs; and people renege on their IOUs. But money tries to be a reliable IOU from society that you are owed something for something you did in the past.

We transfer these IOUs around; money is how we transfer wealth.

Status is your rank in the social hierarchy

There are fundamentally two huge games in life that people play. One is the money game. Money is not going to solve all of your problems; but it’s going to solve all of your money problems. I think people know that. They realize that, so they want to make money.

At the same time, deep down many people believe they can’t make it; so they don’t want any wealth creation to happen. They virtue signal by attacking the whole enterprise, saying, “Well, making money is evil. You shouldn’t do it.”

But they’re actually playing the other game, which is the status game. They’re trying to be high status in the eyes of others by saying, “Well, I don’t need money. We don’t want money.” 

Status is your ranking in the social hierarchy.

Wealth is not a zero-sum game. Everybody in the world can have a house. Because you have a house doesn’t take away from my ability to have a house. If anything, the more houses that are built, the easier it becomes to build houses, the more we know about building houses, and the more people can have houses.

Wealth is a very positive-sum game. We create things together. We’re starting this endeavor to create a piece of art that explains what we’re doing. At the end of it, something brand new will be created. It’s a positive-sum game.

Status is a very old game

Status, on the other hand, is a zero-sum game. It’s a very old game. We’ve been playing it since monkey tribes. It’s hierarchical. Who’s number one? Who’s number two? Who’s number three? And for number three to move to number two, number two has to move out of that slot. So, status is a zero-sum game.

Politics is an example of a status game. Even sports is an example of a status game. To be the winner, there must be a loser. Fundamentally, I don’t like status games. They play an important role in our society, so we can figure out who’s in charge. But you play them because they’re a necessary evil.

On an evolutionary basis—if you go back thousands of years—status is a much better predictor of survival than wealth. You couldn’t have wealth before the farming age because you couldn’t store things. Hunter-gatherers carried everything on their backs.

Hunter-gatherers lived in entirely status-based societies. Farmers started going to wealth-based societies. The modern industrial economies are much more heavily wealth-based societies.

People creating wealth will always be attacked by people playing status games

There’s always a subtle competition going on between status and wealth. For example, when journalists attack rich people or the tech industry, they’re really bidding for status. They’re saying, “No, the people are more important. And I, the journalist, represent the people, and therefore I am more important.”

The problem is, to win at a status game you have to put somebody else down. That’s why you should avoid status games in your life—because they make you into an angry combative person. You’re always fighting to put other people down and elevate yourself and the people you like.

Status games are always going to exist; there’s no way around it. Realize that most of the time when you’re trying to create wealth, you’re getting attacked by someone else and they’re trying to look like a goody-two shoes. They’re trying to up their own status at your expense.

They’re playing a different game. And it’s a worse game. It’s a zero-sum game, instead of a positive-sum game.

Make Abundance for the World
Wealth isn’t about taking something from somebody else

Ethical wealth creation makes abundance for the world

Naval: I think there is this notion that making money is evil, right? It’s rooted all the way back down to “money is the root of all evil.” People think that the bankers steal our money. It’s somewhat true in that, in a lot of the world, there’s a lot of theft going on all the time.

The history of the world, in some sense, is this predator/prey relationship between makers and takers. There are people who go out and create things, and build things, and work hard on things.

Then there are people who come along with a sword, or a gun, or taxes, or crony capitalism, or Communism, or what have you. There’s all these different methods to steal.

Even in nature, there are more parasites than there are non-parasitical organisms. You have a ton of parasites in you, who are living off of you. The better ones are symbiotic, they’re giving something back. But there are a lot that are just taking. That’s the nature of how any complex system is built.

What I am focused on is true wealth creation. It’s not about taking money. It’s not about taking something from somebody else. It’s from creating abundance.

Obviously, there isn’t a finite number of jobs, or finite amount of wealth. Otherwise we would still be sitting around in caves, figuring out how to divide up pieces of fire wood, and the occasional dead deer.

Most of the wealth in civilization, in fact all of it, has been created. It got created from somewhere. It got created from people. It got created from technology. It got created from productivity. It got created from hard work. This idea that it’s stolen is this horrible zero-sum game that people who are trying to gain status play.

Everyone can be rich

But the reality is everyone can be rich. We can see that by seeing, that in the First World, everyone is basically richer than almost anyone who was alive 200 years ago.

200 years ago nobody had antibiotics. Nobody had cars. Nobody had electricity. Nobody had the iPhone. All of these things are inventions that have made us wealthier as a species.

Today, I would rather be a poor person in a First World country, than be a rich person in Louis the XIV’s France. I’d rather be a poor person today than aristocrat back then. That’s because of wealth creation.

The engine of technology is science that is applied for the purpose of creating abundance. So, I think fundamentally everybody can be wealthy.

This thought experiment I want you to think through is imagine if everybody had the knowledge of a good software engineer and a good hardware engineer. If you could go out there, and you could build robots, and computers, and bridges, and program them. Let’s say every human knew how to do that.

What do you think society would look like in 20 years? My guess is what would happen is we would build robots, machines, software and hardware to do everything. We would all be living in massive abundance.

We would essentially be retired, in the sense that none of us would have to work for any of the basics. We’d even have robotic nurses. We’d have machine driven hospitals. We’d have self-driving cars. We’d have farms that are 100% automated. We’d have clean energy.

At that point, we could use technology breakthroughs to get everything that we wanted. If anyone is still working at that point, they’re working as a form of expressing their creativity. They’re working because it’s in them to contribute, and to build and design things.

I don’t think capitalism is evil. Capitalism is actually good. It’s just that it gets hijacked. It gets hijacked by improper pricing of externalities. It gets hijacked by improper yields, where you have corruption, or you have monopolies.
'''


print(summ_for_long(context))
# print(summ('My friend ate my lunch, and I hate him'))