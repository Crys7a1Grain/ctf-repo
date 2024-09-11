from string import ascii_letters

from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        exp = request.form['Expression']
        for i in exp:
            if i in ascii_letters + '_':
                return render_template('index.html', exp='', result="Only [0-9] and special characters")
        try:
            result = eval(exp)
        except Exception as e:
            result = 'Something went wrong'
        return render_template('index.html', exp=exp, result=result)

    else:
        return render_template('index.html', exp='', result='')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=25555)
