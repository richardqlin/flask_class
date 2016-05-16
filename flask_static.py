'''
8 . Flask-Static Files
A web application often requires a static file such as a javascript
 file or a CSS file supporting the display of a web page. Usually, 
 the web server is configured to serve them for you, but during the development, 
 these files are served from static folder in your package or next to your module 
 and it will be available at /static on the application.
A special endpoint 'static' is used to generate URL for static files.
In the following example, a javascript function defined in hello.js is 
called on OnClick event of HTML button in index.html, which is rendered 
on '/' URL of the Flask application.

'''

from flask import Flask,render_template, make_response, request
app=Flask(__name__)

@app.route('/')

def index():
	return render_template('index.html')

'''
11 Flask - Cookies
A cookie is stored on a client's computer in 
the form of a text file. Its purpose is to 
remember and track data pertaining to a client's 
usage for better visitor experience and site statistics.
A Request object contains a cookie's attribute. It is a 
dictionary object of all the ctookie variables 
and their corresponding values, a clien has transmitted. In addition to it, a cookie also stores its expiry time, path and domain name of the site.
In Flask, cookies are set on response object. 
Use make_response() function to get response 
object from return value of a view function. 
After that, use the set_cookie() function of 
response object to store a cookie.
Reading back a cookie is easy. The get() 
method of request.cookies attribute is used 
to read a cookie. In the following Flask 
application, a simple form opens up as you 
visit '/' URL.

'''

@app.route('/cook')
def cookies():
	print 'hello cook'
	return render_template('cookies.html')

@app.route('/setcookies')
def setcookies():
	print 'hello set_cookie'
	if request.method=='POST':
		user=request.form['name']
		print user
		resp=make_response(render_template('readcookies.html'))
		#resp=make_response(url_for('getcookies'))
		resp.set_cookie('userID','name')
		return resp

@app.route('/getcookies')
def getcookies():
	name=request.cookies.get('userID')
	return '<h1> Welcome'+name+'</h1>'

if __name__=='__main__':
	app.run(debug=True)
