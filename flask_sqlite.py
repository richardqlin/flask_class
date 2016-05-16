from flask import Flask, render_template,request,flash
import sqlite3 as sql
app=Flask(__name__)
app.secret_key='development key'


@app.route('/')
def home():
	return render_template('home.html')

@app.route('/enternew')
def new_student():
	return render_template('student_new.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
	msg='error'
	if request.method=='POST':
		print request.method
		print 'hello'
		try:
			name=request.form['name']
			addr=request.form['add']
			city=request.form['city']
			pin=request.form['pin']
			print name,addr,city
			with sql.connect('database.db') as con:
				cur=con.cursor()
				cur.execute("insert into students (name, addr, city, pin) VALUES \
					(?,?,?,?)",(name,addr,city,pin))
				con.commit()
				msg='Record successfully added'
		except:
			con.rollback()
			msg='error in insert operation'
		finally:
			return render_template('result.html',msg=msg)
			con.close()

@app.route('/list')
def list():
	con=sql.connect('database.db')
	con.row_factory=sql.Row
	cur=con.cursor()
	cur.execute('select * from students')
	rows=cur.fetchall();
	return render_template('list.html',rows=rows)

if __name__=='__main__':
	app.run(debug=True)