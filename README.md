# MovieBuff-API
An API that allows users to create, view and update their list of favourite movies!

# Requirements
Python (3.6)
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

5. Running tests

    Run the following command in order to run tests:

        $ python manage.py test

## Authors

* **Jonathan Kamau** - [Github Profile](https://github.com/jonathankamau)


## License

This project is licensed under the MIT License.
