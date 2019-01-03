from chatterbot.logic import LogicAdapter
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session
import ast

from . models import *

from django.contrib.auth.models import User

import json

"""        User.objects.all().delete()
        Artist.objects.all().delete()
"""
class PolicyQuote(LogicAdapter):
    def __init__(self, **kwargs):
        super(PolicyQuote, self).__init__(**kwargs)

    def can_process(self, statement):
        last_artist = Artist.objects.all().last()
        if last_artist == None:
            user = User.objects.create(username="Admin", password="password@123")
            last_artist =Artist.objects.create(name="Admin", user=user)
        if last_artist.text == None:
                k = {}
                k['qwd$qewhd@dasjd']='dskh@dsjfcp$odjfc'
                k['qwdh$qewhd@dasjd']='dskh@dsjf$podjfc'
                last_artist.text = json.dumps(k)
        c_s = ast.literal_eval(last_artist.text)
        
        try:
            for c_ in list(c_s):
                if statement.text.find(c_) != -1:
                    print("statement.text.find(c_)",statement.text.find(c_), statement.text, c_)
                    return True
            return False
        except KeyError:
            return False

    def process(self, statement):
        artist = Artist.objects.all().last()
        if artist.text == None:
            artist.text = json.dumps("{'qwdhiqew@dpiuadasjd':'dskh@dsjfcpodjfc','sss@ssssssasasdsdwdewd@wdewf':'d21@32ewdee@edew'}")
            artist.save()
        c_s = ast.literal_eval(artist.text)
        for c_ in c_s.keys():
            if statement.text.find(c_) != -1:
                print(c_s)
                print()
                statement.text = "Your " + c_ + " is " + str(c_s[str(c_)])
                return statement
        return "Not Known"