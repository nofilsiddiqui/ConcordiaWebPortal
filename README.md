

# Concordia University Web Portal

## Project Overview

This project is a Django-based web application designed to manage FAQs, user registration, and events for Concordia University. The portal is intended to provide a seamless experience for users to interact with the university's resources, ask questions, and stay informed about upcoming events. The application is designed with a user-friendly interface and includes features for both users and administrators.

## Features

### 1. User Registration and Authentication
- **User Registration**: Users can create an account by providing their email, password, and additional information like faculty of interest and program of interest.
- **User Login**: Registered users can log in to access the portal's features.
- **User Profile**: Users can view and update their profile information.
- **Email Notifications**: Upon successful registration, users receive a thank-you email. Additionally, users are notified via email when they submit a new question.

### 2. FAQ Management System
- **FAQ List**: Users can browse through a list of frequently asked questions organized in an accordion-style layout.
- **Search Functionality**: Users can search for relevant questions using a search bar, which filters the FAQs based on the query.
- **Submit a Question**: Users can submit new questions through a simple form. Submitted questions are sent to the admin for review and approval.
- **Admin Approval**: Administrators can review, approve, and answer submitted questions via the Django admin interface.

### 3. Events Management
- **Upcoming Events**: The portal displays a list of upcoming events with details such as event title, date, and location. Only events added by the admin are visible to users.
- **Event Management**: Administrators can add, update, and delete events through the Django admin interface.

### 4. Chatbot Integration (Optional)
- **AI-Powered Chatbot**: A chatbot feature is integrated to provide instant answers to user queries. This feature utilizes the Hugging Face transformers library to handle conversational AI tasks.

### 5. Email Notifications
- **Email Integration**: The application is configured to send emails via SMTP using Gmail. Users receive notifications when they register and when they submit questions.

## Technical Details

- **Framework**: Django 4.2.14
- **Database**: SQLite (for development)
- **Frontend**: Bootstrap 5 with Django templates
- **Deployment**: Compatible with PythonAnywhere for easy hosting and deployment
- **Unit Testing**: Implemented using Django's built-in test framework, with tests covering models, views, and forms.
- **Design Patterns**: Observer design pattern for handling real-time updates and notifications.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/concordia-university-portal.git
   cd concordia-university-portal
   ```

2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   - Open your browser and go to `http://127.0.0.1:8000/`.

## Deployment on PythonAnywhere

1. **Upload your project files to PythonAnywhere**.
2. **Set up a virtual environment** and install the necessary packages.
3. **Configure your WSGI file** and static files.
4. **Set environment variables** and configure the Django settings for production.
5. **Run the application** and access it via your PythonAnywhere domain.

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or additional features.

## License

This project is licensed under the MIT License.

---

This README provides a comprehensive overview of your project, detailing its functionality, installation steps, and technical aspects.