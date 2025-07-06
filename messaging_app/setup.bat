@echo off
echo Setting up Django Messaging App...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python 3.11+ first.
    pause
    exit /b 1
)

REM Check if pip is installed
pip --version >nul 2>&1
if errorlevel 1 (
    echo pip is not installed. Please install pip first.
    pause
    exit /b 1
)

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    copy env.example .env
    echo Please edit .env file with your database credentials.
)

REM Run migrations
echo Running database migrations...
python manage.py migrate

REM Create superuser
echo Creating superuser...
python manage.py createsuperuser

echo Setup complete!
echo To start the development server, run:
echo venv\Scripts\activate.bat
echo python manage.py runserver
echo.
echo Or use Docker Compose:
echo docker-compose up --build
pause 