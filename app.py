from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('init.html', flag=None)


@app.route('/state')
def state():
    return render_template('depression_state.html', flag='depression_state')


@app.route('/relation')
def relation():
    return render_template('depression_state.html', flag='relation')


@app.route('/compare')
def compare():
    return render_template('depression_state.html', flag='compare')


@app.route('/recommendation')
def recommendation():
    return render_template('depression_state.html', flag='recommendation')


if __name__ == '__main__':
    app.run()
