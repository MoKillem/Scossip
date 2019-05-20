# Scossip
An interactive website connecting users across campus to a gossip website

--Design:
  Background:
    we want to create a platform for uni students to post everyday news on campus.
    
   Design:
    --users are all students and they are able to post things anonymously.
    --Other students will be able to react to the  post and comment on the post.
    --there is a seach bar at top of the mainpage for students to search up related posts.
    --There is a side bar on the left hand side for displaying top posts.
    
   More details on the buttons:
    --users have to log in to react to the posts.
    --There are three different types of reactions user can choose to react to the posts.
    --For each post, one user can only use one reaction. 
    --It is like how facebook different reactions works. If you have reacted to the post and you click the same reaction again, the           webpage will cancel your original reaction. If you click on a different on, the webpage will change your reaction status. 
    
   Sign up Page:
    -- there is a signup page for new users to signup
    -- they need to enter their personal details on signup page
    -- use wtform validators to check the format of some information
    -- like email must be in emails format, username must be 6-20 digits, password must be 8-20 digits etc
    -- after signup, user will be redirecrt to the login page
    
   Account page:
    -- There is an account page, user will be able to access all of his/her posted posts on their account page. 
    -- Users will be able to delete their previous posts and update their previous posts on account page.
    -- users will also be able to see their personal details on their account page
    
   Admin:
    -- Admin is able to delete user along with all their posts
    -- delete any user posts along with its comments
    -- edit any user posts
    
Development:
  
  --We first created the general html webpage for signup page and main page using html5. implement it with CSS and bootstrap (at this stage all links are just dummy links now)
  --Then we used javasctipt DOM to check the input tags to make sure all inputs for the signup page are in the corrent form, it will pop up alert window or show error messages if the inputs are not in the required format. (We realised that there is a better way using wtforms and jinja template to achieve this.
  -- after, we started developing the database with sqlalchemy.
  -- after, we tried out some simple flask  app routes and tried to merge the database with the app 
  
how to launch from local host:
run the python "run.py" file




