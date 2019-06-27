from flask import Flask
import requests

app = Flask(__name__, template_folder='./')


@app.route('/')
def index():
	return ("Hello World!")
    #return render_template('index.html')



if __name__ == '__main__':
    app.run()