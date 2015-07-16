import sys
sys.path.insert(0, 'libs')
from bs4 import BeautifulSoup
import requests
from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for("static", filename="index.html"))

@app.route('/<int:post_id>/')
def teletext(post_id):
    s = requests.session()

    html_page = "http://37.152.64.32/" + str(post_id) + "/"
    myjson = s.get(html_page).text
    soup = BeautifulSoup(myjson, 'html.parser')
    #link = soup.find("link")['href'] = "/static/txt.css"
    #print(soup.prettify())
    #return soup.prettify()
    return soup.pre.prettify()

@app.route('/<int:post_id>/<int:sub>.html', endpoint="sub")
@app.route('/<int:post_id>/<int:sub>', endpoint="sub")
def teletext(post_id, sub):
    s = requests.session()
    html_page = "http://37.152.64.32/" +str(post_id) + "/" + ("%01d" % sub) + ".html"
    myjson = s.get(html_page).text
    soup = BeautifulSoup(myjson, 'html.parser')
    return soup.pre.prettify()

if __name__ == '__main__':
    app.run()
