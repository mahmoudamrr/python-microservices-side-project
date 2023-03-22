<!-- ABOUT THE PROJECT -->
## About The Project

we have two folders admin and main the admin app Built with django that will let us create update delete products.
and main app Built with flask to let us browse products and like them.
the two app communicate through rabbitmq.



### Built With

* [Django](https://www.djangoproject.com/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [MySQL](https://www.mysql.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Docker](https://www.docker.com/)
* [RabbitMQ](https://www.rabbitmq.com/)



<!-- GETTING STARTED -->
## Getting Started

1. Clone the repo
   ```sh
   git clone https://github.com/mahmoudamrr/python-microservice-side-project.git
   ```

2. for each file of the project --admin & main
  ```sh
  docker-compose up
  ```
  
  3. admin app migration inside docker container
  ```sh
  docker-compose exec backend sh
  ```
  ```sh
  python manage.py makemigration
  ```
  ```sh
  python manage.py migrate
  ```

  
  4. main app migration inside docker container
  ```sh
  docker-compose exec backend sh
  ```
  ```sh
  python manage.py db init
  ```
  ```sh
  python manage.py db migrate
  ```
  ```sh
  python manage.py db upgrade
  ```
