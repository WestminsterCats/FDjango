# Westminster University Lending System

Welcome to the Westminster University Lending System! This Django project aims to provide a comprehensive lending system tailored for the needs of Westminster University. With this system, users can borrow various items, manage their loans, and administrators can efficiently track lending activities.

## Features

- **User Authentication**: Users can create accounts, log in, and manage their profiles.
- **Item Management**: Administrators can add, edit, and remove items available for lending.
- **Loan Management**: Users can request loans, view their loan history, and return items.
- **Admin Dashboard**: Administrators have access to a dashboard to oversee lending activities, manage users, and generate reports.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/your_username/FDijango.git
    ```

2. Navigate to the project directory:
    ```
    cd FDjango
    ```

3. Create a virtual environment:
    ```
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```
        source venv/bin/activate
        ```

5. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

6. Set up the database:
    ```
    python manage.py migrate
    ```

7. Create a superuser (admin account):
    ```
    python manage.py createsuperuser
    ```

8. Start the development server:
    ```
    python manage.py runserver
    ```

9. Access the application at `http://127.0.0.1:8000/` in your web browser.

## Usage

- **User Accounts**: Users can sign up for new accounts or log in with existing credentials.
- **Browsing Items**: Users can view available items for lending.
- **Requesting Loans**: Users can request loans for desired items, specifying loan duration.
- **Managing Loans**: Users can view their current loans, renew loan periods, or return items.
- **Administrative Tasks**: Admins can log in to the admin dashboard (`http://127.0.0.1:8000/admin`) to manage items, users, loans, and generate reports.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## Acknowledgements

- This project was developed as a part of the Westminster University community.
- Special thanks to the Django community for their excellent framework.

---
*Note: Replace `your_username` in the installation instructions with your GitHub username if you've forked the repository.*
