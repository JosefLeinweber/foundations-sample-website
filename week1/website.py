from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def first_page():
    return render_template('home.html', page_title="Home", sub_title="Home")


@app.route('/guidline')
def second_page():
    return render_template('guidline.html', page_title="Guidline", sub_title="Guidline")

@app.route('/feedback')
def third_page():
    return render_template('feedback.html', page_title="Feedback", sub_title="Feedback")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
