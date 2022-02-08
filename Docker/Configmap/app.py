from flask import Flask, render_template
import socket,os

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
greeting= os.environ['GREETING']
app = Flask(__name__)
say=1
user = "DevOps Team"
version = "1.0"

@app.route('/')
def main_entry():
    greeting= os.environ['GREETING']
    return render_template('index.html', message = greeting, ip = IPAddr, host_name = hostname, user = user, version = version )

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')