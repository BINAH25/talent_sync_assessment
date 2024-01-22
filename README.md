# talent_sync_assessment
The Django Blogging Platform API is a powerful and flexible RESTful API built on the Django framework and Django Rest Framework (DRF). The primary goal of this project is to provide a robust backend solution for a modern blogging platform. The API supports essential functionalities such as user registration, authentication, and authorization, allowing users to create, read, update, and delete blog posts seamlessly

## Key Features
### User Authentication and Authorization
1. **User Registration**: New users can effortlessly register by providing necessary details (username and password).
2. **User Login**: Existing users can securely log in to the platform.
3. **JWT Authentication**: The API implements JSON Web Token (JWT) authentication to ensure secure user sessions.
3. **Permissions**: only users who have authorize permissions can create read update and delete a post.

### Blog Post Management
1. **Create Posts**: Authenticated and authorized users can craft engaging blog posts by providing a title,content and author.
2. **Read Posts**:  Authenticated and authorized users can retrieve blog posts.
3. **Update Posts**: Authenticated and authorized users have the ability to edit the content and title of their own blog posts.
4. **Delete Posts**: Authenticated and authorized users users can delete their own blog posts.
### Structured Data Model
The project includes a well-defined data model that represents blog posts.
Each post comprises a title, content, author, and a timestamp for tracking post creation.
### RESTful Endpoints
The API adheres to RESTful principles with clear and concise endpoints for user authentication and blog post management.
## Language and Libraries
Python 3.9
Django 5.0.1
## Usage Guidelines

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/BINAH25/talent_sync_assessment.git
   cd talent_sync_assessment
   
2. **Create Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the requires packages:**
   ```bash
   cd assessment
   pip install -r requirements.txt
   python manage.py makemigrations
   python manage.py migrate
4. **User registration endpoint:**
   ```bash
   http://127.0.0.1:8000/api/sign_up/
5. **User login endpoint:**
   ```bash
   http://127.0.0.1:8000/api/login/

6. **Create post  and get all posts endpoint:**
   ```bash
   http://127.0.0.1:8000/api/post/
7. **get a post endpoint:**
   ```bash
   http://127.0.0.1:8000/api/post/post_id/
   (e.g http://127.0.0.1:8000/api/post/1/)
8. **update a post endpoint:**
   ```bash
   http://127.0.0.1:8000/api/post/post_id/
   (e.g http://127.0.0.1:8000/api/post/1/)
9. **delete a post endpoint:**
   ```bash
   http://127.0.0.1:8000/api/post/post_id/
   (e.g http://127.0.0.1:8000/api/post/1/)
9. **assign and revoke a user permission endpoint:**
   ```bash
   http://127.0.0.1:8000/api/post/assign-permissions/
   http://127.0.0.1:8000/api/post/revoke-permissions/
### Fields for user registration
<img width="512" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/7ca364ea-4c11-4fa5-b4e4-4d0ebd723209">
### Fields for user login
<img width="1039" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/1a00d02a-e2ec-4b56-aac8-e2f3287c608c">
### Fields for creating a post
<img width="514" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/b9916860-9f07-446e-b65d-42bb321c36f3">
### getting all posts
<img width="1019" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/0b4b9acf-79cd-4bc4-ac0a-9b72d6169735">
### retrieve  a post
<img width="976" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/47603df2-66e5-45a5-bbe5-53979bdfc8dd">
### delete a post
<img width="940" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/daa637fe-5b7c-40e7-9b03-45e8324bcb09">
### give permission to a user
<img width="994" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/3d741dc7-7d5e-40c5-bd96-824f9118e4d9">
### revoke user permission 
<img width="1029" alt="image" src="https://github.com/BINAH25/talent_sync_assessment/assets/81252456/f4bf0a30-4a9a-4855-9009-ec5955dc8312">








