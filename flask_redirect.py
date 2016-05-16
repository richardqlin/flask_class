'''
13. flask - redirct
'''

from flask import Flask, redirect, abort, url_for, render_template,request

app= Flask(__name__)

@app.route('/')
def index():
	return render_template('log_in.html')

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=='POST':
		if request.form['username']=='admin':
			return redirect(url_for('success'))
		else:
			abort(401)
	else:
		return redirect(url_for('index'))

@app.route('/success')
def  success():
	return 'logged in successfully'


if __name__=='__main__':
	app.run(debug=True)
