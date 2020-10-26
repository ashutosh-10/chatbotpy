from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
bot = Flask(__name__)

from pred import predict



formm = """

<form action ="/whatsapp" method="post">
	<input type = "text" name="body">
	<input type = "submit" value="send">
</form>
"""




@bot.route('/', methods = ['GET','POST'])
def homePage():
	msg = request.form.get('body')
	
	if msg == None:
		return formm
	else:
		resp = predict(msg)
		return resp

	
@bot.route('/whatsapp/', methods = ['POST'])
def whatsapp():
	msg = request.form.get('Body')

	if msg not in [None,'']:
		resp = predict(msg.strip()	)
	else:
		resp = "Invalid input"
	msg =  MessagingResponse()
	msg.message(resp)
	return str(msg)
if __name__ == "__main__": 
	bot.run(debug = True)