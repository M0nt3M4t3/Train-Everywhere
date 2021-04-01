# coding: utf-8
# Author: <>

from bottle import route, run, template, request, static_file
import os, sys
import json

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
    pagename = (pagename)+".json"
    my_file = open(f"storage/{pagename}", "r")
    data = my_file.read()
    gym = json.loads(data)

    return template("show_utegym",pagename=pagename, gym=gym)

@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8000, debug=True, reloader=True)#("hit med HTTP-metoden POST")

