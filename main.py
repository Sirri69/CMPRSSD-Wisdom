from flask import Flask, render_template, request, jsonify
import json
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://Read_Only:read@cluster0.fn26y.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.blog_project
summaries = db.summaries

@app.route('/')
@app.route('/<path:path>')
def catch_all(path=None):
	authors = db.summaries.distinct('author')
	# print(authors)
	return render_template('index.html', authors=authors)


@app.route('/api/<int:page>')
@app.route('/api')
def api(page=1):
	if page <= 0:
		page = 1
	x = list(summaries.find({}, {'_id':0}).skip((page-1)*10).limit(10))
	if len(x) == 0:
		return jsonify([
			{
 
  "author": "Pranav",
  "title": "You seem lost",
  "link": "/",
  "content": "Click on the link to get back home"
}
		])
	return jsonify(x)


@app.route('/api/author/<author>')
def author(author=None):
	if author is not None:
		return jsonify(list(db.summaries.find({'author':author}, {'_id':0})))


app.run(host='127.0.0.1', port=8080, debug=True)

