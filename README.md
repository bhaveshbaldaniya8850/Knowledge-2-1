# Book Barter System

The Book Barter System is a web application built using Django. It allows users to register, log in, and post books they would like to barter or share. Users can search for books uploaded by others and contact the platform administrators for queries.

## Features

- **User Authentication:** 
  - Users can sign up for a new account.
  - Registered users can log in and log out securely.
- **Book Listings (Posts):**
  - Authenticated users can create new book posts by providing details such as Book Title, Author, Cover Image, Description (Info), and Contact Phone Number.
  - All posts are displayed on the home page and a dedicated "posted" page.
- **Search Functionality:**
  - Users can search for specific books by their title.
- **Contact System:**
  - A dedicated "Contact Us" page allows users to send inquiries or feedback to the site administrators.
- **Chat/Profile:**
  - The framework includes stubs and templates for user profiles and chat functionalities.

## Project Structure

The project uses Django 3.2.5 and is structured around two main apps, though functionality is primarily driven by the `home` app.

### 1. `home` App
This app manages routing, user authentication, and serving most pages.
**Models (`home/models.py`):**
- `about`: Stores contact form submissions (Name, Phone, Email, Content).
- `signup`: A legacy/custom model for registration details (though standard Django `User` model is used for actual authentication).

**Views (`home/views.py`):**
- Handles rendering of templates (`index.html`, `contactus.html`, `newpost.html`, etc.).
- `handlelogin`, `handlesignup`, `handlelogout`: Manage the authentication flow.
- `new_post`: Validates and saves new book listings to the database.
- `search`: Filters the books by title.

### 2. `postbook` App
This app primarily defines the core data model.
**Models (`postbook/models.py`):**
- `post`: The primary model for storing book details. It maps to a database table named `gallery` and includes fields like `user_name`, `title`, `phone`, `cover` (image), `author`, `info`, and `timestamp`.

## Running the Project Locally

Follow these steps to run the Book Barter System on your local machine:

### Prerequisites
- Python 3.x installed on your system.
- Django installed (`pip install django==3.2.5` recommended based on the project settings).
- Pillow installed for handling `ImageField` in models (`pip install pillow`).

### Steps to Run

1. **Navigate to the project directory:**
   Open your command prompt or terminal and navigate to the directory containing `manage.py`:
   ```bash
   cd path/to/project
   ```

2. **Make Database Migrations (Optional but recommended):**
   If you have made any changes to the models or if it's the first time setting up:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Create a Superuser (Admin account):**
   To access the Django admin panel, create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set a username, email, and password.

4. **Run the Development Server:**
   Start the local Django server:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**
   Open your web browser and go to:
   - Application: `http://127.0.0.1:8000/`
   - Admin Panel: `http://127.0.0.1:8000/admin/`

## Note on Media/Static Files
The project requires a proper configuration for serving media files (like book covers uploaded by users) during development. The images are currently uploaded to `static/sagar/` as per the `post` model configuration.
