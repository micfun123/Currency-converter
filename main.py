from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import converter

app = Flask(__name__ , template_folder='templates', static_folder='static')
app.secret_key = 'secret'

@app.route('/')
def index():
    return render_template('index.html')



app.run(debug=True)
