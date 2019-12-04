
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TimeField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length


class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

class Appointment(FlaskForm):
    appointment_title = StringField('Title', validators=[DataRequired()])
    appointment_date = DateField('Date (year-month-date)', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    location = StringField('Address', validators=[DataRequired()])
    customer_name = StringField('Name', validators=[DataRequired()])
    notes = StringField('Note', validators=[DataRequired()])
    appointment_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    submit = SubmitField('submit')

