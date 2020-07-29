"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, redirect, url_for, request
from website import app
from website.pythonScripts import clubDataModule
import calendar

dataPath = 'website/data'
session = 'asdf1234'

@app.route('/')
@app.route('/home')
def home():
    if session == None:
        return redirect(url_for('login'))

    if clubDataModule.checkFile(dataPath):
        data = clubDataModule.openFile(dataPath)

        if len(data) == 3:
            clubData = clubDataModule.clubData(data[0][0], data[1][0], data[2][0])

    month = calendar.HTMLCalendar().formatmonth(2020, 7, True)

    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
        formattedMonth=month,
        description=clubData.description,
    )

@app.route('/contact')
def contact():
    if session == None:
        return redirect(url_for('login'))

    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    if session == None:
        return redirect(url_for('login'))

    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/login', methods=['GET', 'POST'])
def login():

    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'password':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))

    return render_template(
        'login.html',
        title='Login',
        error=error
    )

@app.route('/clubInfo/view')
@app.route('/clubInfo')
def clubInfo():
    if session == None:
        return redirect(url_for('login'))

    dataExists = clubDataModule.checkFile(dataPath)

    if dataExists:
        data = clubDataModule.openFile(dataPath)

        if len(data) == 3:
            clubData = clubDataModule.clubData(data[0][0], data[1][0], data[2][0])

            return render_template(
                'clubInfo/clubInfo.html',
                title='Club Info',
                year=datetime.now().year,
                dataExists=dataExists,
                team = clubData.title,
                coach = clubData.coach,
                )
    else:
        return render_template(
            'clubInfo/clubInfo.html',
            title='Club Info',
            year=datetime.now().year,
            dataExists=dataExists,
            )

@app.route('/clubInfo/edit', methods=['GET', 'POST'])
def editClubInfo():
    if session == None:
        return redirect(url_for('login'))

    if request.method == 'POST':
        clubInfo=[]
        clubInfo.append(request.form['clubname'])
        clubInfo.append(request.form['coach'])
        clubInfo.append(request.form['description'])

        clubDataModule.writeData(dataPath, clubInfo)

        return redirect(url_for("clubInfo"))

    if clubDataModule.checkData(dataPath):
        data = clubDataModule.openFile(dataPath)

        if len(data) == 3:
            clubData = clubDataModule.clubData(data[0][0], data[1][0], data[2][0])

        return render_template(
            'clubInfo/editClubInfo.html',
            title='Edit Club Info',
            year=datetime.now().year,
            defaultTitle=clubData.title,
            defaultCoach=clubData.coach,
            defaultDescription=clubData.description,
        )

    return render_template(
        'clubInfo/editClubInfo.html',
        title='Edit Club Info',
        year=datetime.now().year,
        defaultTitle="Club Name",
        defaultCoach="Club Coach",
        defaultDescription="Club Description",
    )

@app.route('/coaches')
def coachInfo():

    return render_template(
        'coachInfo/coachInfo.html',
        title='Coaches',

    )

@app.route('/coaches/edit')
def editCoachInfo():

    return render_template(
        'coachInfo/editCoachInfo.html',
        title='Edit Coach',

    )

@app.route('/coaches/add')
def addCoachInfo():

    return render_template(
        'coachInfo/addCoachInfo.html',
        title='Add Coach',

    )

@app.route('/squads')
def squadInfo():

    return render_template(
        'squadInfo/squadInfo.html',
        title='Squads',
    )

@app.route('/squads/add')
def addSquadInfo():

    return render_template(
        'squadInfo/addSquadsInfo.html',
        title='Add Squad',
    )

@app.route('/squads/edit')
def editSquadInfo():

    return render_template(
        'squadInfo/editSquadInfo.html',
        title='Edit Squad',
    )

@app.route('/calendar')
def viewCalendar():
    month = calendar.HTMLCalendar().formatmonth(2020, 7, True)

    return render_template(
        'calendar/viewCalendar.html',
        title='Calendar',
        formattedMonth=month,
        year=datetime.now().year,
    )