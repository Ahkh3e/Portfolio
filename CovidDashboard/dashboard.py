from flask import Flask, render_template #this has changed

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') #this has changed


if __name__ == '__main__':
    app.run()
