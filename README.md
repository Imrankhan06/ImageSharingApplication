Image Sharing Application

REST APIs created using Django Rest Framework

Features:
* Signup and logging to user account
* Posting images
* Liking Photos
* Follow and Unfollow users
* Posts, follows and like with relevant permissions.

Project setup in local env:
1. Create a virtual env - python3 -m venv <name>(Ubuntu, Mac)
2. Activate the virtual env - source <path/bin/activate>
3. Install project dependencies - pip install -r requirements.txt
4. Migrate - python manage.py migrate
5. Run the Application - Python manage.py runserver

List of APIs:
1. Registration:
	
	Url: http://localhost:8000/api/user/signup/
	
	Method: POST

	payload: {
		'username':{username},
		'password':{password},
		'email':{email},
		'fullname':{fullname},
		'profile_pic':{file},
		'bio':{text}
	}

2. Login:
	
	Url: http://localhost:8000/api/user/login/
	
	Method: POST

	payload: {
		'username':{username},
		'password':{password}		
	}

	You will get AccessToken.

3. Post a photo:
	
	Url: http://localhost:8000/api/post/
	
	Method: POST

	payload: {
		'photo':{photo},
		'text':{text},
		'location':{location}
	}

	headers = {
  		'Authorization': {'Bearer Token'}
	}

4. Follow/Unfollow users:

	Url: http://localhost:8000/api/user/{username}/follow/
	
	Method: GET

	payload: {
		'username':{username},
		'password':{password}		
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}

5. Get Followers Count:

	Url: http://localhost:8000/api/user/{username}/get-followers/
	
	Method: GET

	payload: {
		'username':{username},
		'password':{password}
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}

6. Get Following Count:

	Url: http://localhost:8000/api/user/{username}/get-following/
	
	Method: GET

	payload: {
		'username':{username},
		'password':{password}		
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}

7. Like a post:

	Url: http://localhost:8000/api/post/like/{post_id}/
	Method: GET

	payload: {
		'username':{username},
		'password':{password}		
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}

8. Get list of images of a current user:

	Url: http://localhost:8000/api/user/home/
	
	Method: GET

	payload: {
		'username':{username},
		'password':{password}		
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}

9. Get list of posts of followed users:
	
	Url: http://localhost:8000/api/post/feeds/
	
	Method: GET

	payload: {
		'username':{username},
		'password':{password}		
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}

10. Get list of all users:

	Url: http://localhost:8000/api/user/{username}/allusers/
	
	Method: GET

	payload: {
		'username':{username},
		'password':{password}		
	}

	headers = {
  		'Authorization': {'Bearer <Token>'}
	}


Production SetUp:

Created a production_ready folder inside the ImageApplication folder which has core, dev, and prod py files to configure different envs.
