# Club Management Project

This is a Django-based web application built as part of the Django Wednesdays tutorial series on YouTube, created by [John Elder](http://johnelder.com/).

<br>

## Overview

This project is a club management web application that allows users to explore and manage clubs, events, and venues. It was developed as part of the Django Wednesdays tutorial series on YouTube, created by John Elder.

The tutorial focuses on teaching core aspects of Django, along with front-end development using Bootstrap. This project covers several advanced features like authentication, file uploads, search functionality, and more.

![home page](https://raw.githubusercontent.com/abdrrahim2002/Club-Management-Project/refs/heads/main/images/home.png)

<br>

![search function](https://raw.githubusercontent.com/abdrrahim2002/Club-Management-Project/refs/heads/main/images/search.png)


<br>

![form](https://raw.githubusercontent.com/abdrrahim2002/Club-Management-Project/refs/heads/main/images/form.png)



<br>

![pagination](https://raw.githubusercontent.com/abdrrahim2002/Club-Management-Project/refs/heads/main/images/Pagination.png)

<br>

![admin dashboard](https://raw.githubusercontent.com/abdrrahim2002/Club-Management-Project/refs/heads/main/images/admin%20dashboard.png)

<br>

<br>

## What I Learned

During this project, I gained hands-on experience with the following:

- **Bootstrap Integration:** Learned how to use Bootstrap for responsive and user-friendly web design.
- **Django Fundamentals:** Explored the base and foundational aspects of the Django framework.
- **User Authentication:** Implemented Django’s authentication system to allow users to sign up, log in, and manage their accounts.
  - Non-logged-in users can view only public data (events and venues).
  - Logged-in users can create and manage their own venues and events.
  - Admin users have extra privileges to approve events and manage content.
- **Form Creation & File Uploads:** Built custom forms with image upload capabilities, enhancing user interaction.
- **Pagination:** Learned how to implement pagination for better user experience on pages with large amounts of data.
- **Search Functionality:** Utilized Django ORM to create a search system for venues and events.
- **Data Export Options:** Added features allowing users to download data in multiple formats, including text, CSV, and PDF.

<br>

## Features

- User registration and authentication system
- Conditional display of options based on user role (anonymous, logged-in, admin)
- Venue and event creation, editing, and approval system
- Search and filtering for venues and events
- Pagination for improved navigation
- File uploads for images
- Data export options in text, CSV, and PDF formats

<br>

## Installation

1. Clone this repository:

```
git cline https://github.com/abdrrahim2002/Club-Management-Project.git
```

2. Navigate to the project directory:

```
cd Club-Management-Project
```

3. Set up a virtual environment:

```
virtualenv venv
source venv/bin/activate
```

4. Install the required dependencies:

```
pip install -r requirements.txt
```

5. Apply migrations to set up the database:

```
cd myclub_website
python manage.py makemigrations
python manage.py migrate
```

6. Create super user:

```
python manage.py createsuperuser
```

7. Run the development server:

```
python manage.py runserver
```

8. At last visit `http://127.0.0.1:8000/` in your browser.

<br>

## Technologies Used
- Python: Programming language
- Django: Web framework
- SQLite: Database
- Bootstrap: Front-end framework
- HTML: Markup

<br>

## Acknowledgments
Special thanks to [John Elder](http://johnelder.com/) for the insightful Django Wednesdays tutorial series that guided the development of this project ❤️.
