# django_rest
Python Django CRUD API with MySQL and Django Rest Framework

## Features

- Create, retrieve, update, and delete blog posts.
- Add comments to blog posts and retrieve comments for a specific blog post.
- Like and dislike functionality for blog posts.
- User authentication to protect sensitive operations.
- File upload support for adding images to blog posts.

## Installation

1. Make sure you have Python and Django installed on your machine.
2. Clone the repository:
```
git clone <URL>
```
3. Navigate to the project directory:
```
cd django_rest
```
4. Install the required dependencies:
```
pip install django
pip install djangorestframework
pip install django-cors-headers
pip install pymysql
```
5. Create a MySQL Database and configure in the settings.py file:
```
        'NAME': '<database name>',
        'USER':'<database user>',
        'PASSWORD':'<database password>',
        'HOST':'<database host>',
        'PORT':'<database port>'
       
```
6. Apply the database migrations:
```
python manage.py makemigrations BlogPost
python manage.py migrate BlogPost
```
7. Start the development server:
```
python manage.py runserver
```


8. Access the application by visiting `http://localhost:8000/api/` in your web browser.

## API Endpoints

- `GET /api/blog/`: Get all blog posts.
- `POST /api/addblog/`: Create a new blog post.
- `GET /api/blog/<slug:slug>/`: Get details of a specific blog post.
- `PUT /api/blog/<slug:slug>/`: Update a specific blog post.
- `DELETE /api/blog/<slug:slug>/`: Delete a specific blog post.
- `POST /api/blog/<int:id>/like/`: Like or dislike a blog post.
- `POST /api/blogs/<slug:slug>/comments/`: Add a comment to a blog post.
- `GET /api/blogs/<slug:slug>/comment/`: Get comments for a specific blog post.
- `POST /api/savefile/`: Upload a file (image) for a blog post.
- `GET /api/getuser/`: Get details of the authenticated user.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or bug fix.

3. Make your changes and commit them.

4. Push your changes to your forked repository.

5. Submit a pull request describing your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

## Authors

- [Mulikevs](https://github.com/mulikevs)

Feel free to add your name and contact information if you'd like.


