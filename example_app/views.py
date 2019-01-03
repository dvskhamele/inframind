# sudo netstat -ntlp | grep LISTEN
# sudo fuser -k 8000/tcp
import certifi
import json
from django.views.generic.base import TemplateView
from django.views.generic import View
from django.http import JsonResponse
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from example_app.chatbot_train import *
import requests
from socket import error as SocketError
import time

from django.shortcuts import render
from .models import *
from chatterbot.ext import django_chatterbot
import googlemaps

from django.http import HttpResponse

import random

import re


import gspread
from oauth2client.service_account import ServiceAccountCredentials
# use creds to create a client to interact with the Google Drive API

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.

from django.contrib.sessions.backends.db import SessionStore

from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
import ast


from django.core.mail import send_mail
from django.conf import settings

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import datetime
import time
import openpyxl as excel



class Feedback(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=1173685752").get_worksheet(
            2)
        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        name = data_dict['you']
        nominee = data_dict['nominee_name']
        relation = data_dict['relation']
        r = 0
        if not name in sheet.col_values(1):
            sheet.append_row([name, "-", "-"])

        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                sheet.update_cell(r, 3, nominee)
                sheet.update_cell(r, 2, relation)

                sheet.update_cell(r, 4, str(datetime.date.today()))
                break

        response_data = {
            "name": name, "address": nominee, "contact": relation}

        return JsonResponse(response_data)


class UpdatePassword(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=1173685752").get_worksheet(
            1)

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        name = data_dict['user_name_forget']
        new_password = data_dict['confirm_password']

        r = 0
        if not name in sheet.col_values(1):
            sheet.append_row([name, "-", "-"])

        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                sheet.update_cell(r, 2, new_password)
                status = "Hi " + name.capitalize() + ", You password has been successfully changed, Now you can login with new password :)"

                break

        response_data = {
            "name": name, "status": status}

        return JsonResponse(response_data)


def rno(no=123456):
    if str(no) in nos:
        no = random.randint(120000, 200000)
        rno(no)
    else:
        return no


def rno_with_list(nos,no=123456):
    if str(no) in nos:
        no = random.randint(120000, 200000)
        rno(no)
    else:
        return no

def urno(no=123456):
    nos = []
    for u in User.objects.all():
        nos.append(u.username)
    if str(no) in nos:
        no = random.randint(120000, 200000)
        urno(no)
    else:
        return no


class Ticket(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        name = data_dict['you']
        r = 0
        if not name in sheet.col_values(1):
            response_data = {"name": "NotFound", }

            return JsonResponse(response_data)

        enos = sheet.col_values(16 + 3)
        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                sheet.update_cell(r, 16, "Yes")
                no = random.randint(120000, 200000)
                no = rno(no)
                sheet.update_cell(r, 18, random.choice(["Under Processing", "Under Verification", "Transaction"]))
                sheet.update_cell(r, 19, no)

                break

        response_data = {"ticket": no,
                         "status": "Done"}

        return JsonResponse(response_data)


class SubmitFileClaim(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        name = data_dict['you']
        input_claim = data_dict['input_claim']
        r = 0

        if not name in sheet.col_values(1):
            response_data = {"name": "NotFound", }

            return JsonResponse(response_data)

        enos = sheet.col_values(16 + 3)

        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                sheet.update_cell(r, 16, "Yes")
                no = random.randint(120000, 200000)
                no = rno_with_list(no=no, nos=enos)

                sheet.update_cell(r, 17, input_claim)
                sheet.update_cell(r, 18, random.choice(["Under Processing", "Under Verification", "Transaction"]))
                sheet.update_cell(r, 19, no)
                break

        response_data = {"ticket": no,
                         "status": "Done"}

        return JsonResponse(response_data)


class TicketStatus(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        text = data_dict['text']
        names = [int(s) for s in text.split() if s.isdigit()]
        for name in names:
            if 120000 < name < 200000:
                name = name

        name = str(name)
        if not name in sheet.col_values(19):
            response_data = {"name": "NotFound", }

            return JsonResponse(response_data)
        r = 0
        for rv in sheet.col_values(19):
            r = r + 1
            if rv == name:
                status = "It is " + str(sheet.row_values(r)[17])

                break

        response_data = {"ticket": name,
                         "status": status}

        return JsonResponse(response_data)


class Address(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        name = data_dict['you']
        nominee = data_dict['nominee_name']
        relation = data_dict['relation']
        r = 0

        if not name in sheet.col_values(1):
            response_data = {"name": "NotFound", }

            return JsonResponse(response_data)

        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                p_nominee = sheet.row_values(3)[r]
                p_relation = sheet.row_values(4)[r]
                sheet.update_cell(r, 3, nominee)
                sheet.update_cell(r, 4, relation)
                sheet.update_cell(r, 16, "No")
                sheet.update_cell(r, 17, "Done By ChatInsure Bot")
                sheet.update_cell(r, 18, random.choice(["Under Processing", "Under Verification", "Transaction"]))
                break

        response_data = {"p_address": p_nominee, "p_contact": p_relation,
                         "name": name, "address": nominee, "contact": relation}

        return JsonResponse(response_data)


class Nominee(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        name = data_dict['you']
        nominee = data_dict['nominee_name']
        relation = data_dict['relation']
        r = 0

        if not name in sheet.col_values(1):
            response_data = {"name": "NotFound", }

            return JsonResponse(response_data)

        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                p_nominee = sheet.row_values(1)[r]
                p_relation = sheet.row_values(1)[r]
                sheet.update_cell(r, 5, nominee)
                sheet.update_cell(r, 6, relation)
                sheet.update_cell(r, 16, "No")
                sheet.update_cell(r, 17, "Done By ChatInsure Bot")
                sheet.update_cell(r, 18, random.choice(["Under Processing", "Under Verification", "Transaction"]))
                break

        response_data = {"p_nominee": p_nominee, "p_relation": p_relation,
                         "name": name, "nominee": nominee, "relation": relation}

        return JsonResponse(response_data)


class UserLogin(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=736971536").get_worksheet(
            1)

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)
        user_name = data_dict['user_name'].upper()
        password = data_dict['password']
        r = 0
        status = "Username or password is incorrect"

        users = sheet.col_values(1) + sheet.col_values(3) + sheet.col_values(4)
        user_names = []
        for user in users:
            user_names.append(user.upper())
        if not user_name in user_names:
            response_data = {"status": status, }

            return JsonResponse(response_data)

        for rv in user_names:
            r = r + 1
            if rv == user_name:
                p_user_name = sheet.row_values(r)[0].upper()
                p_password = sheet.row_values(r)[1]
                if password == p_password:
                    status = "Hi " + p_user_name.capitalize() + ", You have successfully logged in :)"
                break
            if len(sheet.col_values(1)) == r:
                r = 0

        response_data = {"status": status, }

        return JsonResponse(response_data)


class ForgetPassword(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=736971536").get_worksheet(
            1)

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        if request.method == "GET":
            user_name = data_dict['user_name_forget'].upper()
            password = data_dict['mobile_number']
        r = 0

        status = "Username or Mobile number is incorrect"

        users = sheet.col_values(1)
        user_names = []
        for user in users:
            user_names.append(user.upper())

        if not user_name in user_names:
            response_data = {"status": status, }

            return JsonResponse(response_data)

        for rv in user_names:
            r = r + 1
            if rv == user_name:
                p_user_name = sheet.row_values(r)[0].upper()
                p_password = sheet.row_values(r)[3]

                if password == p_password:
                    status = "Hi " + p_user_name.capitalize() + ", Please enter a otp which is sent to your Registred mobile number."
                break
            if len(sheet.col_values(1)) == r:
                r = 0

        response_data = {"status": status, }

        return JsonResponse(response_data)


class FileClaim(View):
    def get(self, request, *args, **kwargs):
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('example_app/client_secret.json', scope)
        client = gspread.authorize(creds)

        sheet = client.open_by_url(
            "https://docs.google.com/spreadsheets/d/1_qQjUcfKLZDtmZKK8tF2n12rTbO3JTU90pTXN6WisnQ/edit#gid=0").sheet1

        data_string = request.GET.get('data')
        data_dict = json.loads(data_string)

        if request.method == "GET":
            name = data_dict['you']
        r = 0

        if not name in sheet.col_values(1):
            response_data = {"name": "NotFound", }

            return JsonResponse(response_data)

        for rv in sheet.col_values(1):
            r = r + 1
            if rv == name:
                u_name = sheet.row_values(r)[1]

                u_bike = sheet.row_values(r)[9] + " " + sheet.row_values(r)[10]

                break

        response_data = {
            "u_name": u_name, "u_bike": u_bike}

        return JsonResponse(response_data)


class ChatterBotAppView(TemplateView):
    template_name = 'app.html'


class EveryStyle(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'every_style.css')


def get_html(url, headers, post_data, retry_count=0):
    try:

        photon_requests_session = requests.sessions.Session()
        photon_requests_session.verify = certifi.where()
        response = photon_requests_session.post(url, data=post_data, verify=False, headers=headers)
        response = response
        return response
    except SocketError as e:
        if retry_count == 5:
            raise e
        time.sleep(10)
        get_html(url=url, post_data=post_data, headers=headers, retry_count=retry_count + 1)


class ClearAll(View):
    """    
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def get(self, request, *args, **kwargs):
        response_data = {}
        return JsonResponse(response_data)

class Index(View):
    """
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def post(self, request, *args, **kwargs):
        """
        motor api - esbmotor
        payment api - esbpayment
        pdf generation api - esbgneric
        """
        """return render(request, 'form.html')
                        
                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password': 't43f!n501', 'grant_type': 'password',
                     'scope': 'esbmotor', 'client_id': 'ro.Thefinsol', 'client_secret': 'ro.t43f!n501', }
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method': "POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'
        response = get_html(url=url, headers=headers, post_data=post_data)
        response = json.loads(response.text)
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer " + response["access_token"]
        headers["Content-type"] = 'application/json'
        post_data["scope"] = "esbmotor"

        response = get_html(url=url, headers=headers, post_data=str(to_send))

        # Third_step
        """url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'
                                three_send = threesend(request)
                                to_send = { **post_data, **three_send }

                                response = get_html(url=url, headers=headers,post_data=str(to_send))
            """
        return render(request, 'form.html', {'response': json.loads(response.text)})

    def get(self, request, *args, **kwargs):
        try:
            sent = tosend(request)
        except:
            return render(request, 'PremiumForm.html')
        """return render(request, 'form.html')

                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password': 't43f!n501', 'grant_type': 'password',
                     'scope': 'esbmotor', 'client_id': 'ro.Thefinsol', 'client_secret': 'ro.t43f!n501', }
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method': "POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'

        response = get_html(url=url, headers=headers, post_data=post_data)
        try:
            response = json.loads(response.text)
        except:
            return HttpResponse(response.text)

        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer " + response["access_token"]
        headers["Content-type"] = 'application/json'

        post_data["scope"] = "esbmotor"

        to_send = {**post_data, **sent}

        response = get_html(url=url, headers=headers, post_data=str(to_send))

        try:
            response = json.loads(response.text)
        except:
            return HttpResponse({"message":"The server is not responding right now, please try again after sometime."})

        # response = {{ **json.loads(response.text), **to_send }}

        # Third_step
        """url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'
                                three_send = threesend(request)
                                to_send = { **post_data, **three_send }

                                response = get_html(url=url, headers=headers,post_data=str(to_send))
        """

        no = random.randint(120000, 200000)
        no = urno(no)
        user = User.objects.create(username=str(no))

        response1 = {}
        for k in response.keys():
            l = str(response[k])
            response1[re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()] = l

        artist = Artist.objects.create(user=user,text=str(response1))
        login(request, user)



        return JsonResponse(response1)





def tosend1(request):
    POST = request.GET
    OldPolicy = POST["old_policy"]
    k = {
        "old_policy": POST["old_policy"],
        "ExShowRoomPrice": POST["price"],
        "CustomerType": str(POST["radio1"]).upper(),
        "RTOLocationCode": POST["rto_code"],
        "StateCode": POST["rto_state_code"],
        "CityCode": POST["rto_city_code"],
        "NewDate": POST["new_date"],
        "RegistrationNumber": POST["reg_number"],
        "DeliveryOrRegistrationDate": POST["reg_date"],
        "FirstRegistrationDate": POST["reg_date"],
        "PolicyStartDate": POST["new_date"],
        "PolicyEndDate": POST["new_date"],
        "Email": POST["email"],
        "MobileNumber": POST["number"],
        "VehicleModelCode": str(int(POST["modelc"])),













        "IsNoPrevInsurance": "FALSE",
        "BusinessType": "New Business",
        "DealId": "DL-3005/1483341",
        "CorrelationId": str(uuid.uuid4()),
        "GSTToState": str("MAHARASHTRA").upper(),
        "CountryCode": "91",
        "VehicleMakeCode": str(int(31)),
        "Tenure": "1",
        "PACoverTenure": "5",
        "TPTenure": "5",
        "ManufacturingYear": '',
    }

    k["ManufacturingYear"] = k["FirstRegistrationDate"][:4]
    end_date = datetime.datetime.strptime(k["PolicyStartDate"], "%d/%m/%Y").date()
    end_date = str(end_date + datetime.timedelta(int(k["Tenure"]) * 364))
    k["PolicyEndDate"] = str(end_date)


    if OldPolicy == "false":
        k["BusinessType"] = "New Business"

    if OldPolicy == "true":
        k["BusinessType"] = "Roll Over"

    k["PolicyStartDate"] = datetime.datetime.strptime(k["PolicyStartDate"], "%d/%m/%Y").strftime("%Y-%m-%d")

    return k


def tosend2(request):
    POST = request.GET
    OldPolicy = POST["old_policy"]
    k = {
        "old_policy": POST["old_policy"],
        "ExShowRoomPrice": POST["ExShowRoomPrice"],
        "CustomerType": str(POST["CustomerType"]).upper(),
        "RTOLocationCode": POST["RTOLocationCode"],
        "StateCode": POST["StateCode"],
        "CityCode": POST["CityCode"],
        "NewDate": POST["NewDate"],
        "RegistrationNumber": POST["RegistrationNumber"],
        "DeliveryOrRegistrationDate": POST["DeliveryOrRegistrationDate"],
        "FirstRegistrationDate": POST["FirstRegistrationDate"],
        "PolicyStartDate": POST["PolicyStartDate"],
        "PolicyEndDate": POST["PolicyEndDate"],
        "Email": POST["Email"],
        "MobileNumber": POST["MobileNumber"],
        "VehicleModelCode": str(int(POST["VehicleModelCode"])),













        "IsNoPrevInsurance": "FALSE",
        "BusinessType": "New Business",
        "DealId": "DL-3005/1483341",
        "CorrelationId": str(uuid.uuid4()),
        "GSTToState": str("MAHARASHTRA").upper(),
        "CountryCode": "91",
        "VehicleMakeCode": str(int(31)),
        "Tenure": "1",
        "PACoverTenure": "5",
        "TPTenure": "5",
        "ManufacturingYear": '',
    }

    k["ManufacturingYear"] = k["FirstRegistrationDate"][:4]
    end_date = datetime.datetime.strptime(k["PolicyStartDate"], "%Y-%m-%d").date()
    end_date = str(end_date + datetime.timedelta(int(k["Tenure"]) * 364))
    k["PolicyEndDate"] = str(end_date)


    if OldPolicy == "false":
        k["BusinessType"] = "New Business"

    if OldPolicy == "true":
        k["BusinessType"] = "Roll Over"

    k["PolicyStartDate"] = datetime.datetime.strptime(k["PolicyStartDate"], "%Y-%m-%d").strftime("%Y-%m-%d")

    return k



class WhatPremium(View):
    """
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def post(self, request, *args, **kwargs):
        return render(request, 'form.html', {'response': json.loads(response.text)})

    def get(self, request, *args, **kwargs):
        sent = tosend1(request)

        """return render(request, 'form.html')

                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password': 't43f!n501', 'grant_type': 'password',
                     'scope': 'esbmotor', 'client_id': 'ro.Thefinsol', 'client_secret': 'ro.t43f!n501', }
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method': "POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'

        response = get_html(url=url, headers=headers, post_data=post_data)
        try:
            response = json.loads(response.text)
        except:
            return HttpResponse(response.text)

        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer " + response["access_token"]
        headers["Content-type"] = 'application/json'

        post_data["scope"] = "esbmotor"

        to_send = {**post_data, **sent}

        response = get_html(url=url, headers=headers, post_data=str(to_send))

        try:
            response = json.loads(response.text)
        except:
            return HttpResponse({"message":"The server is not responding right now, please try again after sometime."})

        # response = {{ **json.loads(response.text), **to_send }}

        # Third_step
        """url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'
                                three_send = threesend(request)
                                to_send = { **post_data, **three_send }

                                response = get_html(url=url, headers=headers,post_data=str(to_send))
        """

        no = random.randint(120000, 200000)
        no = urno(no)
        user = User.objects.create(username=str(no))

        response1 = {}
        for k in response.keys():
            l = str(response[k])
            response1[re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()] = l

        artist = Artist.objects.create(user=user,text=str(response1))
        login(request, user)



        return render(request, 'form.html', {'response': sent, 'requested': sent, 'got_parameters': response})


class ThirdStep(View):
    """
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def post(self, request, *args, **kwargs):
        return render(request, 'form.html')

    def get(self, request, *args, **kwargs):
        """return render(request, 'form_proposal.html')

                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password': 't43f!n501', 'grant_type': 'password',
                     'scope': 'esbmotor', 'client_id': 'ro.Thefinsol', 'client_secret': 'ro.t43f!n501', }
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method': "POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'
        response = get_html(url=url, headers=headers, post_data=post_data)
        response = json.loads(response.text)
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer " + response["access_token"]
        headers["Content-type"] = 'application/json'
        post_data["scope"] = "esbmotor"

        # Third_step
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'
        three_send = threesend(request)
        to_send = {**post_data, **three_send}
        print("three_send", to_send)
        response = get_html(url=url, headers=headers, post_data=str(to_send))

        response = json.loads(response.text)
        response1 = {}


        POST = json.loads(request.GET.get("data"))

        print(request.user.artist.all().first().text)
        response_saved = ast.literal_eval(request.user.artist.all().first().text)


        for k in list(POST):
            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
            response_saved[l] = POST[k]

        for k in response.keys():
            l = str(response[k])
            response1[re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()] = l

        for k in list(response1):
            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
            response_saved[l] = response1[k]

        for k in list(to_send):
            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
            response_saved[l] = to_send[k]

        for ele in response_saved:
            if isinstance(ele, dict):
                for k, v in ele.items():
                    if isinstance(v, dict):
                        for k1, v1 in v.items():
                            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k1).lower()
                            response_saved[l] = v1
                    else:
                        l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
                        response_saved[l] = v

        artist = Artist.objects.get(user=request.user)
        artist.text = str(response_saved)
        artist.save()

        # return render(request, 'form.html', {'response': response1, 'requested': three_send})
        print("to_send\n",response_saved)
        return JsonResponse(response1)




class WhatProposal(View):
    """
    API endpoint to interact with http://cldilbizapp01.cloudapp.net:9000/cerberus/connect/token
    """

    def post(self, request, *args, **kwargs):
        return render(request, 'form.html')

    def get(self, request, *args, **kwargs):

        sent = tosend2(request)
        """return render(request, 'form_proposal.html')

                                def post(self, request, *args, **kwargs):"""
        post_data = {'username': 'Thefinsol', 'password': 't43f!n501', 'grant_type': 'password',
                     'scope': 'esbmotor', 'client_id': 'ro.Thefinsol', 'client_secret': 'ro.t43f!n501', }
        """,'grant_type':'password',
        'scope':'esbgeneric','client_id':'ro.Thefinsol','client_secret':'ro.t43f!n501',"""
        headers = {'Content-type': 'application/x-www-form-urlencoded', 'Method': "POST"}
        url = 'https://cldilbizapp02.cloudapp.net:9001/cerberus/connect/token'
        response = get_html(url=url, headers=headers, post_data=post_data)
        response = json.loads(response.text)
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCalculatePremium'
        headers["Authorization"] = "Bearer " + response["access_token"]
        headers["Content-type"] = 'application/json'
        post_data["scope"] = "esbmotor"

        # Third_step
        url = 'https://cldilbizapp02.cloudapp.net:9001/ILServices/Motor/v1/Proposal/TwoWheelerCreateProposal'

        three_send = threesend1(request)
        to_send = {**post_data, **three_send}
        print("three_send", to_send)
        response = get_html(url=url, headers=headers, post_data=str(to_send))

        response = json.loads(response.text)
        response1 = {}


        POST = request.GET

        print(request.user.artist.all().first().text)
        response_saved = ast.literal_eval(request.user.artist.all().first().text)


        for k in list(POST):
            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
            response_saved[l] = POST[k]

        for k in response.keys():
            l = str(response[k])
            response1[re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()] = l

        for k in list(response1):
            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
            response_saved[l] = response1[k]

        for k in list(to_send):
            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
            response_saved[l] = to_send[k]

        for ele in response_saved:
            if isinstance(ele, dict):
                for k, v in ele.items():
                    if isinstance(v, dict):
                        for k1, v1 in v.items():
                            l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k1).lower()
                            response_saved[l] = v1
                    else:
                        l = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', k).lower()
                        response_saved[l] = v

        artist = Artist.objects.get(user=request.user)
        artist.text = str(response_saved)
        artist.save()

        # return render(request, 'form.html', {'response': response1, 'requested': three_send})
        print("to_send\n",response_saved)
        return render(request, 'form.html', {'response': three_send, 'requested': three_send,  'got_parameters': response })


class PolicyView(View):

    def get(self, request, *args, **kwargs):
        prod = Prod.objects.all()
        """idv="High",cover="-1"""
        return JsonResponse({
            'text': [
                str(prod)
            ]
        }, status=200)


       
class Chatte(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    def get(self, request, *args, **kwargs):


        driver = webdriver.Chrome()

        # link to open a site
        driver.get("https://web.whatsapp.com/")

        # 10 sec wait time to load, if good internet connection is not good then increase the time
        # units in seconds
        # note this time is being used below also
        wait = WebDriverWait(driver, 10)
        wait5 = WebDriverWait(driver, 5)
        screenie = 'example_app/static/img/screenie.png'
        driver.save_screenshot(screenie)
        return render(request, 'screenie.html')

    def post(self, request, *args, **kwargs):


        driver = webdriver.Chrome()

        # link to open a site
        driver.get("https://web.whatsapp.com/")

        # 10 sec wait time to load, if good internet connection is not good then increase the time
        # units in seconds
        # note this time is being used below also
        wait = WebDriverWait(driver, 10)
        wait5 = WebDriverWait(driver, 5)
        screenie = 'example_app/static/img/screenie.png'
        driver.save_screenshot(screenie)


        import cv2 
        import numpy as np
        from PIL import Image, ImageEnhance

        winname = "Test"
        cv2.namedWindow(winname)        # Create a named window

        pil_image = Image.open(screenie)
        contrast_enhancer = ImageEnhance.Contrast(pil_image)
        pil_enhanced_image = contrast_enhancer.enhance(2)
        enhanced_image = np.asarray(pil_enhanced_image)
        cv2.imshow('Enhanced Image', enhanced_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        input("Scan the QR code and then press Enter")


        msgToSend = [
                    [12, 32, 0, "Hello! This is test Msg. Please Ignore." + "http://bit.ly/mogjm05"]
                ]



        count = 0
        while count < len(msgToSend):
            # Identify time
            print(count)
            curTime = datetime.datetime.now()
            curHour = curTime.time().hour
            curMin = curTime.time().minute
            curSec = curTime.time().second

            # if time matches then move further
            if msgToSend[count][0] != msgToSend[count][1]:
                # utility variables to tract count of success and fails
                success = 0
                sNo = 1
                failList = []

                # Iterate over selected contacts
                for target in targets:
                    print(sNo, ". Target is: " + target)
                    sNo += 1
                    if sNo > 0:
                        # Select the target
                        x_arg = '//span[contains(@title,' + target + ')]'
                        try:
                            wait5.until(EC.presence_of_element_located((
                                By.XPATH, x_arg
                            )))
                        except:
                            # If contact not found, then search for it
                            searBoxPath = '//*[@id="input-chatlist-search"]'
                            wait5.until(EC.presence_of_element_located((
                                By.ID, "input-chatlist-search"
                            )))
                            inputSearchBox = driver.find_element_by_id("input-chatlist-search")
                            time.sleep(0.5)
                            # click the search button
                            driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/div/button').click()
                            time.sleep(1)
                            inputSearchBox.clear()
                            inputSearchBox.send_keys(target[1:len(target) - 1])
                            print('Target Searched')
                            # Increase the time if searching a contact is taking a long time
                            time.sleep(4)

                        # Select the target
                        driver.find_element_by_xpath(x_arg).click()
                        print("Target Successfully Selected")
                        time.sleep(2)
                        j = 2
                        while j > 0:
                            print(time.ctime())
                            ins = driver.find_elements_by_class_name("_3_7SH")
                            if "message-in" in ins[len(ins) - 1].get_attribute("class") and j > 1:
                                what_input = ins[len(ins) - 1].find_elements_by_class_name("selectable-text")[0].text
                                input_data = input_text = json.dumps({"text": what_input }, ensure_ascii=False).encode("utf-8")

		                # Select the Input Box
                                inp_xpath = "//div[@contenteditable='true']"
                                input_box = wait.until(EC.presence_of_element_located((
		                    By.XPATH, inp_xpath)))
                                time.sleep(1)

		                # Send message
		                # taeget is your target Name and msgToSend is you message'
                                print("input_data", input_text)

                                headers = {'Content-type': 'application/json/', 'Method': "POST"}
                                url = 'http://ec2-52-66-248-85.ap-south-1.compute.amazonaws.com:82/chatterbot/'
                                print("input_text", input_text)
                                response = get_html(url=url, headers=headers, post_data=input_data)
                                response = response.text



                                print("response", response)
                                print("json.loads(response)", json.loads(response))

                                if str(json.loads(response)["text"]) == "policyForm":
                                    input_box.send_keys("Please visit this link for proposal: "+"http://ec2-52-66-248-85.ap-south-1.compute.amazonaws.com:82/index1")  # + Keys.ENTER # (Uncomment it if your msg doesnt contain '\n')
                                elif "book garag" in str(input_text).lower():
                                    input_box.send_keys(str("Below are the garages you can book appointment with: "))  
                                    input_box.send_keys(Keys.ENTER)

                                    garages = {
                                    ' #1' : ['Bafna Motorcycles, Mumbai', "18.9642628, 72.7840248", "https://www.google.co.in/maps/dir/22,+77/Bafna+Scooters+Spares+%26+Accessories,+160-A%2F3,+Banker+Building,+Grant+Road+East,+Allibhai+Premji+Marg,+Bharat+Nagar,+Grant+Road,+Mumbai,+Maharashtra+400007/@20.4805234,72.6605773,7z/data=!3m1!4b1!4m12!4m11!1m3!2m2!1d77!2d22!1m5!1m1!1s0x3be7ce12d5f78f75:0x851b25350e520ac7!2m2!1d72.8190437!2d18.9642628!3e0"],
                                    ' #2': ['Sai Service Agency Bombay Pvt. Ltd., Mumbai',"19.2195078,72.8632974", "https://www.google.co.in/maps/dir/22,+77/19.2195078,+72.8632974/@20.6026251,72.6861823,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8632974!2d19.2195078!3e0"],
                                    ' #3' :
                                    ['Twenty One Speciality Chemicals Pvt Ltd, Mumbai',"19.1196179,  72.8880612","https://www.google.co.in/maps/dir/22,+77/19.1196179,+72.8880612++/@20.5532918,72.6841135,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8880612!2d19.1196179!3e0"],
                                    ' #4' :
                                    ['Anand Auto Tranz Private Limited, Mumbai', "19.125118,  72.8499311","https://www.google.co.in/maps/dir/22,+77/'19.125118,72.8499311'/@20.5581882,72.6797961,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8499311!2d19.125118!3e0"] ,              
                                    ' #5' :
                                    ['Bnt Motors Pvt Ltd, Delhi',"28.7642156, 77.1412214", "https://www.google.co.in/maps/dir/22,+77/28.7642156,+77.1412214/@25.3238252,72.4780813,6z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d77.1412214!2d28.7642156!3e0"] ,
                                    ' #6':
                                    ['Santoor Car Care, pune',"18.5634493, 73.9346069", "https://www.google.co.in/maps/dir/22,+77/'18.5634493,73.9346069'/@20.2797916,73.2209737,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.9346069!2d18.5634493!3e0"] ,
                                    ' #7':['Sehgal Autoriders Pvt Ltd, pune',"18.6198904, 73.8373883", "https://www.google.co.in/maps/dir/22,+77/'18.6198904,73.8373883'/@20.3065117,73.173705,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.8373883!2d18.6198904!3e0"],
                                    ' #8' :['Singh Cycle And Motor Co, pune',"18.5715414, 73.9521122", "https://www.google.co.in/maps/dir/22,+77/'18.5715414,73.9521122'/@20.2811486,73.2265941,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.9521122!2d18.5715414!3e0" ],
                                    ' #9' :['Sehgal Autoriders Pvt Ltd, pune',"18.5117089, 73.7686455","https://www.google.co.in/maps/dir/22,+77/18.5117089,+73.7686455/@20.2544626,73.1335175,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.7686455!2d18.5117089!3e0"],
                                    '#10':[
                                    'Gems Automobiles Pvt. Ltd. pune',"18.5016726, 73.9208914","https://www.google.co.in/maps/dir/22,+77/'18.5016726,73.9208914'/@20.2493905,73.2149764,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.9208914!2d18.5016726!3e0"],
                                   '#11' :['Shanti Scooters Private Limited, pune',"18.5741306,  73.8859774","https://www.google.co.in/maps/dir/22,+77/'18.5741306,73.8859774'/@20.2850231,73.1830716,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.8859774!2d18.5741306!3e0"] ,
                                   '#12' :['Rohan Automotive, pune', "18.5838962,73.8310914","https://www.google.co.in/maps/dir/22,+77/'18.5838962,73.8310914'/@20.2730214,73.1661067,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d73.8310914!2d18.5838962!3e0"],
                                    }
                                    for k,v in garages.items():
                                        try:
                                            input_box.send_keys("\n Reply with *Garage "+str(k) + "* for " + str(v[0])+" "+str(v[2])) 
                                            input_box.send_keys(Keys.ENTER)
                                        except:
                                            pass 
                                    input_box.send_keys("\n For example: To book an appontment with Garage #7 Sehgal Autoriders Pvt Ltd, pune. Reply with: Garage #7") 
                                    input_box.send_keys(Keys.ENTER)

                                elif "book branch" in str(input_text).lower():
                                    input_box.send_keys(str("Below are the branches you can book appointment with: "))  
                                    input_box.send_keys(Keys.ENTER)

                                    garages = {
                                    ' #1': 
                                    ["ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM","28.525507, 77.1840862", "https://www.google.co.in/maps/dir/22,+77/+28.525507,77.1840862/@25.2352892,72.478056,6z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d77.1840862!2d28.525507!3e0"] ,
                                    ' #2': ['ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM',"28.6923729, 76.9954194","https://www.google.co.in/maps/dir/22,+77/'28.5471945,77.0374669'/@25.2323957,72.304773,6z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d77.0374669!2d28.5471945!3e0"],
                                    ' #3': ['ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM', "28.5471945, 77.0374669","https://www.google.co.in/maps/dir/22,+77/28.5471945,+77.0374669/@25.2323957,72.304773,6z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d77.0374669!2d28.5471945!3e0"],
                                    ' #4': ['ICICI Bank Mohan Co, operative Ind Estate New Delhi - Branch & ATM', "28.6923729, 76.9954194","https://www.google.co.in/maps/dir/22,+77/28.6923729,76.9954194+/@25.2880068,72.3047889,6z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d76.9954194!2d28.6923729!3e0"],                                   
                                    ' #5': ['ICICI Lombard General Insurance Co. Ltd, Andheri (E), Mumbai, Maharashtra',"19.1070845, 72.8821504", "https://www.google.co.in/maps/dir/22,+77/'19.1070845,72.8821504'/@20.5506124,72.682318,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8821504!2d19.1070845!3e0"],
                                    ' #6': ['ICICI Lombard General Insurance Co. Ltd, Fort, Mumbai',"18.9333571,72.8314793","https://www.google.co.in/maps/dir/22,+77/18.9333571,+72.8314793/@20.4652683,72.6703423,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8314793!2d18.9333571!3e0"],
                                    ' #7': ['ICICI Lombard General Insurance Co. Ltd, Malad, Mumbai', "19.1862033, 72.8276892",",https://www.google.co.in/maps/dir/22,+77/'19.1862033,72.8276892'/@20.5581882,72.6690306,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8276892!2d19.1862033!3e0"]  ,
                                    ' #8': ['ICICI Lombard General Insurance Co. Ltd, Prabhadevi, Mumbai',"19.0163602,72.8249249",",https://www.google.co.in/maps/dir/22,+77/'19.0163602,72.8249249'/@20.5049186,72.6609953,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8249249!2d19.0163602!3e0"],
                                    ' #9': ['ICICI Lombard General Insurance Co. Ltd, Sion, Mumbai', "19.0495536, 72.8747062","',https://www.google.co.in/maps/dir/22,+77/'19.0495536,72.8747062'/@20.5232604,72.6916082,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8747062!2d19.0495536!3e0"],
                                    '#10': ['ICICI Lombard General Insurance Co. Ltd, Teli gali, Mumbai',"19.1164241, 72.8484543", "https://www.google.co.in/maps/dir/22,+77/'19.1164241,72.8484543'/@20.5539988,72.6787807,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.8484543!2d19.1164241!3e0"],
                                    '#11': ['ICICI Lombard General Insurance Co. Ltd, Thane , Mumbai', "19.2038274, 72.9752509", "https://www.google.co.in/maps/dir/22,+77/'19.2038274,72.9752509'/@20.6087999,73.8649784,8z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.9752509!2d19.2038274!3e0"],
                                    '#12': ['ICICI Lombard General Insurance Co. Ltd, Vashi , Mumbai', "19.0644061, 72.9946395", "https://www.google.co.in/maps/dir/22,+77/'19.0644061,72.9946395'/@20.5308067,72.7520671,7z/data=!3m1!4b1!4m10!4m9!1m3!2m2!1d77!2d22!1m3!2m2!1d72.9946395!2d19.0644061!3e0"] ,
                                    }
                                    for k,v in garages.items():
                                        try:
                                            input_box.send_keys("\n Reply with *Branch "+str(k) + "* for " + str(v[0])+" "+str(v[2])) 
                                            input_box.send_keys(Keys.ENTER)
                                        except:
                                            pass 
                                    input_box.send_keys("\n For example: To book an appontment with branch #5 ICICI Lombard General Insurance Co. Ltd, Andheri (E), Mumbai, Maharashtra. Reply with: branch #5") 
                                    input_box.send_keys(Keys.ENTER)
                                elif str(json.loads(response)["text"]) == "garage" or "book appo" in str(what_input).lower():
                                    input_box.send_keys(str("Please select one of the following options: 1) Book Garage 2) Book Branch"))  
                                else:
                                        try:
                                            branch_selected = garages[str(what_input[-3:])]
                                            input_box.send_keys("Your appointment is booked with "+str(branch_selected[0]) + " with address "+str(branch_selected[2])) 
                                            input_box.send_keys(Keys.ENTER)
                                            input_box.send_keys("Please, reply with a date in DD-MM-YYYY, HH:MM format (as in 01-01-2019, 00:15). To check availability and finalising the appointment.") 
                                        except:
                                            if re.search(r'\d{2}-\d{2}-\d{4}', what_input) != None:
                                                date = re.search(r'\d{2}-\d{2}-\d{4}, \d{2}:\d{2}', what_input)
                                                input_box.send_keys("Your appointment has been booked. Thanks :)") 
                                            else:
                                                print(str(json.loads(response)["text"]))
                                                input_box.send_keys(str(json.loads(response)["text"]))  # + Keys.ENTER # (Uncomment it if your msg doesnt contain '\n')
            
		                # Link Preview Time, Reduce this time, if internet connection is Good
                                time.sleep(4)
                                input_box.send_keys(Keys.ENTER)
                                print("Successfully Send Message to : " + target + '\n')
                                print(time.ctime())
                        success += 1
                        time.sleep(0.5)

                print("\nSuccessfully Sent to: ", success)
                print("Failed to Sent to: ", len(failList))
                print(failList)
                print('\n\n')
                count += 1


        return JsonResponse(response_data, status=200)



       
class ChatteMail(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    def get(self, request, *args, **kwargs):

        targets = ["thefinansoldemo@gmail.com",]

        msgToSend = [
                    [12, 32, 0, "Hello! This is test Msg. Please Ignore." + "http://bit.ly/mogjm05"]
                ]


        store = file.Storage('example_app/token.json')
        creds = store.get()
        http = creds.authorize(Http())   
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('example_app/PythonMateMailCredentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        service = discovery.build('gmail', 'v1', http=creds.authorize(Http()))
        user_id = "dvskha@gmail.com"
        # Call the Gmail API

        count = 0
        while count < len(msgToSend):
            # Identify time
            curTime = datetime.datetime.now()
            curHour = curTime.time().hour
            curMin = curTime.time().minute
            curSec = curTime.time().second

            # if time matches then move further
            if msgToSend[count][0] != msgToSend[count][1]:
                # utility variables to tract count of success and fails
                success = 0
                sNo = 1
                failList = []

                # Iterate over selected contacts
                for target in targets:
                    print(sNo, ". Target is: " + target)
                    sNo = 0
                    client_to_chat = "thefinansoldemo@gmail.com"
                    while sNo == 0:
                        headers = {'Content-type': 'application/json/', 'Method': "POST"}
                        url = 'http://ec2-52-66-248-85.ap-south-1.compute.amazonaws.com:82/chatterbot/'
                        messages = ListMessagesMatchingQuery(service, user_id, query="from:"+client_to_chat)
                        messages_length = len(messages)
                        while messages_length > 0:
                            msg_id = messages[0]['id']
                            input_text = GetMessage(service, user_id, msg_id)
                            print()
                            print()
                            input_snippet = input_text['snippet']
                            print("SHOWING RESPONE", input_snippet)
                            if "On Mon" in input_snippet or  "On Tue" in input_snippet or  "On Wed" in input_snippet or  "On Thu" in input_snippet or  "On Fri" in input_snippet or  "On Sat" in input_snippet or  "On Sun" in input_snippet:
                                input_snippet=input_snippet[:input_snippet.find("On Mon")]
                                input_snippet=input_snippet[:input_snippet.find("On Tue")]
                                input_snippet=input_snippet[:input_snippet.find("On Wed")]
                                input_snippet=input_snippet[:input_snippet.find("On Thu")]
                                input_snippet=input_snippet[:input_snippet.find("On Fri")]
                                input_snippet=input_snippet[:input_snippet.find("On Sat")]
                                input_snippet=input_snippet[:input_snippet.find("On Sun")]
                            print()
                            if "INBOX" in input_text["labelIds"]:
                                text_recieved = input_snippet
                                input_data = json.dumps({"text": text_recieved }, ensure_ascii=False)
                                response = get_html(url=url, headers=headers, post_data=input_data)
                                response = json.loads(response.text)["text"] 
                                try:
                                    to_send = CreateMessage(user_id, client_to_chat, "In reply to: "+ text_recieved, response)
                                except:
                                    to_send = CreateMessage(user_id, client_to_chat, "text_recieved", response + " : " +  text_recieved )
                                message = SendMessage(service, user_id, to_send)
                                DeleteMessage(service, user_id, msg_id)
                                messages_length = 0
                                print("SENT MESSAGE: ", message)

                print("\nSuccessfully Sent to: ", success)
                print("Failed to Sent to: ", len(failList))
                print(failList)
                print('\n\n')
                count += 1


        return JsonResponse(response_data, status=200)



class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    def post(self, request, *args, **kwargs):
        chatterbot = ChatBot(**settings.CHATTERBOT


                         )


        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.read().decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        chatterbot = ChatBot(**settings.CHATTERBOT
                         )
        response = chatterbot.get_response(request.GET["text"])

        return HttpResponse(response)


"""


     url = 'https://clients6.google.com/rpc'
     values = {
         "method": "pos.plusones.get",
         "id": "p",
         "params": {
                    "nolog": True,
                    "id": "http://www.newswhip.com",
                    "source": "widget",
                    "userId": "@viewer",
                    "groupId": "@self"
                   },
          "jsonrpc": "2.0",
          "key": "p",
          "apiVersion": "v1"
     }
     headers = {"content-type" : "application/json"}

     req = requests.post(url, data=json.dumps(values), headers=headers)


"""


class TrainBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """


    def get(self, request, *args, **kwargs):
        chatterbot = ChatBot(**settings.CHATTERBOT)
        #chatterbot = trainit(self.chatterbot)
        chatterbot = trainit(chatterbot)
        """
        Return a response to the statement in the posted data.


        * The JSON data should contain a 'text' attribute.
        """
        input_data = json.loads(request.read().decode('utf-8'))

        if 'text' not in input_data:
            return JsonResponse({
                'text': [
                    'The attribute "text" is required.'
                ]
            }, status=400)

        response = chatterbot.get_response(input_data)

        response_data = response.serialize()

        return JsonResponse(response_data, status=200)
