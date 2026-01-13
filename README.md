# User Data Automation and Reporting
This project is a Python automation script that collects user data from an external API,
processes and normalizes the data, and generates JSON and CSV reports.
The script includes logging, error handling, and local data caching.

## Features

- Fetches user data from a public REST API
- Caches raw API responses locally in JSON format
- Processes and normalizes nested JSON data
- Generates structured JSON and CSV reports
- Logs all operations and errors to a log file
- Handles network and file I/O errors

## Project Structure
data/
├── users.json
├── processed_users.json
├── report.csv
logs/
├── app.log
main.py
requirements.txt

## Technologies Used

- Python 3
- requests
- csv
- json
- logging

## How It Works

1. The script checks if cached user data exists locally.
2. If not found, it fetches data from the external API.
3. Raw data is saved to a JSON file.
4. User data is processed and normalized into a simplified structure.
5. Processed data is saved as a JSON file.
6. A CSV report is generated for further analysis.
7. All steps are logged to a log file.

## How to Run

1. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
2. Install dependencies:
pip install -r requirements.txt
3. Run the script:
python main.py

## Example Output
- data/processed_users.json – normalized user data
[
  {
    "id": 1,
    "name": "Leanne Graham",
    "email": "Sincere@april.biz",
    "city": "Gwenborough"
  },
  {
    "id": 2,
    "name": "Ervin Howell",
    "email": "Shanna@melissa.tv",
    "city": "Wisokyburgh"
  }
]
- data/report.csv – CSV report with user information
id,name,email,city
1,Leanne Graham,Sincere@april.biz,Gwenborough
2,Ervin Howell,Shanna@melissa.tv,Wisokyburgh
3,Clementine Bauch,Nathan@yesenia.net,McKenziehaven
- logs/app.log – application logs
2026-01-13 16:40:54,326 - INFO - Application started
2026-01-13 16:40:54,326 - INFO - Requesting data from URL: https://jsonplaceholder.typicode.com/users
2026-01-13 16:40:54,642 - INFO - Successfully received data from URL: https://jsonplaceholder.typicode.com/users
2026-01-13 16:40:54,643 - INFO - Writing data to JSON file: data/users.json
2026-01-13 16:40:54,643 - INFO - Successfully wrote data to JSON file: data/users.json
2026-01-13 16:40:54,643 - INFO - Writing data to JSON file: data/processed_users.json
2026-01-13 16:40:54,644 - INFO - Successfully wrote data to JSON file: data/processed_users.json
2026-01-13 16:40:54,644 - INFO - Writing data to CSV file: data/report.csv
2026-01-13 16:40:54,644 - INFO - Successfully wrote data to CSV file: data/report.csv
2026-01-13 16:40:54,644 - INFO - Application finished successfully

## Author

Developed by [AleksBlack]

