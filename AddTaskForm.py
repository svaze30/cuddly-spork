from wtforms import *
from wtforms.validators import *
from flask_wtf import *

class AddTaskForm(FlaskForm):
    TaskName=StringField('Task Name',validators=[data_required()])
    TaskDeadline=DateField('Task Deadline',validators=[data_required()])
    submit=SubmitField('Add Task')