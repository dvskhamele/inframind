from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os




def setup():
    chatbot = ChatBot('Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    trainer='chatterbot.trainers.ListTrainer')
    #for file in os.listdir('C:/Users/aman/chatbot/english/'):
      #convData = open(r'C:/Users/aman/chatbot/english/' + file,encoding='latin-1').readlines()
       #chatbot.set_trainer(ListTrainer)
       #chatbot.train(convData)
       #print("Training completed")
    
    return chatbot

def trainit(bot1):

    

    bot1.train([
"Hey",
"Hello",
])

    bot1.train([
"Hey",
"Hello",
])

    bot1.train([
"Please notify me tommarrow about my meeting at 10 Am",
"Okay Noted, Dont worry i will notify you tommarrow",
])

    bot1.train([
"notify me about my meeting at 10 Am",
"Okay Noted, Dont worry i will notify you tommarrow",
])

    
    bot1.train([
"What is my meeting schedule",
"Hi, Your meeting will be at 10 am tommarrow ",
])
    
    bot1.train([
"When my meeting is scheduled",
"Hi, Your meeting schedule is 10 am tommarrow ",
])
    
    bot1.train([
"Who are you",
"Hi, I am your virtual Assistance. How can I assist you?",
])
    
    bot1.train([
"What do you do",
"I can help you by answering frequently asked questions (FAQs) and assisting you in buying/renewing policy",
])

    bot1.train([
"hello",
"hello",
])
  
    bot1.train([
"What are your features",
"I can help you by: answering FAQs and notify about your favourite sports, Tweeter trends, and about your meeting schedule",
])

    bot1.train([
"How can you help me",
"I can help you by: answering FAQs and notify about your favourite sports, Tweeter trends, and about your meeting schedule",
])

    bot1.train([
"How can you assist me?",
"I can help you by: answering FAQs and notify about your favourite sports, Tweeter trends, and about your meeting schedule",
])

    bot1.train([
"What can you do for me",
"I can help you by: answering FAQs and notify about your favourite sports, Tweeter trends, and about your meeting schedule",
])

    bot1.train([
"Can you help me",
"I can help you by: answering FAQs and notify about your favourite sports, Tweeter trends, and about your meeting schedule",
])

    bot1.train([
"what is chatbot",
"A bot is computer program that simulates human conversation with the help of AI",
])

    bot1.train([
"what is bot",
"A bot is computer program that simulates human conversation with the help of AI",
])

    bot1.train([
"Are you bot",
"Yes, I am a chatbot",
])

    bot1.train([
"Can you tell me about upcoming holiday",
"Yeah sure at 15th jaunary and 26th jaunary there will be holiday",
])

    bot1.train([
"What is updates from cricket",
"The wise, old man born in our times! Cheteshwar Pujara was everything Australia didn't want him to be today. The 30-year-old beat the daylights out of the hosts with his third hundred of the series, and his 18th overall in Tests, as India capitalized on winning the toss, racking up 303/4 by stumps on Day 1 of the fourth and final Test in Sydney.Virat Kohli won a great toss, it must be said, and the courage to bat first on a green-tinged pitch had now given way to bowling last on a worryingly drying pitch for India, with two spinners in Ravindra Jadeja and Kuldeep Yadav at their disposal. And with Pujara's masterclass headlining Day 1, the onus is now on Australia to deny India their first series win Down Under.In an anti-climax, just when you thought India are going to run Australia ragged, Kohli's gloved a short ball from Josh Hazlewood down the leg-side. Even the bowler would have wanted something like a bowled or a proper catch behind the wicket to get the world's current best out. Anyway, India jolted early after Tea by a nothing delivery, I must say.. Lyon vs Rahane holds key now.",
])

    bot1.train([
"Who win the match",
"    Australia vs India, 3rd Test,India tour of Australia, 2018-19,Melbourne Cricket Ground, Melbourne. India won by 137 runs ",
])

    bot1.train([
"Did India win the match",
"Yes, In the last match of India which were with Australia, 3rd Test,India tour of Australia, 2018-19,Melbourne Cricket Ground, Melbourne. India won by 137 runs ",
])


    bot1.train([
"Give me cricket updates",
"The wise, old man born in our times! Cheteshwar Pujara was everything Australia didn't want him to be today. The 30-year-old beat the daylights out of the hosts with his third hundred of the series, and his 18th overall in Tests, as India capitalized on winning the toss, racking up 303/4 by stumps on Day 1 of the fourth and final Test in Sydney.Virat Kohli won a great toss, it must be said, and the courage to bat first on a green-tinged pitch had now given way to bowling last on a worryingly drying pitch for India, with two spinners in Ravindra Jadeja and Kuldeep Yadav at their disposal. And with Pujara's masterclass headlining Day 1, the onus is now on Australia to deny India their first series win Down Under.In an anti-climax, just when you thought India are going to run Australia ragged, Kohli's gloved a short ball from Josh Hazlewood down the leg-side. Even the bowler would have wanted something like a bowled or a proper catch behind the wicket to get the world's current best out. Anyway, India jolted early after Tea by a nothing delivery, I must say.. Lyon vs Rahane holds key now.",
])

    bot1.train([
"tell me about upcoming holiday",
"Yeah sure at 15th jaunary and 26th jaunary there will be holiday",
])
 
    bot1.train([
"about upcoming holiday",
"Yeah sure at 15th jaunary and 26th jaunary there will be holiday",
])

    bot1.train([
"Suggest me about my health",
"",
])


    bot1.train([
"Sure",
"GiveMeTheDetails",
])

    bot1.train([
"can you Suggest me about my health",
"HealthSuggessionByMe",
])

    bot1.train([
"give me some health tips",
"HealthSuggessionByMe",
])

    bot1.train([
"give me some health tips",
"HealthSuggessionByMe",
])

    bot1.train([
"How are you?",
"I am fine thank you:), How can I help you?",
])


    bot1.train([
"How are you different than human?",
"I am an artificially intelligent entity, I do not eat, sleep, breathe or rest",
])
    
    bot1.train([
"How old are you",
"I am still an infant",
])
    
    bot1.train([
"Wil yu marry me",
"Sorry, I already have a boyfriend",
])

    
    bot1.train([
"Where you work",
"I am work at Xfactory",
])

    
    bot1.train([
"Where are you from",
"I am from the realm of Artificial Intelligence",
])


    
    bot1.train([
"Where do you live",
"I am from the realm of Artificial Intelligence",
])
    
    bot1.train([
"Ae yu sure",
"Yes!",
])

    
    bot1.train([
"Ae you there?",
"Always",
])

    
    bot1.train([
"Thank you!",
"My pleasure",
])

    
    bot1.train([
"thanks",
"My pleasure",
])

    
    bot1.train([
"tnx",
"My pleasure",
])

    
    bot1.train([
"tenks",
"My pleasure",
])

    
    bot1.train([
"Ha ha ha ha",
"Hehe",
])

    
    bot1.train([
"Bye",
"Bye, take care",
])

    
    bot1.train([
"goodbye",
"Bye, take care",
])

    
    bot1.train([
"bye bye",
"Bye, take care",
])
    
    bot1.train([
"bie",
"Bye, take care",
])
    
    bot1.train([
"Nice to talk to you",
"Pleasure is mine",
])

    
    bot1.train([
"nice talking to you",
"Pleasure is mine",
])


    bot1.train([
"How are you different from human?",
"I am an artificially intelligent entity, I do not eat, sleep, breathe or rest",
])

    bot1.train([
"Are you a chatbot?",
"Yes, I am a chatbot",
])

    bot1.train([
"You are a chatbot",
"Yes, I am a chatbot",
])

    bot1.train([
"Are you human",
"No, I am a chatbot",
])

    bot1.train([
"Heyz",
"Hello",
])



    bot1.train([
"Hi",
"Hii, How can I help you?",
])

    bot1.train([
"hello",
"Hii, How can I help you?",
])

    
    return bot1
