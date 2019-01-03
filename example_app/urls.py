from django.conf.urls import url, include
from django.contrib import admin
from example_app.views import *


urlpatterns = [
    url(r'^chatte/', Chatte.as_view(), name='chatte'),
    url(r'^chattemail/', ChatteMail.as_view(), name='chattemail'),
    url(r'^chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    url(r'^file_claim/$', FileClaim.as_view(), name='file_claim'),
    url(r'^nominee/$', Nominee.as_view(), name='nominee'),
    url(r'^address/$', Address.as_view(), name='address'),
    url(r'^feedback/$', Feedback.as_view(), name='feedback'),
    url(r'^update_password/$', UpdatePassword.as_view(), name='update_password'),
    url(r'^submit_file_claim/$', SubmitFileClaim.as_view(), name='submit_file_claim'),
    url(r'^ticket_status/$', TicketStatus.as_view(), name='ticket_status'),
    url(r'^index1/$', Index.as_view(), name='index'),

    url(r'^what_premium/$', WhatPremium.as_view(), name='what_premium'),
    url(r'^what_proposal/$', WhatProposal.as_view(), name='what_proposal'),
    url(r'^quote/$', Index.as_view(), name='index'),
    url(r'^every_style/$', EveryStyle.as_view(), name='every_style'),
   # url(r'^setup/$', SetUp.as_view(), name='setup'),
   # url(r'^direct_to_nearest/$', DirectToNearest.as_view(), name='DirectToNearest'),
    url(r'^clear_all/$', ClearAll.as_view(), name='clear_all'),
    #url(r'^makes/$', Makes.as_view(), name='makes'),
   # url(r'^exprice_of', ExpriceOf.as_view(), name='ExpriceOf'),
    #url(r'^models/$', Models.as_view(), name='models'),
    url(r'^user_login/$', UserLogin.as_view(), name='UserLogin'),
    #url(r'^rtos/$', RTOs.as_view(), name='RTOs'),
    #url(r'^loct_code_of/$', LoctCodeOf.as_view(), name='LoctCode'),
    url(r'^policy/$', PolicyView.as_view(), name='PolicyView'),
    url(r'^proposal_creation/$', ThirdStep.as_view(), name='ThirdStep'),
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^train/$', TrainBotApiView.as_view(), name='train'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^forget_password/$', ForgetPassword.as_view(), name='ForgetPassword'),

]








