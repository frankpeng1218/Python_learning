# app.py

from flask import Flask, render_template
from controller.user import user
from controller.user_detail import user_detail  # Import user_detail blueprint

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(user_detail)  # Register user_detail blueprint

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return '你好'

@app.route('/welcomehtml')
def welcomehtml():
    return render_template('welcome.html', message='你好你好你好6')

if __name__ == '__main__':
    # app.run()
    # app.run(host='0.0.0.0', port=5555)
    app.run(host='0.0.0.0', port=5555)

