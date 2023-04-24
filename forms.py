from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, DateField
from wtforms.validators import DataRequired



class TickerForm(FlaskForm):
  ticker =  StringField("Sticker", validators=[DataRequired()])
  quantity = StringField("Quantity", validators=[DataRequired()])
  date_purchased = DateField("Date Purchased", validators=[DataRequired()])
  date_sold = DateField("Date Sold")
  submit = SubmitField("Add Sticker")

class PortfolioForm(FlaskForm):
  
  submit = SubmitField("Calculate Portfolio")

