from flask import Flask, request
bot = Flask(__name__)





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
		return f"the message you entered is {msg}"

	return str(msg)


bot.run()
