# Flask Blog App

The Flask Blog App is a simple and user-friendly blogging platform developed using Flask, a popular Python web framework, and MongoDB, a flexible NoSQL database. This application allows users to create, view, and manage blog entries with ease.

## Description

The Flask Blog App provides a straightforward blogging experience with the following features:

-**Create Blog Entries:** Easily add new blog posts through a web form. Entries can include titles and content, which are stored in a MongoDB database for persistence.

-**View Blog Entries:** Browse and read existing blog posts on the homepage. Each entry is displayed with its title and content, allowing for an engaging reading experience.

-**Manage Content:** Blog entries are saved in a structured manner within the MongoDB database, enabling efficient data retrieval and management.


## Features
**User-Friendly Interface:** Intuitive design for creating and viewing blog entries.
**Persistent Storage:** Blog entries are saved in MongoDB, ensuring data is preserved across sessions.
**Scalable:** Designed to handle increasing numbers of blog entries efficiently.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- Flask
- Flask-PyMongo
- MongoDB

## Installation
1.**Clone the Repository**    ```bash
    git clone https://github.com/your-username/flask-blog-app.git
    cd flask-blog-app
    ```
    
2.**Create a Virtual Environment**    ```bash
    python -m venv venv
    ```
    
3.**Activate the Virtual Environment**    
    - On Windows:
        bash venv\Scripts\activate
    - On macOS/Linux:
        bash source venv/bin/activate
        
4.**Install Dependencies**    ```bash
    pip install -r requirements.txt
    ```
    
5.**Set Up MongoDB**    Ensure MongoDB is running locally or configure the connection string in `app.py`. You can use the default settings or modify them as needed.

6.**Run the Application**    ```bash
    python app.py
    ```
    By default, the app will be available at `http://127.0.0.1:5000`.

    
## Configuration

Customize the MongoDB connection settings in `app.py`. Update the connection URI if you're using a different host or port.

# Usage
Create a Blog Entry
1. Navigate to the homepage and click on "Add New Entry."
2. Fill in the form with your blog content and submit.
3. View Blog Entries
Entries will be listed on the homepage. Click on any entry to view its details.

**CAN BE VIEWED AT https://blogwebsite-xc5f.onrender.com WHEN ACTIVE**
