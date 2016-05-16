from flask import Flask, render_template
app= Flask(__name__)


@app.route('/mark/<int:score>')
def mark(score):
	return render_template('mark.html', marks=score)

@app.route('/result')
def result():
	d={'phy':50,'che':60,'maths':70}
	return render_template('table.html', result=d)

if __name__ == '__main__':
	app.run(debug=True)
