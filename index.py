from flask import Flask, jsonify,render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service')
def service():
    return render_template('service.html')


if __name__ == '__main__':
    app.run(port=3000)