## coding: utf-8
# Author: Filip & Cassandra
# pylint: disable=E1101

from bottle import route, run, template, request, static_file, redirect 
import helpers

@route("/")
def start_page(): 
    ''' Startsidan på hemsidan.''' 
    return template("index")

@route("/gym")
def list_gyms():
    ''' Sidan som visar upp alla utegym som punktlista, funktionen tar 
    alla utegyms namn som finns i vår databastabell "utegym" och kör
    sedan igenom alla gymmen i vår funktion get_average där den lägger
    till genomsnittsbetyg i slutet av listan sedan returnar den detta 
    som en lista till HTML dokumentet utegym.html.'''

    gyms = helpers.get_gyms()
   
    list_gyms = []
    for gym in gyms: 
        list_gym = [gym[0], gym[1]]
        average = helpers.get_average(gym[0])
        list_gym.append(average) 
        list_gyms.append(list_gym)

    return template("list_gym", gyms=list_gyms)

@route ("/gym/5")
def list_of_gyms_with_5_average():
    ''' Sidan som visar upp alla utegym med genomsnittabetyg 5 
    som punktlista, funktionen tar alla utegyms namn som finns i 
    vår databastabell "utegym" och kör sedan igenom alla gymmen 
    i vår funktion get_average där den lägger till genomsnittsbetyg 
    i slutet av listan sedan returnar den detta som en lista till HTML 
    dokumentet utegym.html.'''

    gyms = helpers.get_gyms_average_5()
   
    list_gyms = []
    for gym in gyms: 
        list_gym = [gym[0], gym[1]]
        average = helpers.get_average(gym[0])
        list_gym.append(average) 
        list_gyms.append(list_gym)

    return template("list_gym_average_5", gyms=list_gyms)

@route ("/gym/4")
def list_of_gyms_with_4_average():
    ''' Sidan som visar upp alla utegym med genomsnittabetyg 4 
    som punktlista, funktionen tar alla utegyms namn som finns i 
    vår databastabell "utegym" och kör sedan igenom alla gymmen 
    i vår funktion get_average där den lägger till genomsnittsbetyg 
    i slutet av listan sedan returnar den detta som en lista till HTML 
    dokumentet utegym.html.'''

    gyms = helpers.get_gyms_average_4()
   
    list_gyms = []
    for gym in gyms: 
        list_gym = [gym[0], gym[1]]
        average = helpers.get_average(gym[0])
        list_gym.append(average) 
        list_gyms.append(list_gym)

    return template("list_gym_average_4", gyms=list_gyms)

@route ("/gym/3")
def list_of_gyms_with_3_average():
    ''' Sidan som visar upp alla utegym med genomsnittabetyg 3
    som punktlista, funktionen tar alla utegyms namn som finns i 
    vår databastabell "utegym" och kör sedan igenom alla gymmen 
    i vår funktion get_average där den lägger till genomsnittsbetyg 
    i slutet av listan sedan returnar den detta som en lista till HTML 
    dokumentet utegym.html.'''

    gyms = helpers.get_gyms_average_3()
   
    list_gyms = []
    for gym in gyms: 
        list_gym = [gym[0], gym[1]]
        average = helpers.get_average(gym[0])
        list_gym.append(average) 
        list_gyms.append(list_gym)

    return template("list_gym_average_3", gyms=list_gyms)

@route ("/gym/2")
def list_of_gyms_with_2_average():
    ''' Sidan som visar upp alla utegym med genomsnittabetyg 2 
    som punktlista, funktionen tar alla utegyms namn som finns i 
    vår databastabell "utegym" och kör sedan igenom alla gymmen 
    i vår funktion get_average där den lägger till genomsnittsbetyg 
    i slutet av listan sedan returnar den detta som en lista till HTML 
    dokumentet utegym.html.'''

    gyms = helpers.get_gyms_average_2()
   
    list_gyms = []
    for gym in gyms: 
        list_gym = [gym[0], gym[1]]
        average = helpers.get_average(gym[0])
        list_gym.append(average) 
        list_gyms.append(list_gym)

    return template("list_gym_average_2", gyms=list_gyms)

@route ("/gym/1")
def list_of_gyms_with_1_average():
    ''' Sidan som visar upp alla utegym med genomsnittabetyg 1 
    som punktlista, funktionen tar alla utegyms namn som finns i 
    vår databastabell "utegym" och kör sedan igenom alla gymmen 
    i vår funktion get_average där den lägger till genomsnittsbetyg 
    i slutet av listan sedan returnar den detta som en lista till HTML 
    dokumentet utegym.html.'''

    gyms = helpers.get_gyms_average_1()
   
    list_gyms = []
    for gym in gyms: 
        list_gym = [gym[0], gym[1]]
        average = helpers.get_average(gym[0])
        list_gym.append(average) 
        list_gyms.append(list_gym)

    return template("list_gym_average_1", gyms=list_gyms)

@route("/gym/<pagename>")
def show_gym(pagename):
    ''' Sidan för alla utegym. Funktionen tar pagename och hämtar 
    ut beskrivning av databastabellen "utegym" för det utegym som 
    det står i pagenamet att det är. Hämtar också ut alla recensioner 
    ur databastabellen "recensioner" på samma viss.'''
   
    gym_info = helpers.get_info(pagename)
    description = gym_info[0][0]
    description = helpers.line_break(description)

    reviews = helpers.get_reviews(pagename) 
    average = helpers.get_average(pagename)

    picture = helpers.get_picture(pagename)
    picture = picture[0][0]

    return template("show_gym", pagename=pagename, gym_info=description,
    reviews=reviews, average=average, picture=picture)

@route("/add_review", method="POST")
def update_review():
    '''Hämtar ut värdena i formuläret från show_gym och skickas in det 
    i helpers funktion add_review.'''

    name = request.forms.name
    rating = request.forms.rating
    comment = request.forms.comment
    pagename = request.forms.gym
    helpers.add_review(name, rating, comment, pagename)

    return redirect("/gym/" +pagename) 

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8080, debug=True, reloader=True)
