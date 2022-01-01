
from flask import Flask,request
from flask import render_template
from reserch import reserch4letters
# Flask: 中央登记中心
app = Flask(__name__)

@app.route('/',methods=['GET'])
def hello_world():  # put application's code here
    return render_template('hello.html')

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

# [POST] 实现用户输入,点击提交，将数据提交到 /result
@app.route('/result',methods=['POST'])
def result():
    py_firstname = request.form['firstname']
    py_lastname = request.form['lastname']
    py_fullname = py_firstname.title()+' '+py_lastname.title()

    py_word = request.form['word']
    py_vowels = request.form['vowels']
    py_found = reserch4letters(py_vowels,py_word)

    return render_template('result.html',
                           fullname = py_fullname,
                           found = py_found)

@app.route('/result2',methods=['POST',"GET"])
def result2():
    return render_template('result2.html')


@app.route('/buy',methods=['GET','POST'])
def buy():
    return render_template('buy.html')

@app.route('/buying',methods=['GET','POST'])
def buying():

    return render_template('buying.html')
if __name__ == '__main__':
    app.run(host='127.0.0.1',part=5000,debug=True)


