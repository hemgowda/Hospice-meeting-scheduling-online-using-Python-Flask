from flask_wtf import Form 
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField 
from wtforms import validators, ValidationError 
from flask import Flask, render_template, request, flash
 
class ContactForm(Form): 
 #id_number = TextField("id",[validators.Required("Please enter your id.")])
 name = TextField("Name ",[validators.Required("Please enter your name.")]) 
 age= TextField("age ",[validators.Required("Please enter your age.")]) 
 gender = SelectField('gender', choices = [('male', 'male'),('female', 'female'),('not to say', 'not to say')]) 
 location = TextField("location",[validators.Required("Please enter your location")])
 phone = TextField("phone ",[validators.Required("Please enter your phone number")]) 
 schedule = TextField("schedule ",[validators.Required("Please enter schedul timing")]) 
 submit = SubmitField("Submit") 