# Django Messaging App

A Django REST API for a messaging application with user authentication and message management.

## Features

- User authentication and management
- Message creation and retrieval
- Message read status tracking
- RESTful API endpoints
- Comprehensive test coverage
- Docker support
- CI/CD with Jenkins and GitHub Actions

## API Endpoints

- `GET /api/users/` - List all users
- `GET /api/users/{id}/` - Get specific user details
- `GET /api/messages/` - List messages for authenticated user
- `POST /api/messages/` - Create a new message
- `GET /api/messages/{id}/` - Get specific message details
- `PUT /api/messages/{id}/` - Update a message
- `DELETE /api/messages/{id}/` - Delete a message
- `POST /api/messages/{id}/mark_as_read/` - Mark message as read

## Setup Instructions

### Prerequisites

- Python 3.11+
- MySQL 8.0+
- Docker (optional)

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd messaging_app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp env.example .env
# Edit .env with your database credentials
```

5. Run database migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

### Docker Setup

1. Build the Docker image:
```bash
docker build -t messaging-app .
```

2. Run the container:
```bash
docker run -p 8000:8000 messaging-app
```

## Testing

### Run Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest messaging/tests.py
```

### Code Quality
```bash
# Run flake8 linting
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```

## CI/CD Setup

### Jenkins Pipeline

1. Install Jenkins in Docker:
```bash
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

2. Access Jenkins at `http://localhost:8080`

3. Install required plugins:
   - Git plugin
   - Pipeline plugin
   - ShiningPanda plugin
   - Cobertura plugin
   - JUnit plugin

4. Configure credentials:
   - Add GitHub credentials
   - Add Docker Hub credentials

5. Create a new pipeline job pointing to your repository

### GitHub Actions

The repository includes two workflows:

1. **CI Pipeline** (`.github/workflows/ci.yml`):
   - Runs on push to main/develop and pull requests
   - Sets up MySQL service
   - Runs tests with pytest
   - Performs code quality checks with flake8
   - Generates coverage reports
   - Uploads artifacts

2. **Deployment Pipeline** (`.github/workflows/dep.yml`):
   - Runs on push to main and tags
   - Builds Docker image
   - Pushes to Docker Hub
   - Creates GitHub releases for tags

### Required Secrets

Set up the following secrets in your GitHub repository:

- `DOCKER_USERNAME`: Your Docker Hub username
- `DOCKER_PASSWORD`: Your Docker Hub password/token

## Project Structure

```
messaging_app/
├── messaging_project/     # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── messaging/            # Main app
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── pytest.ini
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

## License

This project is licensed under the MIT License. 