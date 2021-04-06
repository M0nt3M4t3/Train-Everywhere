# coding: utf-8
# Author: <>

from bottle import route, run, template, request, static_file
import os, sys
import json
import pyodbc as db
server = 'localhost'
username = 'sa'
password = 'Cas_775370149'
database = 'Train_Everywhere'
connection = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' +
database + ';UID=' + username + ';PWD=' + password)
cursor = connection.cursor() # type: db.Cursor

@route("/")
def startpage():  
    return template("startsida")

@route("/utegym")
def list_utegym():
    '''
    '''
    cursor.execute("SELECT Namn FROM Utegym")
    gyms = cursor.fetchall()
    return template("utegym", gyms=gyms)

@route('/utegym/<pagename>')
def show_article(pagename):
    '''
    '''
    cursor.execute ("""SELECT Omrade FROM Utegym WHERE Namn=?""", pagename)
    data = cursor.fetchall()
    cursor.execute ("""
                    SELECT R.Namn, R.Betyg, R.Datum, R.Kommentar
                    FROM  Recensioner R JOIN Utegym U
                    ON R.Gym_id = U.Gym_id
                    WHERE U.Namn = ?
                    ORDER BY R.Datum;""", pagename)
    reviews = cursor.fetchall()
    
    return template("show_utegym",pagename=pagename, data=data, reviews=reviews)

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8000, debug=True, reloader=True)#("hit med HTTP-metoden POST")

