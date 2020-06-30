from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'

if __name__=='_main': 
   #app.run('localhost', port=5000, debug=True)
   app.run(debug=True)    
