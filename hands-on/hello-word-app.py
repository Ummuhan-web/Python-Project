from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return "ummuhan"+" yavuz"
   

if __name__=='__main__': 
   #app.run('localhost', port=5000, debug=True)
   app.run(debug=True)    
