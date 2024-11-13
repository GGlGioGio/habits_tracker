# Habit Tracker
This is a simple habit tracking application built using Flask. 
Users can track their daily habits and see progress over time.


## Technologies
- Python 3.11
- Flask
- Docker (for containerization)
- PostgreSQL (for database)
- Pytest (for testing)


## Installation
1. Clone the repository:
   git clone https://github.com/GGlGioGio/habits_tracker.git

2. Navigate to the project folder
   cd habits_tracker

3. Create and active a virtual environment
   For Windows:
   .\venv\Scripts\activate

   For MacOS/Linux
   source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Set up environment variables (if necessary). For Flask you can specify environment variables.
   For Windows:
   set FLASK_APP=app.py
   set FLASK_ENV=development

   For MacOS/Linux
   export FLASK_APP=app.py
   export FLASK_ENV=development

6. Start app:
   flask run
   App will be in this link: http://127.0.0.1:5000
   

## Running tests
To run tests, use:
pytest

To instal pytest, use:
pip install pytest


## Logs
Logs can be found in the logs/ directory (if configured). You can also check Flask logs in the console where the app is running.


## Continuous Integration (CI)
We use GitHub Actions to automatically run tests when pushing code.

You can view the status of the builds in the Actions tab.


## License
This project is licensed under the MIT License.