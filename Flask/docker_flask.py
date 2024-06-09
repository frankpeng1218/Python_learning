from flask import Flask, render_template
from flask_admin import Admin

app = Flask(__name__)
admin = Admin(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/welcome')
def welcome():
    return '你好'


@app.route('/welcomehtml')
def welcomehtml():
    return render_template('welcome.html', message = '你好你好你好6')


if __name__ == '__main__':
    app.run()