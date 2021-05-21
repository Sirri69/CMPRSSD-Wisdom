from flask import Flask, render_template, request, jsonify
import json
import time

app = Flask(__name__)


@app.route('/')
@app.route('/<path:path>')
def catch_all(path=None):
	return render_template('index2.html')


@app.route('/api/<int:page>')
@app.route('/api')
def api(page=1):
	time.sleep(3)
	x = json.load(open('static/summaries.json'))[page * 10 - 10:page * 10]
	print(jsonify(x))
	return jsonify(x)


@app.route('/api/all')
def all():
	x = json.load(open('static/summaries.json'))
	print(jsonify(x))
	return jsonify(x)


app.run(host='0.0.0.0', port=8080, debug=True)
