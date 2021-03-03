from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/first-page')
def first_page():
    return render_template('first-page.html', page_title="First Page", sub_title="Home")


@app.route('/second-page')
def second_page():
    return render_template('second-page.html', page_title="Second Page", sub_title="Guidline")

@app.route('/third-page')
def third_page():
    return render_template('third-page.html', page_title="Third Page", sub_title="Feedback")

# add additonal pages here using a similar format as above


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
