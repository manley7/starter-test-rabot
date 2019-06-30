import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date

# use creds to create a client to interact with the Google Drive API

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('cred_drive.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Banque").sheet1

client = "desSTINATAIR" # get the name of the receiver
montant = "20000"
dateD = str(date.today().day)+"/"+str(date.today().month)
balance = sheet.cell(9, 3).value
motif = "virement à destination de " + client
if int(balance) < int(montant):
#   dispatcher.utter_message("Vous n'avez pas les fond pour effectuer ce virement")
    print("non")
else:
   i = 13
   while sheet.cell(i,1).value != "":
        i = i+1
   sheet.update_cell(i,1, dateD)
   sheet.update_cell(i,2, motif)
   sheet.update_cell(i,3, "-"+montant)

