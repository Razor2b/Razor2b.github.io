from flask import Flask
from flask import request

def login()
	if request.method == 'POST':
		firstname = request.form['firstname']
		lastname = request.form['lastname']
        email = request.form['email']
        tel = request.form['tel']

		
		# code that uses the data you've got
		# in our case, checking if the user exists
		# and logs them in, if not redirect to sign up
	else:
		# an exception