# Author: Cassandra & Filip
# coding: utf-8

import os, sys
import pyodbc as db
import safety
from datetime import date
import datetime

server = 'localhost'
username = safety.CW[0]
password = safety.CW[1]
database = 'Train_Everywhere'
connection = db.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' +
database + ';UID=' + username + ';PWD=' + password)
cursor = connection.cursor() # type: db.Cursor


def nl2br(text):
    '''Lägger in <br> där det är splits i texten som skickas in via 
    parametern och returnerar sedan texten korrekt.'''
    
    return "<br>".join(text.splitlines())

def get_info(name):
    '''Hämtar ut beskrivning från ett utegym som skickas in via parametern 
    och returnerar sedan beskrivningen.'''
    
    cursor.execute ("""SELECT Beskrivning FROM Utegym WHERE Namn=?""", name)
    gym_info = cursor.fetchall()
    return gym_info

def get_picture(name):
    '''Hämtar ut bild från Utegyms tabellen för gymmet som skickats med via 
    parametern'''

    cursor.execute ("""SELECT Bild FROM Utegym WHERE Namn=?""", name)
    picture = cursor.fetchall()
    return picture

def get_reviews(gym):
    '''Hämtar ut alla recensioner från valt gym som skickas in via parametern
    och returnerar de som en tuple.'''
   
    cursor.execute ("""
                    SELECT R.Namn, R.Betyg, R.Datum, R.Kommentar
                    FROM  Recensioner R JOIN Utegym U
                    ON R.Gym_id = U.Gym_id
                    WHERE U.Namn = ?
                    ORDER BY R.Datum;""", gym)
    reviews = cursor.fetchall()
    return reviews

def add_review(name, rating, comment, gym):
    '''Lägger in nya recensioner från formuläret i show_gym, kallar även på
    olika andra funktioner för att få all information som krävs i 
    recensions-tabellen.'''

    review_id = get_id()
    name = (name)
    date = get_day()
    gym_id = get_gym_id(gym)
    rating = (rating)
    comment = (comment)
    cursor.execute("""INSERT INTO Recensioner VALUES (?, ?, ?, ?, ?, ?)"""
                    , review_id, name, date, gym_id, rating, comment)
    connection.commit()

def get_id():
    '''Tar ut alla recensions_id värden i recensionstabellen och 
    kollar sedan på det senaste värdet och plussar sedan en på det
    senaste värdet och returnerar sedan detta.'''
    
    cursor.execute ("""
                SELECT Recension_id
                FROM Recensioner""")
    reviews_id = cursor.fetchall()
    last = reviews_id[-1]
    value = last[0]
    new_value = value + 1  
    return new_value

def get_day():
    '''Returnerar dagens datum.'''
    
    date_today = date.today()
    return date_today

def get_gym_id(gym):
    '''Returnerar gymmets gym_id som skickats in via parametern.'''

    cursor.execute ("""
            SELECT Gym_id
            FROM Utegym
            WHERE Namn = ?""", gym)
    gym_id = cursor.fetchall()
    gym_id = gym_id[0]
    gym_id = gym_id[0]
    return gym_id

def get_gyms():
    '''Returnerar alla Namn och bilder från Utegyms tabellen i Utegym från 
    databasen och i bokstavsordning.'''

    cursor.execute("SELECT Namn, Bild FROM Utegym ORDER BY Namn ASC")
    gyms = cursor.fetchall()
    return gyms

def get_average(gym):
    '''Returnerar medelvärdet på alla gymmets recensioner som skickas in via 
    parametern.'''
    try:
        id = get_gym_id(gym)
        cursor.execute("""SELECT sum(Betyg) as total_betyg, 
                    count(Gym_id) as total_count
                    FROM Recensioner
                    WHERE gym_id= ?""", id)
        count = cursor.fetchall()
        values_in_list = count[0]
        total_sum_reviews = values_in_list[0]
        total_reviews = values_in_list[1]
        average = round(total_sum_reviews / total_reviews)
        return average
    except TypeError:
        average = 0
        return average