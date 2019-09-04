# MovieBuff-API
An API that allows users to create, view and update their list of favourite movies!

#### URL endpoints

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `/api/v1/auth/register` | `POST`  | Register a new user|
|  `/api/v1/auth/login` | `POST` | Login and retrieve token|
| `/api/v1/movie/search?movie_name={{movie_name}}` | `GET` | Search for a movie by its name |
| `/api/v1/movie/add` | `POST` | Add a movie to the favourite movies list |
| `/api/v1/movie/favourites` | `GET` |  Retrieve all movies in favourite movies list |
| `/api/v1/movie/delete?id={{movie_id}}` | `DELETE` | Delete a movie in the favourite movies list |
| `/api/v1/user/update` | `PUT` |  Update the logged in user's username |

# Requirements
Python (3.7)
Flask (1.0.2)

# Installation
1. create a working directory

	      $ mkdir -p work-dir
	      $ cd workdir


2. clone this repo to local
    - Via SSH

          	git clone git@github.com:jonathankamau/MovieBuff-API.git

    - via HTTPS

          	git clone https://github.com/jonathankamau/MovieBuff-API.git
          
3. Navigate to project directory
    
    
      		$ cd MovieBuff-API
      		$ git checkout develop

4. Run the following commmand:

            $ python manage.py runserver

    This command creates a docker instance for the postgres database as well as for the API and runs the server as well.

    Open your browser to http://127.0.0.1:5000/ and you should see the browsable version of the API
    You can access the api online as well via this link http://movie-buff-api.herokuapp.com/

5. Running tests

    Run the following command in order to run tests:

        $ python manage.py test

## Authors

* **Jonathan Kamau** - [Github Profile](https://github.com/jonathankamau)


## License

This project is licensed under the MIT License.
