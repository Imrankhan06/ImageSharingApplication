
# Image Sharing Application

REST APIs created using Django Rest Framework




## Features

- Signup and logging to user account
- Posting images
- Liking Photos
- Follow and Unfollow users
- Posts, follows and likes with relevant permissions.




## Project setup in local env

Clone the Project Repo

```bash
  mkdir <name>
  cd <name>
  git clone https://github.com/Imrankhan06/ImageSharingApplication
```
Create virtual environment(Ubuntu, Mac)

```bash
  python3 -m venv <name>
```
Activate virtual environment
```bash
  source <name>/bin/activate
```
Install project dependencies
```bash
  pip install -r requirements.txt
```
Migrate
```bash
  python manage.py migrate
```
Run the application
```bash
  python manage.py runserver
```

## List of APIs

* Registration:
```bash
    Url: http://localhost:8000/api/user/signup/
	
	Method: POST

	payload: {
		'username':<username>,
		'password':<password>,
		'email':<email>,
		'fullname':<fullname>,
		'profile_pic':<file>,
		'bio':<text>
	}
```
* Login:
```bash
    Url: http://localhost:8000/api/user/login/
	
	Method: POST

	payload: {
		'username':<username>,
		'password':<password>		
	}

	You will get AccessToken.
```
* Post a photo:
```bash
    Url: http://localhost:8000/api/post/
	
	Method: POST

	payload: {
		'photo':<photo>,
		'text':<text>,
		'location': <location>	
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
* Follow/Unfollow users:
```bash
    Url: http://localhost:8000/api/user/<username>/follow/
	
	Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
* Get Followers Count:
```bash
    Url: http://localhost:8000/api/user/<username>/get-followers/
	
	Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
* Get Following Count:
```bash
    Url: http://localhost:8000/api/user/<username>/get-following/
	
	Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
* Like a post:
```bash
    Url: http://localhost:8000/api/post/like/<post_id>/
	
    Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
* Get list of images of a current user:
```bash
    Url: http://localhost:8000/api/user/home/
	
	Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
*  Get list of posts of followed users:
```bash
    Url: http://localhost:8000/api/post/feeds/
	
	Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```
*  Get list of all users:
```bash
    Url: http://localhost:8000/api/user/<username>/allusers/
	
	Method: GET

	payload: {
		'username':<username>,
		'password':<password>		
	}

	headers = {
  		'Authorization': 'Bearer <Token>'
	}
```

## Production Setup:

Created a production_ready folder inside the ImageApplication folder which has core, dev, and prod py files to configure different envs.
