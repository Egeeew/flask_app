from flask import Flask, render_template, request, redirect
import random as r

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('main_page.html')

@app.route('/not_ort', methods=["GET", "POST"])
def not_ort():
    ortalama = 0
    
    if request.method == "POST":
        if request.form.get('gonder'):
            sayi = int(request.form.get('sayi'))
            sayi2 = int(request.form.get('sayi2'))
            ortalama = (sayi + sayi2) / 2
            return render_template('not_ort.html', ortalama=ortalama)

    return render_template('not_ort.html', ortalama=ortalama)

@app.route('/sifre', methods=["GET", "POST"])
def sifre():
    sifre = "Şifreniz burada görünecek."
    char = "abcçdefgğhıijklmnoöprsştuüvyzABCÇDEFGHIİJKLMNOÖPRSŞTUÜVYZ.!'#^+$<%&/{[]}?*\_-|@,~<>0123456789"
    if request.method == "POST":
        if request.form.get('submit'):
            sifre = ""
            for i in range(8):    
                rnd = r.randint(0, len(char)-1)
                sifre += char[rnd]
            return render_template('sifre.html', sifre = sifre)

    return render_template('sifre.html', sifre = sifre)

@app.route('/vki', methods=["GET", "POST"])
def vki():
    m=0
    k=0
    vki = 0
    if request.method == "POST":
        if request.form.get('submit2'):
            m = int(request.form.get('cm'))/100
            k = int(request.form.get('kg'))
            vki = k/(m**2)
            return render_template('vki.html', vki = vki, m = m, k= k)

    return render_template('vki.html', vki = vki, m= m, k= k)

@app.route('/sayi', methods=["GET","POST"])
def sayi():
    x = 0
    y = 0
    sonuc = 0
    if request.method == "POST":
        if request.form.get('submit3'):
            x = int(request.form.get('x'))
            y = int(request.form.get('y'))
            sonuc = x**y
            return render_template('sayi.html', sonuc = sonuc, x = x, y = y)
    return render_template('sayi.html', sonuc = sonuc, x = x, y = y)