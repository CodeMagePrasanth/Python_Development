from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from datetime import datetime
from datetime import date
from werkzeug.utils import secure_filename
import urllib.request
import os
import time
import xlrd
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  charset="utf8",
  database="cyber_bullying"
)
app = Flask(__name__)
app.secret_key = 'abcdef'

PEOPLE_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER
@app.route('/', methods=['GET', 'POST'])
def home():
    msg=""
    ################3
    '''loc = ("dataset.xlsx") 
    # To open Workbook 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0)
    nr=sheet.nrows
    i=0
    while i<nr:
        print(sheet.cell_value(i, 0))
        i+=1'''
    ###################
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM register WHERE username = %s AND password = %s and dstatus=0', (uname, pwd))
        account = cursor.fetchone()
        if account:
            session['username'] = uname
            return redirect(url_for('profile'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('signup.html',msg=msg)
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'username' in session:
        uname = session['username']
        account=str(uname)
        file2 = open("uname.txt","w")
        file2.write(account)
        file2.close()
    filename=('uname.txt')
    fileread=open(filename,"r+")
    #uname=fileread.read()
    fileread.close()
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM register WHERE username = %s', (uname, ))
    data = cursor.fetchall()
##    cursor = mydb.cursor()
##    cursor.execute('SELECT * FROM register)
##    account = cursor.fetchall()
    return render_template('profile.html',data=data)
@app.route('/search', methods=['GET', 'POST'])
def search():
    if 'username' in session:
        uname = session['username']
    if request.method == "POST":
        search = request.form['search']
        cursor = mydb.cursor()
        cursor.execute("SELECT * from register WHERE name LIKE %s OR city LIKE %s  ",(search, search))
        data = cursor.fetchall()
        mydb.commit()
        #print(data)
        if len(data) == 0 and search == 'all':
            cursor.execute("SELECT * from register")
            mydb.commit()
            val = cursor.fetchall()
            return render_template('profile.html', val=val)
    return render_template('profile.html')
@app.route('/user_post', methods=['GET', 'POST'])
def user_post():
    st=0
    uname=""
    cnt=0
    act=""
    file_name=""
    if 'username' in session:
        uname = session['username']
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM register WHERE username = %s', (uname, ))
    data = cursor.fetchall()
    pcursor = mydb.cursor()
    pcursor.execute('SELECT * FROM user_post u,register r where u.status=0 && u.uname=r.username order by u.id desc')
    pdata = pcursor.fetchall()
    pcursor1 = mydb.cursor()
    pcursor1.execute('SELECT count(*) FROM user_post WHERE uname = %s and status=1', (uname, ))
    cnt = pcursor1.fetchone()[0]
    print(cnt)
    if request.method=='GET':
        act = request.args.get('act')
    if request.method == 'POST':
        post= request.form['txt_post']
        if 'file' not in request.files:
            flash('No file Part')
            return redirect(request.url)
        file= request.files['file']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT max(id)+1 FROM user_post")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        if file.filename == '':
            flash('No Select file')
            #return redirect(request.url)
        if file:
            fname = "P"+str(maxid)+file.filename
            file_name = secure_filename(fname)
            file.save(os.path.join(app.config['UPLOAD_FOLDER']+"/comments/", file_name))
            today = date.today()
        rdate = today.strftime("%d-%m-%Y")
        cursor2 = mydb.cursor()
        cursor2.execute("SELECT * FROM keyword_neg")
        ndata = cursor2.fetchall()
        print(ndata)
        '''for rs in ndata:
            print(rs[1])
            if post.find(rs[1]) != -1:
                act="yes"
                st=1
                break'''
        ########
        loc = ("dataset.xlsx")
        # To open Workbook
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        nr=sheet.nrows
        i=0
        while i<nr:
            print(sheet.cell_value(i, 0))
            dd=sheet.cell_value(i, 0)
            if post.find(dd) != -1:
                act="yes"
                st=1
                break
            i+=1
        ###########
        if cnt==4:
            act="warn"
        elif cnt>=5:
            pcursor2 = mydb.cursor()
            pcursor2.execute('update register set dstatus=1 where username = %s', (uname, ))
        mydb.commit()
        act="block"
        sql = "INSERT INTO user_post (id,uname,text_post,photo,rdate,status) VALUES(%s,%s,%s,%s,%s,%s)"
        val = (maxid,uname,post,file_name,rdate,st)
        mycursor.execute(sql,val)
        print(sql,val)
        mydb.commit()
        msg="Upload success"
        return redirect(url_for('user_post',act=act))
    return render_template('user_post.html',data=data,act=act,pdata=pdata)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if 'username' in session:
        uname = session['username']
    return render_template('contact.html')
@app.route('/edit_profile', methods=['GET', 'POST'])
def edit_profile():
    data=""
    if 'username' in session:
        uname = session['username']
        print(uname)
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM register WHERE username = %s', (uname, ))
        data = cursor.fetchall()
        print(data)
        return render_template('edit_profile.html',data=data)
    return render_template('edit_profile.html',data=data)
@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    uname=""
    if 'username' in session:
        uname = session['username']
        print(uname)
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM register WHERE username = %s', (uname, ))
        data = cursor.fetchall()
        print(data)
    uname=""
    print(uname)
    if request.method=='POST':
        name = request.form['name']
        dob = request.form['dob']
        contact = request.form['mobile']
        email = request.form['email']
        city = request.form['city']
        profession = request.form['prof']
        aadhar = request.form['aadhar']
        filename=('uname.txt')
        fileread=open(filename,"r+")
        uname=fileread.read()
        fileread.close()
        mycursor = mydb.cursor()
        sql=("update register set name=%s, dob=%s,mobile=%s,email=%s,city=%s,profession=%s,aadhar=%s, status=1 where username=%s")
        val=(name,dob, contact, email, city, profession, aadhar, uname)
        mycursor.execute(sql,val)
        mydb.commit()
        print(val)
        msg="success"
        return redirect(url_for('profile',msg=msg))
    return render_template('edit_profile.html')
app.route('/change_profile', methods=['GET', 'POST'])
def change_profile():
    uid=""
    print(uid)
    if 'username' in session:
        uname = session['username']
    print(uname)
    if request.method=='GET':
        act = request.args.get('act')
        uid = request.args.get('uname')
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file Part')
            return redirect(request.url)
        file= request.files['file']
        print(file)
        if file.filename == '':
            flash('No Select file')
            return redirect(request.url)
        if file:
            fname = file.filename
            fimg = uname+".jpg"
            file_name = secure_filename(fimg)
            print(file_name)
            file.save(os.path.join(app.config['UPLOAD_FOLDER']+"/photo/", file_name))
            mycursor = mydb.cursor()
            mycursor.execute("update register set photo=1 where username=%s", (uname, ))
            mydb.commit()
            msg="Upload success"
            return redirect(url_for('profile'))
    else:
        return render_template('change_profile.html')
@app.route('/signup',methods=['POST','GET'])
def signup():
    msg=""
    if request.method=='POST':
        name = request.form['name']
        gender = request.form['gender']
        dob = request.form['dob']
        contact = request.form['mobile']
        email = request.form['email']
        city = request.form['city']
        profession = request.form['prof']
        aadhar = request.form['aadhar']
        uname = request.form['uname']
        password1 = request.form['pass']
        today = date.today()
        rdate = today.strftime("%b-%d-%Y")
        mycursor1 = mydb.cursor()
        mycursor1.execute("SELECT * FROM register where aadhar=%s", (aadhar, ))
        dd = mycursor1.fetchall()
        dlen=len(dd)
        #print(dd)
        print(dlen)
        if dlen==0:
            mycursor = mydb.cursor()
            mycursor.execute("SELECT max(id)+1 FROM register")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            sql = "INSERT INTO register(id, name, gender, dob, mobile, email, city, profession, aadhar, username, password, rdate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (maxid, name, gender, dob, contact, email, city, profession, aadhar, uname, password1,  rdate)
            mycursor.execute(sql,val)
            mydb.commit()
            msg="success"
            return redirect(url_for('signup', msg=msg))
        else:
            msg="fail"
            return render_template('signin.html',msg=msg)
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    msg=""
    if request.method=='POST':
        uname=request.form['uname']
        pwd=request.form['pass']
        print(uname,pwd)
        cursor = mydb.cursor()
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (uname, pwd))
        account = cursor.fetchone()
        if account:
            return redirect(url_for('admin_user_view'))
        else:
            msg = 'Incorrect username/password!'
    return render_template('login.html',msg=msg)
@app.route('/admin_user_view', methods=['GET', 'POST'])
def admin_user_view():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM register where dstatus=0')
    data = cursor.fetchall()
    return render_template('admin_user_view.html',data=data)
@app.route('/admin_detected', methods=['GET', 'POST'])
def admin_detected():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM register where dstatus=1')
    data = cursor.fetchall()
    return render_template('admin_detected.html',data=data)
@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    #session.pop('username', None)
    return redirect(url_for('home'))
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
