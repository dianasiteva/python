from flask import Flask, render_template, redirect, request


app = Flask(__name__)


full_stars = 0
empty_stars = 0
half_stars = 0
rating = 0


@app.route('/DrawRating')
def draw_rating():
    global rating
    rating = int(request.args['rating'])
    return calc_rating(rating)


@app.route('/')
def index():
    return render_template('index.html',
                           rating=rating,
                           full_stars=full_stars,
                           empty_stars=empty_stars,
                           half_stars=half_stars)


def calc_rating(rating):
    global full_stars
    full_stars = rating * 10 // 100

    global empty_stars
    empty_stars = (100 - rating) * 10 // 100

    global half_stars
    half_stars = 10 - full_stars - empty_stars
    return redirect('/')


if __name__ == '__main__':
    app.run()
