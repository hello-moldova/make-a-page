from flask import Flask, render_template, request
import requests



app = Flask(__name__, template_folder='./templates/')


@app.route('/')
def index():
    return render_template('AboutMe.html')

@app.route('/blog')
def blog():
    return render_template('Blog.html')


@app.route('/add', methods=['GET'])
def add():
	a = int(request.args['a'])
	b = int(request.args['b'])
	return "%d" % (a+b)



if __name__ == '__main__':
    app.run()