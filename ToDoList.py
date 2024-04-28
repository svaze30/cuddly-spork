from flask import *
from tasks import *
from datetime import *
import datetime
from AddTaskForm import AddTaskForm
from LoginForm import SignUpForm, LogInForm,CommentForm, PostForm,interestForm
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo 
import urllib.parse
import base64
app=Flask(__name__)
app.config['SECRET_KEY']='87c725f6be51b16e19446e14b59149e7'
username = urllib.parse.quote_plus("shettynew17")
password = urllib.parse.quote_plus("spit@123")
app.config['MONGO_URI'] = f'mongodb+srv://{username}:{password}@cluster0.xpwn0wm.mongodb.net/Login'
bcrypt=Bcrypt(app)

mongo = PyMongo(app)

db = mongo.db.Login_details

NO_POSTS=2

tasks=[
    task("CCN Network Layer Assignment",datetime.date(2024,2,20),0),
    task("Revise LA Chapter 2",datetime.date(2024,7,19),1),
    task("Become a specialist on Codeforces",datetime.date(2024,9,18),2)
]

posts=[
    blogpost("Siddhesh Shrawne","Why do I need a C compiler to run python programs?",0),
    blogpost("Swaroop Vaze","How do I center a div??",1)
]

Users=[
    nuser("Dimsas",bcrypt.generate_password_hash("siddh")),
    nuser("Swaroop",bcrypt.generate_password_hash("Svaze"))
]

@app.route("/update_task_status/<int:task_id>", methods=['POST'])
def update_task_status(task_id):
    for task in tasks:
        if task.id == task_id:
            task.status = "DONE"
            break
    return redirect(url_for('goals'))




def createProfile(form):
    n_user=form.Username.data
    n_password=bcrypt.generate_password_hash(form.Password.data).decode('utf-8')
    new_obj=nuser(n_user,n_password)
    flag=0
    for user in Users:
        if user.username==n_user:
            flag=1
            break
    
    if flag==1:
        return False
    else:    
        Users.append(new_obj)
        return True
    

@app.route("/",methods=['GET','POST'])
def login():
    flag=0
    form=LogInForm()
    if(form.validate_on_submit()):
        for user in Users:
            if(user.username==form.Username.data):
                if(bcrypt.check_password_hash(user.password,form.Password.data)):
                    flag=1
                    session['username']=form.Username
                    session.modified=True
                    return redirect(url_for("maint"))
                else:
                    flash(f'Incorrect Password for {form.Username.data}','error')
                    return redirect(url_for("login"))
        if flag==0:
            flash(f'No account found for {form.Username.data}','error')
            return redirect(url_for("login"))        
    return render_template("Login.html",form=form)

@app.route("/SignIn",methods=['GET','POST'])
def signin():
    form=SignUpForm()
    if(form.validate_on_submit()):
        if createProfile(form):
            db.insert_one({'username':form.Username.data,
                           'password':form.Password.data})
            Users.append(nuser(form.Username.data,bcrypt.generate_password_hash(form.Password.data)))
            session['ProfilePic']=form.profilePic.data
            session['interests']=["","",""]
            session['bio']=""
            session.modified=True
            flash(f'Account Successfully created for {form.Username.data}','success')
            return redirect(url_for("login"))
        else:
            flash(f'Username not available','error')
            redirect(url_for("signin"))
    return render_template("Signin.html",form=form)

@app.route("/home", methods=['GET', 'POST'])
def maint():
    form=CommentForm()
    if(form.validate_on_submit()):
        post_id = int(request.args.get('srNo'))
        new_comment = comment(session['username'], form.Text.data)
        posts[post_id].comments.append(new_comment)
        flash('Comment posted Successfully!!', 'success')
        print("Comment posted!!!")
        return redirect(url_for("maint"))
    else:
        print()
    return render_template("home.html", posts=posts, form=form)

@app.route("/createPost",methods=['GET','POST'])
def createPost():
    global NO_POSTS
    form=PostForm()
    if(form.validate_on_submit()):
        posts.append(blogpost(session['username'],form.Text.data,NO_POSTS))
        NO_POSTS=NO_POSTS+1
        return redirect(url_for("maint"))
    return render_template("CreatePost.html",form=form)


@app.route("/profile",methods=['GET','POST'])
def profile():
    form=interestForm()
    image_data = session['ProfilePic']
    base64_encoded_image = base64.b64encode(image_data.encode()).decode('utf-8')
    if form.validate_on_submit():
        session['interests'][0]=form.inter1.data
        session['interests'][1]=form.inter2.data
        session['interests'][2]=form.inter3.data
        session['bio']=form.bio.data
        session.modified=True
        print(session['interests'])
        return redirect(url_for("profile"))
    return render_template("profile.html", base64_encoded_image=base64_encoded_image,username=session['username'],interests=session['interests'],form=form,bio=session['bio'])

@app.route("/Goals",methods=['POST','GET'])
def goals():
    form=AddTaskForm()
    if form.validate_on_submit():
        n_task=form.TaskName.data
        n_deadline=form.TaskDeadline.data
        obj=task(n_task,n_deadline,len(tasks))
        tasks.append(obj)
        return redirect(url_for('goals'))
    return render_template("AddGoal.html",form=form,tasks=tasks)

@app.route("/Notes",methods=['GET'])
def notes():
    return render_template("Notes.html")

if(__name__=='__main__'):
    app.run(debug=True)