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
## Usage Guidelines

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/django-blogging-api.git
   cd django-blogging-api
