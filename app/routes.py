from app import app
from flask import render_template,flash,redirect
from app.forms import CompanyForm
from app.nasdaq import Nasdaq

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form = CompanyForm()
    if form.validate_on_submit():
        print(form.company_name.data)
        return redirect('/index')
    return render_template('index.html', title='Home', form = form)
