from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return 'hola mundo'

if __name__=='__main__':
    app.run()