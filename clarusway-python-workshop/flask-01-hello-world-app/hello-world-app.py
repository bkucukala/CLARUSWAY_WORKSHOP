from flask import Flask
app = Flask(__name__)

@app.route("/")
def head():
    return ("Hello World!2")


@app.route('/bekir')
def second():
    return ("Hello Bekir You are in bekir!")

@app.route('/bekir/zeynep')
def third():
    return ("Hello Bekir You are in Zeynep!")

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id of this page is {id}'



if __name__=='__main__':
    app.run(debug = True)
    
