'''
14. flask - upload file
'''

from flask import Flask, redirect, url_for, render_template,request

from werkzeug import secure_filename
app= Flask(__name__)

@app.route('/upload')
def upload_file():
	return render_template('upload.html')

@app.route('/uploader', methods=['GET','POST'])
def uploaded_file():
	if request.method=="POST":
		f= request.files['file']
		f.save(secure_filename(f.filename))
		return 'file uploaded successfully'


if __name__=='__main__':
	app.run(debug=True)