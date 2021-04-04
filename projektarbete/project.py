# coding: utf-8
# Author: <>

from bottle import route, run, template, request, static_file
import os, sys
import json
import pyodbc as db
server = 'localhost'
username = 'sa'
password = '#'
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
    path = "storage"
    dir_list = os.listdir(path) #Hämtar ut alla filer i storage och gör det till en lista.
    new_dir_list = [item[:-5] for item in dir_list] #Tar bort .json på alla filer (eftersom det är de sista 5 tecknena på alla filer)        
    
    return template("utegym", new_dir_list=new_dir_list)

@route('/utegym/<pagename>')
def show_article(pagename):
    '''
    '''
    name = (pagename)
    pagename = (pagename)+".json"
    my_file = open(f"storage/{pagename}", "r")
    data = my_file.read()
    gym = json.loads(data)
    cursor.execute ("""
                    SELECT R.Namn, R.Betyg, R.Datum, R.Kommentar
                    FROM  Recensioner R JOIN Utegym U
                    ON R.Gym_id = U.Gym_id
                    WHERE U.Namn = ?
                    ORDER BY R.Datum;""", name)
    reviews = cursor.fetchall()
    return template("show_utegym",pagename=pagename, gym=gym, reviews=reviews)

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8000, debug=True, reloader=True)#("hit med HTTP-metoden POST")

