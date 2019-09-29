from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.nasdaq import Nasdaq

class CompanyForm(FlaskForm):
    company_name = StringField('Company', validators=[DataRequired()])
    submit = SubmitField('Bet')

    def validate_company_name(self, company_name):
         if not company_name.data.lower() in Nasdaq.companies.keys():
             if not company_name.data.lower() in Nasdaq.companies.values():
                 raise ValidationError('Sorry this company doesn\'t exist or is not in the S&P 500')
