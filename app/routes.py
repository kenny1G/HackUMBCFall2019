from app import app
from flask import render_template,flash,redirect
from app.forms import CompanyForm
from app.nasdaq import Nasdaq
from app.Scraper import Scraper

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])
def index():
    form = CompanyForm()
    if form.validate_on_submit():
        return redirect('/search/'+form.company_name.data)
    return render_template('index.html', title='Home', form = form)

@app.route('/search/<company_name>')
def company(company_name):
    scraper = Scraper(company_name, 'MSFT')
    dict = [scraper.get_reddit_titles()]
    return render_template('company.html', dict=dict, company_name=company_name)

@app.route('/<company_name>/<post_title>')
def info(company_name,post_title):
    scraper = Scraper(post_title,company_name)
    title = scraper.get_reddit_titles()[0]
    date = scraper.get_reddit_dates()[0]
    score = scraper.get_reddit_scores()[0]
    stock = scraper.get_stocks(date)
    print(stock)
    return render_template('info.html', title=title,date=date,score=score,stock=stock,company_name=company_name)
