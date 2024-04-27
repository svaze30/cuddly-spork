from flask import *
from tasks import *
from datetime import *
import datetime
from AddTaskForm import AddTaskForm
from LoginForm import SignUpForm, LogInForm
from flask_bcrypt import Bcrypt

app=Flask(__name__)
app.config['SECRET_KEY']='87c725f6be51b16e19446e14b59149e7'
bcrypt=Bcrypt(app)


tasks=[
    task("Get a Haircut",datetime.date(2024,2,20)),
    task("Buy Groceries",datetime.date(2024,1,19)),
    task("Attend Birthday",datetime.date(2024,1,18))
]

posts=[
    blogpost("Siddhesh Shrawne","What is 2+2???????"),
    blogpost("Swaroop Vaze","Aaye Newbie!!")
    
]



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
                    session
                    return redirect(url_for("user",username=form.Username.data))
                else:
                    flash(f'Incorrect Password for {form.Username.data}','error')
                    session['username']=user.username
                    session['profilePic']=user.profilePic
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
            flash(f'Account Successfully created for {form.Username.data}','success')
            return redirect(url_for("login"))
        else:
            flash(f'Username not available','error')
            redirect(url_for("signin"))
    return render_template("Signin.html",form=form)

@app.route("/maint",methods=['GET','POST'])
def maint():
    return render_template("home.html",posts=posts)

# @app.route("/<username>")
# def user(username):
#     return render_template("test.html",tasks=tasks)


setattr(tasks[2],'status',"DONE")
if(__name__=='__main__'):
    app.run(debug=True)