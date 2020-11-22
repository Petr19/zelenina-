from . import app
from flask import render_template


@app.route('/')
def index():
    pi=3.141519
    e=2.7
    title = 'Index'
    return render_template('base.html.j2', pi=pi, title=title)


@app.route('/info/')
def info():
    title = 'Info'
    return render_template('info.html.j2', title=title)


@app.route('/Kvetak/')
def kvetak():
    title = 'Květák'
    return render_template('Kvetak.html.j2', title=title)

@app.route('/Kapusta/')
def kapusta():
    title = 'Kapusta'
    return render_template('Kapusta.html.j2', title=title)


@app.route('/Banany/')
def banany():
    title = 'Banány'
    return render_template('Banany.html.j2', title=title)

