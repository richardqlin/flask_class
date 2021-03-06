
'''
14. flask Message falshing

'''

from flask import Flask, flash, redirect, abort, url_for, render_template,request

app= Flask(__name__)

app.secret_key='hello'

@app.route('/')
def index():
	return render_template('ind.html')

@app.route('/login', methods=['GET','POST'])
def login():
	error=None
	if request.method=='POST':
		if request.form['username']!='admin' \
		 	or request.form['password']!='admin':
			error='Invalid username or password. Please try again!'	
		else:
			flash('You were successfully logged in')
			return redirect(url_for('index'))
	return render_template('logged.html',error=error)


@app.route('/success')
def  success():
	return 'logged in successfully'


if __name__=='__main__':
	app.run(debug=True)