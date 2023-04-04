from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired



class TickerForm(FlaskForm):
  ticker =  StringField("Sticker", validators=[DataRequired()])
  quantity = StringField("Quantity", validators=[DataRequired()])
  submit = SubmitField("Add Sticker")

