from flask import Flask, request
bot = Flask(__name__)

from pred import predict



formm = """

<form action ="/whatsapp" method="post">
	<input type = "text" name="body">
	<input type = "submit" value="send">
</form>
"""

@bot.route('/whatsapp', methods = ['GET', 'POST'])
def homePage():
	msg = request.form.get('body')
	
	if msg == None:
		return formm
	else:
		resp = predict(msg)
		return resp

	return str(msg)

if __name__ == "__main__": 
	bot.run(debug = True)