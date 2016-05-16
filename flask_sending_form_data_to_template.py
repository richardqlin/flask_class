'''9. Flask - Request Object

The data from a client's web page is sent to the server as a global request object. In order to process the request data, it should be imported from the Flask module.
Important attributes of request object are listed below:
 Form: It is a dictionary object containing key and value pairs of form parameters and their values.
 args: parsed contents of query string which is part of URL after question mark (?).
 Cookies: dictionary object holding Cookie names and values.
 files: data pertaining to uploaded file.
 method: current request method.

10. Flask_sending form data to template
We have already seen that the http method can be specified in URL rule. The Form data received by the triggered function can collect it in the form of a dictionary object and forward it to a template to render it on a corresponding web page.
In the following example, '/' URL renders a web page (student.html) which has a form. The data filled in it is posted to the '/result' URL which triggers the result() function.
The results() function collects form data present in request.form in a dictionary object and sends it for rendering to table.html.
The template dynamically renders an HTML table of form data.
Given below is the Python code of application:

'''

from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
def student():
	return render_template('student.html')

@app.route('/result', methods=['POST','GET'])
def result():
	if request.method=='POST':
		result=request.form
		s=0
		c=0
		for k,v in result.items():
			if k!='Name':
				print k,v
				v=int(v)
				s+=v
				c+=1
		total=s
		ave=s/c
		return render_template('table.html', result=result,total=total,ave=ave)

if __name__=="__main__":
	app.run(debug=True)

