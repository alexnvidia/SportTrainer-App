# **SportTrainer App**

SportTrainer is a cross-platform application designed for sports coaches, allowing them to efficiently manage personalized training sessions for their clients. The app offers features such as attendance validation, effort ratings, session notes, and an internal messaging system between coaches and clients. Additionally, it can be accessed from Android, iOS, and web platforms.

## **Table of Contents**
1. [Features](#features)
2. [Technologies Used](#technologies-used)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)

## **Features**

- **Client Management**: A coach can view a list of clients and see details for each one.
- **Session Validation**: The coach can mark whether a client attended or canceled a session using swipe actions.
- **Session Notes**: The coach can add notes at the end of each session.
- **Effort Scale**: Clients can rate the session using the Borg Scale (1-10).
- **Session History**: Clients and coaches can consult training history, with an option to export it to PDF or CSV.
- **Internal Messaging**: Direct communication between clients and coaches through a messaging system, with push notifications.

## **Technologies Used**

- **Backend**: Django (REST API), Node.js (Microservices)
- **Frontend**: Flutter (Compatible with Android, iOS, and web)
- **Database**: PostgreSQL
- **Authentication**: JWT (JSON Web Tokens)
- **Push Notifications**: Firebase Cloud Messaging (FCM) - HTTP v1
- **Version Control**: GIT
- **Deployment**: Docker, Heroku

## **Prerequisites**

Before you begin, ensure you have the following components installed:

- **Python** (version 3.8 or higher)
- **Node.js** (version 14 or higher)
- **Flutter** (version 3 or higher)
- **PostgreSQL**
- **Docker** (optional, for deployment)
- **Git**

## **Installation**

Follow these steps to run the project on your local machine:

### **1. Clone the repository**

```bash
git clone https://github.com/username/sporttrainer-app.git
cd sporttrainer-app
