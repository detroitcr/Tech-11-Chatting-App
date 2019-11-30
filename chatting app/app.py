
from flask import Flask, jsonify, request
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Detroit11'
socketio = SocketIO(app)


users = [
	{'id':2,'name':'Vikas Kumar','age':21},
	{'id':1,'name':'Vikas Rajput','age':20},
	{'id':3,'name':'Siddhant Kumar','age':20}
]

@app.route('/') #HTML endpoint
def index():
	return app.send_static_file('index.html')

@socketio.on('msg')
def handle_msg(data):
	socketio.emit('push',data,broadcast=True, include_self=False)


@app.route('/users')
def getUsers():
	print(users)
	return jsonify(users)

@app.route('/users/<id>') 
def geUser(id):
	result = list(filter(lambda u: str(u['id'])==id,users))
	#result = [ u for u in users if u['id']==id]
	return jsonify(result)

if __name__ == "__main__":
	socketio.run(app)


# from flask import Flask, jsonify, request

# app = Flask(__name__)

# users = [
# 	{'id':2,'name':'Vikas Kumar','age':21},
# 	{'id':1,'name':'Vikas Rajput','age':20},
# 	{'id':3,'name':'Siddhant Kumar','age':20}
# ]

# @app.route('/') #HTML endpoint
# def index():
# 	return app.send_static_file('index.html')

# @app.route('/users')
# def getUsers():
# 	print(users)
# 	return jsonify(users)

# @app.route('/users/<id>') 
# def geUser(id):
# 	result = list(filter(lambda u: str(u['id'])==id,users))
# 	#result = [ u for u in users if u['id']==id]
# 	return jsonify(result)


# if __name__ == "__main__":
# 	app.run()