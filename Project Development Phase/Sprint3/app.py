from flask import Flask,render_template,request
import requests 
import ibm_db
app = Flask(__name__)





@app.route('/')
def index():
    title = "News App"
    return render_template('index.html',title=title)


@app.route('/register')
def register():
    title = "News App Register"
    return render_template('register_page.html',title=title)


@app.route('/login')
def login():
    title = "News App Login"
    return render_template('login.html',title = title)


@app.route('/',methods=["POST"])
def form():
    title = "Home"
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    username = request.form.get("uname")
    
    if not name or not email or not password:
        error_statement = "Please fill the details!!!"
        return render_template('home.html',title = title, name= name,email=email,password=password)
   
    else:
         url ="https://newsapi.org/v2/top-headlines?country=in&apiKey=7e535c4ed1044f4ab17b70d0efd2a84b"
         r = requests.get(url).json()
         case = {
             'articles': r['articles']
         }
         return render_template('home.html',title=title,name= name,email=email,password=password,cases = case)

if __name__ == '__main__':
    app.run(debug = True)


