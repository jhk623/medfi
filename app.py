from flask import Flask, request, session, url_for, redirect, \
    render_template, g, flash, Blueprint


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('init.html', flag=None)


@app.route('/test')
def test():
    from datetime import time
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart.html', values=values, labels=labels, legend=legend)


if __name__ == "__main__":
    app.run(debug=True)


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
