
'''Flask - Routing

route() decorator in Flask is used to bind URL to a function.
For example:
'''
from flask import Flask, render_template
app= Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello World'
	



'''Here, URL'/hello' rule is bound to the hello_world function. 
As a result, if you visit http:localhost:5000/hello URL, the output of the hello_world function 
will be rendered in the browser.
'''	
'''Flask - Variable Rules
By adding variable parts to the rule parameter. This variable part is marked as 
<variable-name> that is passed as a keyword argument to the function with which the rule is associated.

route() decorator contains <name> variable part attached to URL '/hello'. Therefore,
if the http:localhost:5000/hello/
'''	

@app.route('/hello/<name>')
def hello_name(name):
	return 'Hello %s' %name

@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
	return 'Revision Number %f' % revNo


@app.route('/<user>')
def index(user):
	return render_template('hello.html', name=user)


@app.route('/mark/<int:score>')
def mark(score):
	return render_template('mark.html', marks=score)

@app.route('/result')
def result():

	d={'phy':50,'che':60,'maths':70}
	return render_template('table.html', result=d)

if __name__ == '__main__':
	app.run(debug=True)


