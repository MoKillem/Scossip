#Modules Uses
from flask import current_app
from flask import render_template, url_for, flash, redirect, request
from flaskblog.models import User, Post, Button, Reaction,Comment
from flaskblog.forms import SignupForm, LoginForm, PostForm, ButtonForm, SelectForm, SearchForm,CommentForm
from flaskblog import app, db, bcrypt
from flask_login import current_user, login_user, login_required, logout_user, login_manager


posts = [
    {
        'name' : 'Juliet',
        'title' : 'Miss',
        'content' : 'wow',
    },
    {
        'name' : 'Moe',
        'title' : 'dh',
        'content' : 'hmmmm'
    }
]


    

#About page
@app.route("/about")
def about():
    return render_template('about.html')


#Signup page
@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('mainpage'))
    form = SignupForm()#Reference  signup form
    if form.validate_on_submit(): #If submitted
        hashed_passowrd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')#Encrypt the data into a corresponding hash
        user = User(first=form.first.data, last=form.last.data, username=form.username.data, email=form.email.data, password=hashed_passowrd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success') #Response if successfully created
        return redirect(url_for('mainpage'))
    return render_template('SignUpPage.html', form = form)



#Logout
@app.route("/logout")
@login_required
def logout():#Logout system
    logout_user()
    return redirect(url_for('mainpage'))




#Mainpage Page
@app.route("/")
@app.route("/mainpage", methods = ['GET', 'POST'])
def mainpage():
    Searching = SearchForm()
    form1 = ButtonForm()#ButtonForms
    posts_original = Post.query.all()#All possible posts
    form = LoginForm()#Reference Form   
    Postingform = PostForm()
    if posts_original == None:#If there are no posts render the page
        return render_template('mainpage.html')
    posts_reaction_count = []
    for post in posts_original:
        total = 0
        likes = 0
        shocks = 0
        laughs = 0
        for reaction in post.reactions:
            if reaction.state == True:
                total += 1
            if reaction.state == True and reaction.button_id == 1:
                likes += 1
            if reaction.state == True and reaction.button_id == 2:
                shocks += 1
            if reaction.state == True and reaction.button_id == 3:
                laughs += 1
        posts_reaction_count.append({'id':post.id, 'title':post.title, 'content': post.content, 'count': total, 'likes':likes, 'shocks': shocks, 'laughs': laughs})
    posts = posts_reaction_count
    return render_template('mainpage.html', Postingform= Postingform ,  Se = Searching,  posts = posts, form1=form1, form = form)#Render posts into main page 


@app.route('/mainpage/search', methods = ['GET', 'POST'])
def search():
    Searching = SearchForm()
    form1 = ButtonForm()#ButtonForms
    posts = Post.query.all()#All possible posts
    form = LoginForm()#Reference Form   
    Postingform = PostForm()
    postOutput =[]             
    if Searching.search.data and Searching.validate():#If form is validated
        for post in posts:
            key =Searching.keywords.data.lower().strip()
            if key in post.title.lower().strip() or key in post.content.lower().strip() or key in post.user.username :
                postOutput.append(post)
    if postOutput == None:#If there are no posts render the page
        return render_template('mainpage.html')
    posts_reaction_count = []
    for post in postOutput:
        total = 0
        likes = 0
        shocks = 0
        laughs = 0
        for reaction in post.reactions:
            if reaction.state == True:
                total += 1
            if reaction.state == True and reaction.button_id == 1:
                likes += 1
            if reaction.state == True and reaction.button_id == 2:
                shocks += 1
            if reaction.state == True and reaction.button_id == 3:
                laughs += 1
        posts_reaction_count.append({'id':post.id, 'title':post.title, 'content': post.content, 'count': total, 'likes':likes, 'shocks': shocks, 'laughs': laughs})
    posts = posts_reaction_count
    return render_template('mainpage.html', Postingform= Postingform ,  posts = posts, Se = Searching, form1=form1, form = form)

@app.route('/mainpage/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()#Reference Form   
    if form.submit.data and form.validate():#If form is validated
        user = User.query.filter_by(email=form.email.data).first()#Filter users by attempt to login 
        if user != None and bcrypt.check_password_hash(user.password, form.password.data): #Check users data and act accordingly
            login_user(user,remember=form.remember.data)#login the user
        else:
            if user == None:
                flash('User does not exit!',"loginError")
                return redirect(url_for('mainpage'))
            else:
                flash('Please check your email address and password',"loginError")
                return redirect(url_for('mainpage'))
    return redirect(url_for('mainpage'))




@app.route("/reaction/<post_id>", methods = ['GET', 'POST'])
@login_required
def reaction(post_id):
    form1 = ButtonForm()
    if form1.validate_on_submit(): #If submitted
        if current_user.is_authenticated:# if user is loged in
                #detect which button is pressed
            if form1.like.data:
                 button = Button.query.filter_by(id = 1).first()
            elif form1.shocked.data:
                button = Button.query.filter_by(id = 2).first()
            elif form1.laugh.data:
                button = Button.query.filter_by(id = 3).first()
            #something need to be added here to access current post loop 
            post = Post.query.filter_by(id = post_id).first()
            if Reaction.query.filter_by(post=post, user=current_user, state=True).first() == None:#if the user has no current reaction to the post
                reaction = Reaction(post=post, user=current_user, button=button)
                db.session.add(reaction)
                db.session.commit()#add this reaction to database (note: one user can only react once to the database with on button)
                return redirect(url_for('mainpage'))
            elif Reaction.query.filter_by(post=post, user=current_user, state=True).first() != None:#if user has has current reaction to the post
                if Reaction.query.filter_by(post=post, user=current_user, button=button, state=True).first() != None:#current reaction using the same button
                    current_reaction = Reaction.query.filter_by(post=post, user=current_user, button=button, state=True).first()
                    current_reaction.state = False#cancel the reaction
                    db.session.commit()
                    return redirect(url_for('mainpage'))
                elif Reaction.query.filter_by(post=post, user=current_user, button=button, state=True).first() == None:#current reaction is not the one pressed
                    previous_reaction = Reaction.query.filter_by(post=post, user=current_user, state=True).first()
                    previous_reaction.state = False#cancel the previous reactiion
                    new_reaction = Reaction(post=post, user=current_user, button=button)
                    db.session.add(new_reaction)
                    db.session.commit()#add this reaction to database 
                    return redirect(url_for('mainpage'))    
    return redirect(url_for('mainpage'))#Render posts into main page 


@app.route("/comment/<post_id>",methods = ['GET', 'POST'])
@login_required
def comments(post_id):
    comment_information = ""
    form = CommentForm()
    post = Post.query.filter_by(id = post_id).first()
    for comment in post.comments:
            comment_information += " " + comment.content
    
    if form.validate_on_submit(): #If submitted
        comment_sys = Comment(content = form.content.data,post_id = post_id, user = current_user)
        db.session.add(comment_sys)
        db.session.commit()
        return redirect(url_for('comments',post_id = post_id))
    return render_template('comments.html', posting = post , posT_id = post_id,comment_amal = comment_information , form = form)



@app.route("/post/new", methods = ['GET', 'POST'])
@login_required
def new_post():
    Searching = SearchForm()
    form1 = ButtonForm()#ButtonForms
    posts = Post.query.all()#All possible posts
    form = LoginForm()#Reference Form   
    Postingform = PostForm()
    if Postingform.submitPost.data and Postingform.validate():#User form to post
        post1 = Post(title = Postingform.title.data, content = Postingform.content.data, user = current_user)
        db.session.add(post1)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('mainpage'))
    return render_template('mainpage.html', Postingform= Postingform ,  Se = Searching, posts = posts, form1=form1, form = form)



@app.route("/display_top/<button>", methods = ['GET', 'POST'])
def display_top(button):
    Searching = SearchForm()
    form1 = ButtonForm()#ButtonForms
    posts_original = Post.query.all()#All possible posts
    form = LoginForm()#Reference Form   
    Postingform = PostForm()
    if posts_original == None:#If there are no posts render the page
        return render_template('mainpage.html')
    posts_reaction_count = []
    for post in posts_original:
        total = 0
        likes = 0
        shocks = 0
        laughs = 0
        for reaction in post.reactions:
            if reaction.state == True:
                total += 1
            if reaction.state == True and reaction.button_id == 1:
                likes += 1
            if reaction.state == True and reaction.button_id == 2:
                shocks += 1
            if reaction.state == True and reaction.button_id == 3:
                laughs += 1
        comments = len(post.comments)
        posts_reaction_count.append({'id':post.id, 'title':post.title, 'content': post.content, 'count': total, 'likes':likes, 'shocks': shocks, 'laughs': laughs, 'comments': comments})
    n = len(posts_reaction_count)
    for i in range(n):
        for j in range(0,n-i-1):
            if posts_reaction_count[j][button] < posts_reaction_count[j+1][button]:
                posts_reaction_count[j], posts_reaction_count[j+1] = posts_reaction_count[j+1] , posts_reaction_count[j]
    posts = posts_reaction_count
    return render_template('mainpage.html', Postingform= Postingform ,  Se = Searching ,  posts = posts, form1=form1, form = form)#Render posts into main page 


@app.route('/account', methods = ['GET', 'POST'])
@login_required
def account():
    Searching = SearchForm()
    posts = Post.query.filter_by(user_id = current_user.id)#All possible posts
    form = LoginForm()#Reference Form   

    return render_template('account.html', Se = Searching, posts = posts, form = form)


@app.route('/delete/<post_id>')
@login_required
def delete_post(post_id):
    post = Post.query.filter_by(id = post_id).first()
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('account'))


@app.route('/delete/<user_id>')
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id = user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('account'))


@app.route('/update/<post_id>')
@login_required
def update(post_id):
    post = Post.query.filter_by(id = post_id).first()
    return redirect(url_for('account'))