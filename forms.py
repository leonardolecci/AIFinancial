from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired



class TickerForm(FlaskForm):
  ticker =  StringField("Sticker", validators=[DataRequired()])
  quantity = StringField("Quantity", validators=[DataRequired()])
  date_purchased = StringField("Date Purchased", validators=[DataRequired()])
  date_sold = StringField("Date Sold", validators=[DataRequired()])
  submit = SubmitField("Add Sticker")

class PortfolioForm(FlaskForm):
  
  submit = SubmitField("Calculate Portfolio")

