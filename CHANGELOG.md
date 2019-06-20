Changelog
=========

2.0.0
------------
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/915fd2448b2b02843282df109c7fae82bb5bd05a">view commit &bull;</a> ch-add-staging-env-to-config  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/f891058daf5faca099b9bde94f369892c557a7dd">view commit &bull;</a> add new api details  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/2617de729266927ceec64e22204668e3929188b0">view commit &bull;</a> make modifications to gitignore  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/661df608c6dec0b77e3fd69da480070e05c3fcb5">view commit &bull;</a> edit caching solution  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/95093ad5f07619574469658d58d41da6175d9a8d">view commit &bull;</a> chore(database): add configurations for postgres  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/33fc4ba6729029edbf1ddd5b0cabe5e9c83c569f">view commit &bull;</a> modify the database fields in sqlalchemy  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/f056903ce71c283d445ce2a6b121831664e3b87d">view commit &bull;</a> chore(database): add sqlalchemy configs and migrate command  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/57dc235fec767f3bd4452f07e7ccafdc235188da">view commit &bull;</a> chore(database): refactor code to include sqlalchemy query functions and modify the database model - add command to migrate the database as well.
 Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/66ecb8594b4d705125c808938123db732b7c4099">view commit &bull;</a> add ratings and categories endpoints and refactor existing ones  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/d1f09a5296f8b42a6dcdf56291d040feb8fc4567">view commit &bull;</a> feat(endpoints): add the categories and ratings endpoints and refactor the existing ones [Finishes #160940895]
 Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/6f1ee0ce8c1bd50926a0c58ee91a60ca82bfab19">view commit &bull;</a> remove all print statements used while debugging  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/b8dc601dc6d2f851048ff63aded685e90ff2aeae">view commit &bull;</a> add functionality to delete category by its id  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/c7c5b3dfca82861e3eb5f785e73feab471c9a5a7">view commit &bull;</a> chore(dependecies): update dependecies to meet security requirements  Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>
<li> <a href="http://github.com/jonathankamau/MovieBuff-API/commit/79db3fb2bbf968882a8cb7bd15072c31000992fe">view commit &bull;</a> chore(api-version): update the api version The current API version is still 1.2.0 and doesn't speak
to the changes made in the aftermath.

This fixes that by updating the version to v2.

[Finishes ##166822466]
 Author: Jonathan Kamau, Commiter: Jonathan Kamau</li>

1.1.0
------------
- Add production config value. [Jonathan Kamau]

1.0.0
------------
- Merge pull request #12 from jonathankamau/ch-deploy-api-to-
  heroku-160480684. [Jonathan Kamau]

  #160480684 Add heroku settings and test deployment to heroku
- Make fix to procfile. [Jonathan Kamau]
- Change configs. [Jonathan Kamau]
- Fix heroku config. [Jonathan Kamau]
- Fix heroku config. [Jonathan Kamau]
- Fix heroku config. [Jonathan Kamau]
- Fix procfile configuration. [Jonathan Kamau]
- Fix procfile configuration. [Jonathan Kamau]
- Fix procfile configuration. [Jonathan Kamau]
- Fix procfile configuration. [Jonathan Kamau]
- Fix procfile configuration. [Jonathan Kamau]
- Fix procfile configuration. [Jonathan Kamau]
- Add configs for staging and production environments. [Jonathan Kamau]
- Install gunicorn. [Jonathan Kamau]
- Chore(deploy): deploy the api to heroku. [Jonathan Kamau]
- Merge pull request #11 from jonathankamau/ch-registration-endpoint-
  tests-160480553. [Jonathan Kamau]

  #160480553 Registration endpoint tests
- Chore(unittests): add unittests for the registration endpoint.
  [Jonathan Kamau]

  [Finishes #160480553]
- Chore(tests): add unittests for user registration. [Jonathan Kamau]

  [Finishes #160480553]
- Merge pull request #10 from jonathankamau/ft-edit-user-
  details-160480630. [Jonathan Kamau]

  #160480630 Update user's username
- Feat(update-user-details): update user's username. [Jonathan Kamau]

  [Delivers #160480630]
- Merge pull request #9 from jonathankamau/ft-delete-movie-160480618.
  [Jonathan Kamau]

  #160480618 Delete movie endpoint
- Feat(delete-movie): delete movie endpoint. [Jonathan Kamau]

  [Delivers #160480618]
- Merge pull request #8 from jonathankamau/ft-view-favourite-movies-
  list-160480576. [Jonathan Kamau]

  #160480576 get favourite movies endpoint
- Feat(view-favourite-movies): view favourite movies endpoint. [Jonathan
  Kamau]

  [Finishes #160480576]
- Remove the token verification file since it's no longer being used.
  [Jonathan Kamau]
- Add query functions to models. [Jonathan Kamau]
- Add the token decorator. [Jonathan Kamau]
- Add a unique generator for the user's id. [Jonathan Kamau]
- Include the user's id when commiting the selected movie to db.
  [Jonathan Kamau]
- Add the import for view_favourite_movies. [Jonathan Kamau]
- Merge pull request #7 from jonathankamau/ft-add-authorization-for-
  endpoints-160718883. [Jonathan Kamau]

  #160718883 Include authorization for the movie endpoints
- Feat(authorization): include authorization for the movie endpoints.
  [Jonathan Kamau]

  Currently there isn't any user authorization set up for the endpoints.
  This fixes that by adding verification for the user token.

  [Finishes #160718883]
- Merge pull request #6 from jonathankamau/ft-add-favourite-
  movies-160480589. [Jonathan Kamau]

  #160480589 Create the add movie endpoint
- Feat(add-movies): add movie endpoint. [Jonathan Kamau]

  Currently there isn't a way for new movies to be addded to the
  favourites list.

  This solves that by creating the endpoint to allow the user to
  add movies to his favourites list from a search result.

  [Finishes #160480589]
- Make modifications to the cache helper functions. [Jonathan Kamau]
- Add to gitignore. [Jonathan Kamau]
- Add redis as a dependency. [Jonathan Kamau]
- Add the add movie endpoint. [Jonathan Kamau]
- Format the schema file. [Jonathan Kamau]
- Add a get movie query function to the models file. [Jonathan Kamau]
- Remove print statements. [Jonathan Kamau]
- Remove print statements and add the function that adds movie search
  results to cache. [Jonathan Kamau]
- Add import for the addmovie resource in init.py. [Jonathan Kamau]
- Merge pull request #5 from jonathankamau/ft-movie-search-
  endpoint-160480604. [Jonathan Kamau]

  #160480604 Create movie search endpoint
- Feat(movie-search): create movie search endpoint. [Jonathan Kamau]

  [Delivers #160480604]
- Merge pull request #4 from jonathankamau/ft-login-endpoint-160480540.
  [Jonathan Kamau]

  #160480540 Login Endpoint
- Feat(user-login): make fix to models. [Jonathan Kamau]

  [Delivers #160480540]
- Feat(user-login): develop the login endpoint. [Jonathan Kamau]

  [Finishes #160480540]
- Merge pull request #3 from jonathankamau/ft-create-account-
  endpoint-160480531. [Jonathan Kamau]

  #160480531 Create account endpoint
- Feat(create-account): a user should be able to create an account.
  [Jonathan Kamau]

  [Delivers #160480531]
- Merge pull request #2 from jonathankamau/ch-implement-mongo-
  db-160480501. [Jonathan Kamau]

  #160480501 Implement mongodb in application
- Chore(database): make a few final fixes. [Jonathan Kamau]

  [Delivers #160480501]
- Chore(database): implement the mongodb database. [Jonathan Kamau]

  [Finishes ##160480501]
- Merge pull request #1 from jonathankamau/ch-set-up-project-
  structure-160480491. [Jonathan Kamau]

  #160480491 Setup project structure
- Chore(pr-template): edit the pr template. [Jonathan Kamau]
- Chore(readme): add information to readme. [Jonathan Kamau]
- Add template for pull requests. [Jonathan Kamau]
- Chore(initialize-app): set up the configurations necessary to run the
  app. [Jonathan Kamau]

  [Delivers #160480491]
- Chore(file-structure): add intial files to the project. [Jonathan
  Kamau]

  [Finishes #160480491 ]
- Initial commit. [Jonathan Kamau]