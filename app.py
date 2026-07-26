from flask import Flask, render_template, request
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user (username,email,password,fm,country_id,phone) values (:username,:email,:password,:fm,:country_id,:phone)",request.form)
        user = query_db('select * from user')
        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")
    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user")

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into country (name) values (:name)",request.form)
        user = query_db('select * from country')
        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")
    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_city", methods=["GET","POST"])
def add_one_city():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into city (name) values (:name)",request.form)
        user = query_db('select * from city')
        return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")
    user = query_db('select * from city')
    one_user = query_db("select * from city limit 1", one=True)
    return render_template("cityform.html", citys=user, one_user=one_user, the_title="add new city")

@app.route("/add_one_trip", methods=["GET","POST"])
def add_one_trip():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into trip (user_id,country_id,city_id) values (:user_id,:country_id,:city_id)",request.form)
        user = query_db('select * from trip')
        return render_template("tripform.html", trips=user, one_user=one_user, the_title="add new trip")
    user = query_db('select * from trip')
    one_user = query_db("select * from trip limit 1", one=True)
    return render_template("tripform.html", trips=user, one_user=one_user, the_title="add new trip")

@app.route("/add_one_sport", methods=["GET","POST"])
def add_one_sport():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into sport (name) values (:name)",request.form)
        user = query_db('select * from sport')
        return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")
    user = query_db('select * from sport')
    one_user = query_db("select * from sport limit 1", one=True)
    return render_template("sportform.html", sports=user, one_user=one_user, the_title="add new sport")

@app.route("/add_one_record", methods=["GET","POST"])
def add_one_record():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into record (record_broken,sportsperson_name,country_id,city_id,year,sport_id) values (:record_broken,:sportsperson_name,:country_id,:city_id,:year,:sport_id)",request.form)
        user = query_db('select * from record')
        return render_template("recordform.html", records=user, one_user=one_user, the_title="add new record")
    user = query_db('select * from record')
    one_user = query_db("select * from record limit 1", one=True)
    return render_template("recordform.html", records=user, one_user=one_user, the_title="add new record")

@app.route("/add_one_user_broken_record", methods=["GET","POST"])
def add_one_user_broken_record():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into user_broken_record (broken_record,user_id,country_id,city_id,year,sport_id) values (:broken_record,:user_id,:country_id,:city_id,:year,:sport_id)",request.form)
        user = query_db('select * from user_broken_record')
        return render_template("user_broken_recordform.html", user_broken_records=user, one_user=one_user, the_title="add new user_broken_record")
    user = query_db('select * from user_broken_record')
    one_user = query_db("select * from user_broken_record limit 1", one=True)
    return render_template("user_broken_recordform.html", user_broken_records=user, one_user=one_user, the_title="add new user_broken_record")

@app.route("/add_one_trip_links", methods=["GET","POST"])
def add_one_trip_links():

    if request.method == 'POST':

        the_username = "anonyme"
        one_user = query_db("insert into trip_links (user_broken_record_id,trip_id) values (:user_broken_record_id,:trip_id)",request.form)
        user = query_db('select * from trip_links')
        return render_template("trip_linksform.html", trip_linkss=user, one_user=one_user, the_title="add new trip_links")
    user = query_db('select * from trip_links')
    one_user = query_db("select * from trip_links limit 1", one=True)
    return render_template("trip_linksform.html", trip_linkss=user, one_user=one_user, the_title="add new trip_links")

