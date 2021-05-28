from flask import Flask, render_template, request, jsonify
from flask_ngrok import run_with_ngrok
import json
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://Pranav:Pranavpatela1-kop@cluster0.fn26y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.blog_project
summaries = db.summaries

@app.route('/')
@app.route('/<path:path>')
def catch_all(path=None):
	authors = db.summaries.distinct('author')
	print(authors)
	return render_template('index.html', authors=authors)


@app.route('/api/<int:page>')
@app.route('/api')
def api(page=1):
	x = json.load(open('static/summaries.json', encoding='utf8'))[page * 10 - 10:page * 10]
	print(jsonify(x))
	return jsonify(x)


@app.route('/api/all')
def all():
	x = json.load(open('static/summaries.json', encoding='utf8'))
	print(jsonify(x))
	return jsonify(x)


@app.route('/api/<author>')
def author(author=None):
	if author is not None:
		return jsonify(list(db.summaries.find({'author':author}, {'_id':0})))


app.run(host='127.0.0.1', port=8080, debug=True)

