from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Dictionary to store buzzer information
buzzers = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/host')
def host():
    return render_template('host.html')


@socketio.on('buzz')
def handle_buzz(data):
    name = data['name']
    emit('buzzed', {'name': name}, broadcast=True)
    # emit('update_buzzers', get_buzzed_participants(), broadcast=True)

@socketio.on('connect')
def handle_connect():
    emit('update_buzzers', get_buzzed_participants(), broadcast=True)

def get_buzzed_participants():
    return [name for name, info in buzzers.items() if info['buzzed']]

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5555)
