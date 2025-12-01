# Envrionment Setup
- create virtual environment: python3 -m venv venv 
- run virtual environment: source venv/bin/activate
- install requirements: pip install -r requirements.txt

# Database Setup
- get DB environment variables (host, username, port, etc.) from repository owner
- run CREATE USER <DB_USER secret> WITH PASSWORD '<DB_USER secret>';
- run CREATE DATABASE <DB_NAME secret> OWNER <DB_USER secret>;
- navigate to /quickChat/backend/
- run "python3 initialize_db.py"