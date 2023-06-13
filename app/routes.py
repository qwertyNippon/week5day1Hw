from app import app

from flask import render_template


@app.route('/')
def func1():
    Fav = [
        {
            'artist1': 'Drake',
            'artist2': 'Saint John',
            'artist3': '6lack',
            'artist4': 'Sabaton',
            'artist5': 'Jidena'
        }
    ]
    return render_template('index.html', Fav_list=Fav)

@app.route('/')
def func1():
    Fav = [
        {
            'artist1': 'Drake',
            'artist2': 'Saint John',
            'artist3': '6lack',
            'artist4': 'Sabaton',
            'artist5': 'Jidena'
        }
    ]
    return render_template('home.html', Fav_list=Fav)






# @app.route('/')
# def land():
#     return render_template('index.html')

# @app.route('/home')
# def home():
#     return {
#         'Welcome home': 'there is no place like here'
#     }

# @app.route('/test')
# def test():
#     return {
#         'Is this mic on?': 'is this function working????'
#     }

