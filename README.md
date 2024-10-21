SportTrainer App
SportTrainer is a cross-platform application designed for sports coaches, allowing them to efficiently manage personalized training sessions for their clients. The app offers features such as attendance validation, effort ratings, session notes, and an internal messaging system between coaches and clients. Additionally, it can be accessed from Android, iOS, and web platforms.

Table of Contents
Features
Technologies Used
Prerequisites
Installation
Project Structure
Usage
Contributing
License
Features
Client Management: A coach can view a list of clients and see details for each one.
Session Validation: The coach can mark whether a client attended or canceled a session using swipe actions.
Session Notes: The coach can add notes at the end of each session.
Effort Scale: Clients can rate the session using the Borg Scale (1-10).
Session History: Clients and coaches can consult training history, with an option to export it to PDF or CSV.
Internal Messaging: Direct communication between clients and coaches through a messaging system, with push notifications.
Technologies Used
Backend: Django (REST API), Node.js (Microservices)
Frontend: Flutter (Compatible with Android, iOS, and web)
Database: PostgreSQL
Authentication: JWT (JSON Web Tokens)
Push Notifications: Firebase Cloud Messaging (FCM) - HTTP v1
Version Control: GIT
Deployment: Docker, Heroku
Prerequisites
Before you begin, ensure you have the following components installed:

Python (version 3.8 or higher)
Node.js (version 14 or higher)
Flutter (version 3 or higher)
PostgreSQL
Docker (optional, for deployment)
Git
Installation
Follow these steps to run the project on your local machine:

1. Clone the repository
bash
Copiar código
git clone https://github.com/username/sporttrainer-app.git
cd sporttrainer-app
2. Backend - Django
Navigate to the backend/django directory:

bash
Copiar código
cd backend/django
Create a virtual environment and install the dependencies:

bash
Copiar código
python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
pip install -r requirements.txt
Configure the PostgreSQL database in the settings.py file.

Apply the migrations:

bash
Copiar código
python manage.py migrate
Start the development server:

bash
Copiar código
python manage.py runserver
3. Microservices - Node.js
Navigate to the backend/nodejs directory:

bash
Copiar código
cd ../nodejs
Install the Node.js dependencies:

bash
Copiar código
npm install
Start the microservices:

bash
Copiar código
npm start
4. Frontend - Flutter
Navigate to the frontend directory:

bash
Copiar código
cd ../../frontend
Ensure Flutter is installed and configured. Then install the dependencies:

bash
Copiar código
flutter pub get
Start the application:

bash
Copiar código
flutter run
Project Structure
bash
Copiar código
/sporttrainer-app/
│
├── /backend/            # Backend with Django and Node.js
│   ├── /django/         # RESTful API in Django
│   └── /nodejs/         # Microservices in Node.js
│
├── /frontend/           # Frontend with Flutter
│   ├── /android/
│   ├── /ios/
│   └── /web/
│
├── /docs/               # Technical documentation
└── README.md            # Project description
Usage
Coach: Can validate sessions, view their list of clients, add notes, and export session history.
Client: Can view their coach's profile, rate sessions, and consult their training history.
Messaging: Quick communication with integrated push notifications.
Contributing
Contributions are welcome! If you have any suggestions, feel free to create an issue or submit a pull request.

Steps to Contribute:
Fork the project.
Create a new branch: git checkout -b feature/new-feature.
Make your changes and commits: git commit -m "Added new feature".
Push your branch: git push origin feature/new-feature.
Submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more information.
