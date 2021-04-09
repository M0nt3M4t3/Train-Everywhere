# coding: utf-8
# Author: <>

from bottle import route, run, template, request, static_file
import os, sys
import pyodbc as db
import helpers
server = 'localhost'
username = 'sa'
password = '#'
database = 'Train_Everywhere'
connection = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' +
database + ';UID=' + username + ';PWD=' + password)
cursor = connection.cursor() # type: db.Cursor

@route("/")
def startpage(): 
    ''' Startsidan på hemsidan ''' 
    return template("startsida")

@route("/utegym")
def list_utegym():
    ''' Sidan som visar upp alla utegym som punktlista, funktionen tar alla utegyms namn som finns i vår databastabell "utegym"
    och returnar detta som en lista till HTML dokumentet utegym.html'''
    cursor.execute("SELECT Namn FROM Utegym ORDER BY Namn ASC")
    gyms = cursor.fetchall()
    return template("utegym", gyms=gyms)

@route('/utegym/<pagename>')
def show_article(pagename):
    ''' Sidan för varje utegym, funktionen tar pagename och hämtar ut beskrivning av databastabellen "utegym" för det utegym
    som det står i pagenamet att det är. Hämtar också ut alla recensioner ur databastabellen "recensioner" på samma viss.'''
    cursor.execute ("""SELECT Beskrivning FROM Utegym WHERE Namn=?""", pagename)
    data = cursor.fetchall()
    cursor.execute ("""
                    SELECT R.Namn, R.Betyg, R.Datum, R.Kommentar
                    FROM  Recensioner R JOIN Utegym U
                    ON R.Gym_id = U.Gym_id
                    WHERE U.Namn = ?
                    ORDER BY R.Datum;""", pagename)
    reviews = cursor.fetchall()
    text = data[0][0]
    text = helpers.nl2br(text)
    return template("show_utegym",pagename=pagename, data=text, reviews=reviews)

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8080, debug=True, reloader=True)#("hit med HTTP-metoden POST")

