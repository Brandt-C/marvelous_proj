from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddForm(FlaskForm):
    s_name = StringField('Super Hero Name', validators=[DataRequired()])
    name = StringField('Given Name')
    description = StringField('Character description (limit 250 character length please!')
    comic_appearances = StringField('Comic book appearances')
    super_power = StringField('Super Powers')
    equipment = StringField('Equipment/tools/tech')
    submit = SubmitField()




# class RegForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     first_name = StringField('First Name')
#     last_name = StringField('Last Name')
#     password = PasswordField('Password', validators=[DataRequired()])
#     confirm_password = PasswordField('Confirm Password', validators=[EqualTo('password')])
#     submit = SubmitField()