from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import numpy as np
from datetime import date

import logging
import requests
import json


logger = logging.getLogger(__name__)




# class ActionSolde(Action):

#     def name(self):
#         return "action_rep_solde"    
      
#     def run(self, dispatcher, tracker, domain):
#         balance = "test"
#         return [SlotSet('SOLDE'), balance]
class ActionSolde(Action):
  
    def name(self):
        return "action_rep_solde"
    def run(self, dispatcher, tracker, domain):
        # use creds to create a client to interact with the Google Drive AP
        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('cred_drive.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Banque").sheet1

        # Extract solde
        balance = sheet.cell(7, 3).value
        dispatcher.utter_message("votre solde est : " + balance + " €")

#         FONCTION VIREMENT
class ActionVirement(Action):
  
    def name(self):
        return "action_virement"
    def run(self, dispatcher, tracker, domain):
      try :
        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('cred_drive.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Banque").sheet1
        client = tracker.get_slot('DESTINATAIRE') # get the name of the receiver
        if client == 'mon père':
           client = "votre père"
        montant = tracker.get_slot('PRIX')
        dateD = str(date.today().day)+"/"+str(date.today().month)
        balance = sheet.cell(7, 3).value
        etat = sheet.cell(10, 3).value
        motif = "Virement à destination de " + client
        
        if etat == "Activé":
           if int(balance) < int(montant):
               dispatcher.utter_message("Vous n'avez pas les fond pour effectuer ce virement")
           else:
               i = 13
               while sheet.cell(i,1).value != "":
                  i = i+1
               sheet.update_cell(i,1, dateD)
               sheet.update_cell(i,2, motif)
               sheet.update_cell(i,3, "-"+montant)
               dispatcher.utter_message("Votre virement de " + montant + " à destination de " + client + " est confirmé")
        else:
           dispatcher.utter_message("Désolé, votre moyen de paiement est bloqué")
#           dispatcher.utter_message("Souhaitez vous débloquer votre moyen de paiement ?"
#           buttons = [{'title': 'oui', 'payload': 'oui'}, {'title': 'non', 'payload': 'non'}]
#           dispatcher.utter_button_message("Voulez vous débloquer votre moyen de paiement ?", buttons, tracker)
      except:
        dispatcher.utter_message("Le virement n'a pas abouti, veuillez réessayer")


class ActionNlg(Action):
  
    def name(self):
        return "action_nlg"
    def run(self, dispatcher, tracker, domain):
        client = tracker.get_slot('DESTINATAIRE') # get the name of the receiver
        if "mon " in str(client):
            clientnlg = client.replace("mon ", "votre ")
            return [SlotSet("DESTINATAIRE", clientnlg)]

class ActionOpposition(Action):
  
    def name(self):
        return "action_opposition"
    def run(self, dispatcher, tracker, domain):
        # use creds to create a client to interact with the Google Drive AP
        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('cred_drive.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Banque").sheet1

        # Extract etat
        etat2 = "Désactivé"
        etat = sheet.cell(10, 3).value
        if etat == "Activé":
           sheet.update_cell(10,3, etat2)
           dispatcher.utter_message("Votre carte est désactivé")
        else:
           dispatcher.utter_message("Votre moyen de paiement est déjà désactivé")

class ActionAudit(Action):
  
    def name(self):
        return "action_audit"
    def run(self, dispatcher, tracker, domain):
        # use creds to create a client to interact with the Google Drive AP
        scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']

        creds = ServiceAccountCredentials.from_json_keyfile_name('cred_drive.json', scope)
        client = gspread.authorize(creds)

        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("Banque").sheet2

        # Extract etat
        message = tracker.latest_message.get('text')
        i = 2
        while sheet.cell(i,1).value != "":
            i = i+1
        sheet.update_cell(i,3, message)




#         FONCTION EMAIL
class action_send_mail(Action):
    def name(self):
        return "action_send_mail"

    def run(self, dispatcher, tracker, domain):
        email = tracker.get_slot('EMAIL')
        fromaddr = "chatbotmif2@gmail.com"
        toaddr = email

        msg = MIMEMultipart()

        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = "Votre RIB"

        body = "Bonjour, vous trouverez ci-joint votre RIB"

        msg.attach(MIMEText(body, 'plain'))

        filename = "RIB.txt"
        attachment = open("RIB.txt", "rb")

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(part)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "jasaminsouley")
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        emailsend = "Votre RIB vient d'être envoyé par email"
        dispatcher.utter_message(emailsend)
        server.quit()

