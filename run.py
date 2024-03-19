from flask import Flask

app = Flask(__name__)

users = {
   1:{'id': 1,
    'username': 'hb',
    'email': 'hb@fct.com',
    },
    2:{'id': 2,
    'username': 'zm',
    'email': 'zm@fct.com',
    },
}

posts = {
    1:{
        'author': 2,
        'title': 'Welcome to Flask!',
        'body': 'Welcome to our first full stack app, it\'s super simple and easy!'
    },
    2:{
        'author': 1,
        'title': 'Welcome to Flask Intro',
        'body': 'It\'s not actually THIS easy, stupid!'
}}

@app.route('/users')
def get_users():
    return {
        'users': list(users.values())
    }

@app.route('/user', methods=['POST'])
def create_user():
    
@app.route('/')
def land():
    return {
        "you've officially landed ON THE REAL PAGE!!!!!" : "welcome to baby's first flask app!"
    }

@app.route('/users')
def get_users():
    return {
        'users': list(users.values())
    }

@app.route('/user/<int:id>')
def get_ind_user(id):
    if users[id]:
        return {
            'user': users[id]
        }
    return {
        'UHOH, Something went wrong!': 'userID not found'
    }

@app.route('/user/', methods=['POST'])
def create_user():
    data = request.get_json()
    print(data)
    users[data['id']] = data
    return {
        "user created successfully": users[data['id']]
    }

@app.route('/user', methods=['PUT'])
def update_user():
    data = request.get_json()
    if data['id'] in users:
        users[data['id']] = data
    return {
        "user updated": users[data['id']]
    }

@app.route('/user/<int:id>', methods=['DELETE'])
def update_user(id):
    if data['id'] in users:
        del users[data['id']]
    return {
        "user deleted": users
    }