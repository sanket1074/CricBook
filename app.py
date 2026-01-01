from flask import Flask,render_template,request,redirect,session
import mysql.connector

app=Flask(__name__)
app.secret_key="123"

db=mysql.connector.connect(
 host="localhost",user="root",password="Sanket#8691",database="cric_book"
)
cur=db.cursor()

# ------------------ USER LOGIN ------------------
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='POST':
        cur.execute("select * from users where email=%s and password=%s",
        (request.form['email'],request.form['password']))
        u=cur.fetchone()
        if u and u[4]=='user':
            session['uid']=u[0]
            session['role']=u[4]
            return redirect('/user')
    return render_template('login.html')

# ------------------ ADMIN LOGIN ------------------
@app.route('/admin_login', methods=['POST'])
def admin_login():
    cur.execute("select * from users where email=%s and password=%s and role='admin'",
    (request.form['email'], request.form['password']))
    u = cur.fetchone()
    if u:
        session['uid'] = u[0]
        session['role'] = 'admin'
        return redirect('/admin')
    return redirect('/')

# ------------------ REGISTER ------------------
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        cur.execute("insert into users(name,email,password,role) values(%s,%s,%s,'user')",
        (request.form['name'],request.form['email'],request.form['password']))
        db.commit()
        return redirect('/')
    return render_template('register.html')

# ------------------ LOGOUT ------------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

# ------------------ ADMIN PANEL ------------------
@app.route('/admin')
def admin():
    if session.get('role')!='admin':
        return redirect('/')
    cur.execute("select * from matches")
    return render_template('admin_dashboard.html',data=cur.fetchall())

@app.route('/addmatch',methods=['POST'])
def addmatch():
    t=int(request.form['total'])
    p=int(request.form['price'])
    cur.execute("insert into matches(match_name,total_seats,available_seats,price) values(%s,%s,%s,%s)",
    (request.form['name'],t,t,p))
    db.commit()
    return redirect('/admin')

@app.route('/delete/<int:id>')
def delete(id):
    cur.execute("delete from matches where id=%s",(id,))
    db.commit()
    return redirect('/admin')

# ------------------ USER PANEL ------------------
@app.route('/user')
def user():
    if session.get('role')!='user':
        return redirect('/')
    cur.execute("select * from matches")
    return render_template('user_dashboard.html',data=cur.fetchall())

# ------------------ PAYMENT SYSTEM ------------------
@app.route('/payment/<int:id>',methods=['POST'])
def payment(id):
    seats=int(request.form['seats'])
    cur.execute("select match_name,price,available_seats from matches where id=%s",(id,))
    m=cur.fetchone()
    if seats>m[2]:
        return redirect('/user?msg=Not Enough Seats')
    total = seats * m[1]
    return render_template('payment.html',match=m[0],seats=seats,amount=total,mid=id)

@app.route('/pay/<int:id>/<int:seats>',methods=['POST'])
def pay(id,seats):
    cur.execute("update matches set available_seats=available_seats-%s where id=%s",(seats,id))
    cur.execute("insert into bookings(user_id,match_id,seats) values(%s,%s,%s)",
    (session['uid'],id,seats))
    db.commit()
    return redirect('/user?msg=Payment Successful & Booking Confirmed')

# ------------------ USER BOOKINGS ------------------
@app.route('/mybookings')
def mybookings():
    cur.execute("""select matches.match_name,bookings.seats
    from bookings join matches on bookings.match_id=matches.id
    where bookings.user_id=%s""",(session['uid'],))
    return render_template('mybookings.html',data=cur.fetchall())

# ------------------ ADMIN REPORT ------------------
@app.route('/report')
def report():
    if session.get('role')!='admin':
        return redirect('/')
    cur.execute("""select users.name,matches.match_name,bookings.seats
    from bookings join users on bookings.user_id=users.id
    join matches on bookings.match_id=matches.id""")
    return render_template('report.html',data=cur.fetchall())

app.run(debug=True)
