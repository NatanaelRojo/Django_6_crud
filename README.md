# Django 6 CRUD Example + Bootstrap 5

The following is an example of CRUD (Create, Read, Update, Delete) in Django 6.

There are 2 CRUD applications, one uses function-based views (FBV) and the other
uses class-based views (CBV).

## Requirements:
```
Django==6.0.2
Python>=3.12
```

## Run the following commands in sequence to deploy the project to a development environment:

```bash
Creating a Python 3 virtual environment:

1. Update the package list:

$ sudo apt update

2. Install python3-venv

$ sudo apt install python3-venv

3. Create the virtual environment:

$ python3 -m venv my_environment

4. Activate the environment:

$ source my_environment/bin/activate
```

Now install de Requirements

```bash
$ pip install -r requirements.txt

$ cp Django_6_crud/settings.py_example Django_6_crud/settings.py

$ python manage.py makemigrations person product

$ python manage.py migrate

$ python manage.py runserver
```

## Test the project:

Open your browser to http://127.0.0.1:8000 and you'll see the Django 6 CRUD
application for managing people records.

## Image

![1.png](1.png "1.png")

![2.png](2.png "2.png")

![3.png](3.png "3.png")

![4.png](4.png "4.png")

## Project features

- Custom user model
	- The project provides a `User` model that extends Django's
		`AbstractUser` and includes an optional `role` field for application
		roles (e.g. "admin", "manager"). Use `get_user_model()` where
		possible and set `AUTH_USER_MODEL = "users.User"` before running
		initial migrations.

- User management forms
	- `CustomUserCreationForm` and `CustomUserChangeForm` wrap Django's
		built-in forms and expose `username`, `email`, `first_name`,
		`last_name`, and `role`. They preserve password validation and
		hashing while integrating the extra field into create/update flows.

- Class-based user CRUD
	- The `users` app implements CRUD using Django generic class-based
		views: `UserListView`, `UserDetailView`, `UserCreateView`,
		`UserUpdateView`, and `UserDeleteView`. They use `get_user_model()`
		and `reverse_lazy` for reliable behavior with the custom user model.

- Organized templates
	- Templates are located under `apps/users/templates/users/` and
		follow the conventional names expected by the views (e.g.
		`user_list.html`, `user_form.html`, `user_detail.html`,
		`user_confirm_delete.html`).

- Admin-ready
	- The custom `User` can be registered in the admin site for
		administrative management; adding a simple admin registration will
		expose user CRUD in Django's admin interface.

- Developer-friendly docs and code clarity
	- Module- and class-level docstrings were added to `models.py`,
		`forms.py`, and `views.py` to make the codebase easier to inspect
		and maintain.

## Quick setup & common commands

```bash
# create a virtual environment and install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# copy example settings if needed
cp Django_6_crud/settings.py_example Django_6_crud/settings.py

# (first-time only) ensure AUTH_USER_MODEL is configured, then:
python manage.py makemigrations
python manage.py migrate

# create admin user and run the dev server
python manage.py createsuperuser
python manage.py runserver
```


