from flask import Flask, render_template
import requests



app = Flask(__name__, template_folder='./templates/')



@app.route('/')
def index():
    return render_template('AboutMe.html')

@app.route('/blog')
def blog():
    return render_template('Blog.html')




if __name__ == '__main__':
    app.run()