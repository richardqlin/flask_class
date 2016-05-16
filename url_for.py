'''
5.Flask- URL Biulding
url_for() function us useful for dynamically building a URL for a specific function.
The function acceptes the name of a function as first argument, and one or more keyword arguments, 
each corresponding to the variable part of URL
'''
from flask import Flask, redirect, url_for, request
app = Flask(__name__)
@app.route('/admin')
def hello_admin():
	return 'Hello Admin'
	
@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello %s as Guest' % guest
@app.route('/user/<name>')
def hello_user(name):
	if name=='admin':
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest',guest=name))

	
'''a function hello_user(name) which accepts a value to its argument from the URL
hello_user(name) function checks if an argument received matches 'admin' or not. 
If it matches, the application is redirected to the hello_admin function 
using url_for(), otherwise to the hello_guest() functionb passing the received argument
as guest parameter to it.

Open the browser and enter URL as:
http://localhost:5000/hello/admin
The application response in browser is:
Hello Admin
Enter the following URL in the browser:
http://localhost:5000/hello/mvl
The application response now changes to:
Hello mvl as Guest

6. Flask - HTTP methods

http protocal is the foundation of data communication in world wide web. Different
mothods of data retrieval from specified URL are defined in this protocal.
The following table summarizes different http methods:
GET
Sends data in unencrypted form to the server. Most common method.
HEAD
Same as GET, but without response body
POST
Used to send HTML form data to server. Data received by POST method is not cached by server.
PUT
Replaces all current representations of the target resource with the uploaded content.
DELETE
Removes all current representations of the target resource given by a URL

By default, the Flask route responds to the GET requests. However, this preference can
be altered by providing methods argument to route() decorator

In order to demonstrate the use of POST method in URL routing, first let us create an
HTML form and use the POST method to send form data to a URL

create templates
mkdir templates

Save the following script as login.html under templates folder

<html>
<body>
<form action="http://localhost:5000/login" method="post">
<p>Enter Name:</p>
<p><input type="text" name="nm" /></p>
<p><input type="submit" value="submit" /></p>
</form>
</body>
</html>


''' 



@app.route('/success/<name>')
def success(name):
	return 'welcome %s' % name
	
@app.route('/login',methods=['POST', 'GET'])
def login():
	if request.method=='POST':
		user=request.form['nm']
		return redirect(url_for('success',name=user))
	else:
		user=request.args.get('nm')
		return redirect(url_for('success',name=user))
if __name__ == '__main__':
	app.run(debug=True)