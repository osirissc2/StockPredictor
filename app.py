from flask import Flask, render_template
from BackEnd import parser
import os

template_dir = os.path.abspath('static')
app = Flask(__name__, template_folder=template_dir)
# url_for('static', filename='css/kronos.css')
# app = Flask(__name__, static_url_path='/FrontEnd')



@app.route("/")
def main():
    return render_template('index.html')

@app.route('/getDataSet/<query>')
def getDataSetWrapper(query):
	return parser.getDataSet(query)

if __name__ == "__main__":
    app.run()