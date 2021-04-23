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
    '''
    '''
    return "<br>".join(text.splitlines())

def call_info(name):
    '''
    '''
    cursor.execute ("""SELECT Beskrivning FROM Utegym WHERE Namn=?""", name)
    gym_info = cursor.fetchall()
    return gym_info

def call_reviews(gym):
    '''
    '''
    cursor.execute ("""
                    SELECT R.Namn, R.Betyg, R.Datum, R.Kommentar
                    FROM  Recensioner R JOIN Utegym U
                    ON R.Gym_id = U.Gym_id
                    WHERE U.Namn = ?
                    ORDER BY R.Datum;""", gym)
    reviews = cursor.fetchall()
    return reviews

def add_review(name, rating, comment, gym):
    '''
    '''
    review_id = get_id()
    name = (name)
    date = get_day()
    gym_id = get_gym_id(gym)
    rating = (rating)
    comment = (comment)
    cursor.execute("INSERT INTO Recensioner VALUES (?, ?, ?, ?, ?, ?)", review_id, name, date, gym_id, rating, comment)
    connection.commit()

def get_id():
    '''
    '''
    cursor.execute ("""
                SELECT Recension_id
                FROM Recensioner""")
    reviews_id = cursor.fetchall()
    last = reviews_id[-1]
    value = last[0]
    new_value = value + 1  
    return new_value

def get_day():
    '''
    '''
    date_today = date.today()
    return date_today

def get_gym_id(gym):
    '''
    '''
    cursor.execute ("""
            SELECT Gym_id
            FROM Utegym
            WHERE Namn = ?""", gym)
    gym_id = cursor.fetchall()
    gym_id = gym_id[0]
    gym_id = gym_id[0]
    return gym_id

def call_gyms():
    '''
    '''
    cursor.execute("SELECT Namn, Bild FROM Utegym ORDER BY Namn ASC")
    gyms = cursor.fetchall()
    return gyms