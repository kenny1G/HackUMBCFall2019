from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.nasdaq import Nasdaq

class CompanyForm(FlaskForm):
    company_name = StringField('Company', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def does_it_contain(self,company_name):
        if company_name.data.lower() in Nasdaq.companies.keys():
            return True
        for value in Nasdaq.companies.values():
            if company_name.data.lower() in value:
                return True

    def validate_company_name(self, company_name):
        value = self.does_it_contain(company_name)
        if not value:
            raise ValidationError('Sorry this company doesn\'t exist or is not in the Nasdaq listing')
