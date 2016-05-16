from flask import Flask,url_for,redirect,render_template, make_response, request,session

app=Flask(__name__)
app.secret_key='any random string'


@app.route('/')
def index():
	username=''
	if 'username' in session:
		username=session['username']
		return 'Logged in as ' + username+'<br>'+\
			"<b><a href='/logout'> Click here to log out</a></b>"

	return 'You are not logged in' + \
			"<b><a href='/login'></b>"+" click here to log in </b</a>"

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=='POST':
		session['username']=request.form['username']
		return redirect(url_for('index'))
	return '''
	<form action='' method='post'
	<p><input type='text' name='username'>
	<p><input type=submit value=Login>
	</form>
	'''

@app.route('/logout')
def logout():
	session.pop('username', None)
	return redirect(url_for('index'))


if __name__=='__main__':
	app.run(debug=True)
