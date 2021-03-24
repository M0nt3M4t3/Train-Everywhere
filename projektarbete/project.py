# coding: utf-8
# Author: <>

from bottle import route, run, template, request, static_file
import os, sys

@route("/")
def startpage():  
    return template("test_projekt")

    
@route("/static/<filename>")
def static_files(filename):
    return static_file(filename, root="static")

run(host='localhost', port=8000, debug=True, reloader=True)#("hit med HTTP-metoden POST")

