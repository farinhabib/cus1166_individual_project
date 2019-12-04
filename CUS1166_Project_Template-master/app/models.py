
#from flask import url_for
from app import db

class Appointment(db.model):


    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_title = db.Column(db.Title, index=True)
    appointment_date = db.Column(db.Date, index=True)
    appointment_time = db.Column(db.Time, index=True)
    location_address = db.Column(db.Adress, index=True)
    customer_name = db.Column(db.Name, index=True)
    appointment_status = db.Column(db.String(128))

class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))
