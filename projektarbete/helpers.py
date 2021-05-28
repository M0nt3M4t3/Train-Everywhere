# Author: Cassandra & Filip
# coding: utf-8
# pylint: disable=E1101

import os, sys
import mysql.connector
import safety
from datetime import date
import datetime

#establishing the connection
conn = mysql.connector.connect(
   user=safety.info[0], password=safety.info[1], host=safety.info[2], database=safety.info[3]
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()


def line_break(text):
    '''Lägger in <br> där det är splits i texten som skickas 
    in via parametern och returnerar sedan texten korrekt.'''
    
    return "<br>".join(text.splitlines())    

def get_info(gym):
    '''Hämtar ut beskrivning från ett utegym som skickas in via parametern 
    och returnerar sedan beskrivningen.'''

    gym_infoQuery = "SELECT Beskrivning FROM Utegym WHERE Namn= '%s'" % (gym)
    cursor.execute(gym_infoQuery)
    gym_info = cursor.fetchall()
    return gym_info

def get_picture(gym):
    '''Hämtar ut bild från Utegyms tabellen för gymmet som skickats med via 
    parametern'''

    gym_bildQuery = "SELECT Bild FROM Utegym WHERE Namn= '%s'" % (gym)
    cursor.execute(gym_bildQuery)
    picture = cursor.fetchall()
    return picture

def get_reviews(gym):
    '''Hämtar ut alla recensioner från valt gym som skickas in via parametern
    och returnerar de som en tuple.'''

    getReviewsQuery = """
                    SELECT R.Namn, R.Betyg, R.Datum, R.Kommentar
                    FROM  Recensioner R JOIN Utegym U
                    ON R.Gym_id = U.Gym_id
                    WHERE U.Namn = '%s'
                    ORDER BY R.Datum;""" % (gym)
    cursor.execute (getReviewsQuery)
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
    commentQuery = "INSERT INTO Recensioner set recension_id =%s, namn= %s, datum=%s, gym_id= %s, betyg= %s, kommentar= %s "
    cursor.execute(commentQuery, (review_id,name,date, gym_id, rating, comment))
    conn.commit()

def get_id():
    '''Tar ut alla recensions_id värden i recensionstabellen och 
    kollar sedan på det senaste värdet och plussar sedan en på det
    senaste värdet och returnerar sedan detta.'''
    
    try:
        cursor.execute ("""
                    SELECT Recension_id
                    FROM Recensioner""")
        reviews_id = cursor.fetchall()
        last = reviews_id[-1]
        value = last[0]
        new_value = value + 1  
        return new_value
    except IndexError:
        return 1

def get_day():
    '''Returnerar dagens datum.'''
    
    date_today = date.today()
    return date_today

def get_gym_id(gym):
    '''Returnerar gymmets gym_id som skickats in via parametern.'''

    gym_idQuery = """
            SELECT Gym_id
            FROM Utegym
            WHERE Namn = '%s'""" % (gym)
    cursor.execute (gym_idQuery)
    gym_id = cursor.fetchall()
    return gym_id[0][0]

def get_gyms():
    '''Returnerar alla Namn och bilder från Utegyms tabellen i Utegym 
    från databasen och i bokstavsordning.'''

    cursor.execute("SELECT Namn, Bild FROM Utegym ORDER BY Namn ASC")
    gyms = cursor.fetchall()
    return gyms

def get_gyms_average_5():
    '''Returnerar alla Namn och bilder från Utegyms tabellen där 
    Utegymmen har average 5 i Utegym från databasen och i 
    bokstavsordning.'''

    cursor.execute("""SELECT Namn, Bild 
                FROM info_with_average 
                WHERE Average >=4.50
                ORDER BY Namn ASC""")
    gyms = cursor.fetchall()
    return gyms

def get_gyms_average_4():
    '''Returnerar alla Namn och bilder från Utegyms tabellen där 
    Utegymmen har average 4 i Utegym från databasen och i 
    bokstavsordning.'''

    cursor.execute("""SELECT Namn, Bild 
                FROM info_with_average 
                WHERE Average BETWEEN 4 AND 4.49
                ORDER BY Namn ASC""")
    gyms = cursor.fetchall()
    return gyms

def get_gyms_average_3():
    '''Returnerar alla Namn och bilder från Utegyms tabellen där 
    Utegymmen har average 4 i Utegym från databasen och i 
    bokstavsordning.'''

    cursor.execute("""SELECT Namn, Bild 
                FROM info_with_average 
                WHERE Average BETWEEN 3 AND 3.49
                ORDER BY Namn ASC""")
    gyms = cursor.fetchall()
    return gyms

def get_gyms_average_2():
    '''Returnerar alla Namn och bilder från Utegyms tabellen där 
    Utegymmen har average 2 i Utegym från databasen och i 
    bokstavsordning.'''

    cursor.execute("""SELECT Namn, Bild 
                FROM info_with_average 
                WHERE Average BETWEEN 2 AND 2.49
                ORDER BY Namn ASC""")
    gyms = cursor.fetchall()
    return gyms

def get_gyms_average_1():
    '''Returnerar alla Namn och bilder från Utegyms tabellen där 
    Utegymmen har average 1 i Utegym från databasen och i 
    bokstavsordning.'''

    cursor.execute("""SELECT Namn, Bild 
                FROM info_with_average 
                WHERE Average BETWEEN 1 AND 1.49
                ORDER BY Namn ASC""")
    gyms = cursor.fetchall()
    return gyms

def get_average(gym):
    '''Returnerar medelvärdet på alla gymmets recensioner som skickas in via 
    parametern.'''
    try:
        id = get_gym_id(gym)
        averageQuery = """SELECT sum(Betyg) as total_betyg, 
                    count(Gym_id) as total_count
                    FROM Recensioner
                    WHERE gym_id= '%s'""" % (id)
        cursor.execute(averageQuery)
        count = cursor.fetchall()
        values_in_list = count[0]
        total_sum_reviews = values_in_list[0]
        total_reviews = values_in_list[1]
        average = round(total_sum_reviews / total_reviews)
        return average
    except TypeError:
        average = 0
        return average