# MovieHub

## Overview
MovieHub is a Django-based web application developed for the **CM3035 Advanced Web Development** course. The application provides a comprehensive platform to explore movie data sourced from the IMDB 5000 movie dataset. It offers various functionalities such as browsing movies, directors, and actors, along with filtering options, CRUD operations, and detailed insights into movie statistics. The project was designed to showcase web development skills using Django and a relational database model.

## Dataset Information
The dataset used for this project is the [IMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset) by Yueming (2017), available on Kaggle. The dataset provides detailed information on movies, including release year, budget, gross revenue, directors, and actors. Although the dataset includes social media rankings of actors and directors, these elements were not utilized in this project.

### Key Features of the Dataset
- **Movies**: Contains information about each movie, such as title, release year, gross revenue, and IMDB score.
- **Directors**: Lists all directors and their respective movies, along with their IMDB scores.
- **Actors**: Lists all actors and their associated movies, along with director collaborations.
- **Genres**: Represents the genre classification of each movie.
- **Content Ratings**: Defines the content rating of each movie (e.g., PG-13, R).
- **Languages**: Specifies the language of each movie.
- **Countries**: Identifies the country of origin for each movie.

## Application Features
MovieHub offers the following key functionalities:

### Directors
- Lists all directors in the database.
- Displays the top-grossing directors.
- Shows directors who have collaborated with the most actors.
- Lists directors with the highest IMDB score.

### Actors
- Displays all actors and their associated movies.
- Allows users to filter actors based on director collaboration.
- Shows the number of movies in which each actor has appeared.

### Movies
- Lists all movies, including filtering options by genre, release year, language, and content rating.
- Displays the top 10 highest-grossing movies and the top 10 highest-rated movies by IMDB score.
- Allows users to create, update, and delete movie records (CRUD operations).

## Entity-Relationship Diagram (ERD)
The application uses an entity-relationship model to represent the relationships between movies, directors, actors, genres, languages, and countries. The following relationships are defined:

- **Movie - Director**: Each movie has one director, but a director can direct many movies.
- **Movie - Actor**: A movie can feature many actors, and each actor can appear in multiple movies (many-to-many relationship).
- **Movie - Genre**: A movie can belong to multiple genres, and each genre can contain multiple movies.
- **Movie - Language**: Each movie is in one language, but multiple movies can share the same language.
- **Movie - Country**: Each movie originates from one country, but many movies can be from the same country.
- **Movie - Content Rating**: Each movie has one content rating, but multiple movies can share the same rating.

## Setup and Installation
To set up and run the MovieHub application locally, follow these steps:

### Prerequisites
- Python 3.8 or higher
- Django 3.2 or higher
- SQLite3 (or any other supported database)

### Installation Steps
1. **Clone the Repository**:
   ```bash```
   git clone https://github.com/your-username/moviehub.git
   cd moviehub


2. **Install Dependencies**:
Create and activate a virtual environment, then install the required packages:
`python3 -m venv env`
`source env/bin/activate`  # On Windows use `env\Scripts\activate`
`pip install -r requirements.txt`

3. **Apply Migrations**
`python manage.py migrate`

4. **Create a Superuser:**
Create a superuser to access the Django admin interface
`python manage.py createsuperuser`

5. **Run the server:**
`python manage.py runserver`

Access the application at `http://127.0.0.1:8000/` in your web browser.

## Usage
The application provides the following key views and API endpoints:

### Frontend Views (urls.py)
- `/:` Homepage of the MovieHub application.
- `/movies/`: Lists all movies.
- `/movies/<int:pk>/`: Displays details of a specific movie.
- `/movies/new/`: Form to create a new movie.
- `/movies/<int:pk>/edit/`: Form to edit an existing movie.
- `/movies/<int:pk>/delete/`: Deletes a specific movie.
- `/directors/`: Lists all directors.
- `/actors/`: Lists all actors.
- `/top_directors/`: Displays the top directors by gross earnings.
- `/top_movies_by_imdb/`: Displays the top movies based on IMDB scores.

### API Endpoints (api_urls.py)
- `/api/movies/`: Lists all movies and allows the creation of new movies.
- `/api/movies/<int:pk>/`: Retrieve, update, or delete a specific movie.
- `/api/directors/`: Lists all directors.
- `/api/actors/`: Lists all actors.
- `/api/movies_by_genre/<str:genre>/`: Lists movies by a specific genre.
- `/api/directors/<int:director_id>/actors/`: Lists all actors who have worked with a given director.

## Unit Testing
Unit tests have been implemented using factory_boy and Django's built-in test framework.

### Running Tests
To run the tests, execute the following command in the root directory:

`python manage.py test`

The tests cover CRUD operations, API endpoints, and view logic to ensure the application is functioning as expected.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
Kerstin Kegel
This project was developed as part of the CM3035 Advanced Web Development course in the BSc Computer Science program.

- GitHub: car10ca
- Email: kerstinkegel@gmail.com
