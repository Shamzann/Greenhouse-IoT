from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import pigpio
from time import sleep


LEDrød = 21
LEDgul = 20
pi = pigpio.pi()
app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('gul_skru_fra_browser')
def gulskru(data):
    gullysstyrke = int(data['gullysstyrke'])
    print(gullysstyrke)
    pi.write(LEDgul,gullysstyrke)

@socketio.on('rød_skru_fra_browser')
def rødskru(data):
    rødlysstyrke = int(data['rødlysstyrke'])
    print(rødlysstyrke)
    pi.write(LEDrød,rødlysstyrke)
@app.route('/')
def index():
    return render_template('oevelse4.html')

if __name__ == '__main__':
 socketio.run(app, host="0.0.0.0", debug=True)