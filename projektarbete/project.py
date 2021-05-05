# coding: utf-8
# Author: Filip & Cassandra
# pylint: disable=E1101

from bottle import route, run, template, request, static_file, redirect 
import helpers

@route("/")
def start_page(): 
    ''' Startsidan på hemsidan.''' 
    return template("index")

@route("/gym")
def list_gym():
    ''' Sidan som visar upp alla utegym som punktlista, funktionen tar alla 
    utegyms namn som finns i vår databastabell "utegym" och returnar detta 
    som en lista till HTML dokumentet utegym.html.'''

    gyms = helpers.get_gyms()
    return template("gym", gyms=gyms)

@route("/gym/<pagename>")
def show_gym(pagename):
    ''' Sidan för alla utegym. Funktionen tar pagename och hämtar ut 
    beskrivning av databastabellen "utegym" för det utegym som det står
    i pagenamet att det är. Hämtar också ut alla recensioner ur 
    databastabellen "recensioner" på samma viss.'''
   
    gym_info = helpers.get_info(pagename)
    text = gym_info[0][0]
    text = helpers.nl2br(text)

    reviews = helpers.get_reviews(pagename) 
    average = helpers.get_average(pagename)

    picture = helpers.get_picture(pagename)
    picture = picture[0][0]
    print (picture)

    return template("show_gym", pagename=pagename, gym_info=text, reviews=reviews, average=average, picture=picture)

@route("/add_review", method="POST")
def update_review():
    '''Hämtar ut värdena i formuläret från show_gym och skickas in det i
    helpers funktion add_review.'''

    name = request.forms.get("name")
    rating = request.forms.get("rating") 
    comment = request.forms.get("comment")
    pagename = request.forms.get("gym")
    helpers.add_review(name, rating, comment, pagename)

    return redirect("/gym/" +pagename) 

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8000, debug=True, reloader=True)#("hit med HTTP-metoden POST")
