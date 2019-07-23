from app import app
from flask import render_template, request, redirect
from app.models import model

@app.route('/')
@app.route('/index')
def favoriteWord():
    return render_template('index.html')
    
@app.route('/characterCount', methods = ['GET', 'POST'])

def characterCount():
    if request.method == 'GET':
        return "You didn't fill it out. PERIOD. "
    else:
        favoriteWordData = dict(request.form)
        favoriteWord = favoriteWordData["favoriteWord"][0]
        # endthis = model.characterCount(favoriteWord)
        return render_template("favoriteWord.html", endthis = model.characterCount(favoriteWord))

