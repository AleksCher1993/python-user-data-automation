from fileinput import filename
import requests as req
import json
import csv
import os
import logging

def write_csv_to_file(filename, data):
    logging.info(f'Writing data to CSV file: {filename}')
    try:
        with open(filename, 'w', newline='') as file:
            if not data:
                logging.warning(f'No data provided to write to CSV file: {filename}')
                return
            columns=data[0].keys()
            writer=csv.DictWriter(file, fieldnames=columns)
            writer.writeheader()
            writer.writerows(data)
            logging.info(f'Successfully wrote data to CSV file: {filename}')    
    except Exception as e:
            logging.error(f'Failed to write data to CSV file: {filename} with error: {e}')
def write_json_to_file(filename, data):
    logging.info(f'Writing data to JSON file: {filename}')
    try:
        with open(filename, 'w',encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
            logging.info(f'Successfully wrote data to JSON file: {filename}')
    except Exception as e:
            logging.error(f'Failed to write data to JSON file: {filename} with error: {e}')
def format_data_list(dataset):
    dataList=[]
    for data in dataset:
        dataList.append({
            "id": data["id"],
            "name": data["name"],
            "email": data["email"],
            "city": data["address"]["city"]
        })
    return dataList
def request_data(URL):
    logging.info(f'Requesting data from URL: {URL}')
    try:
        with req.Session() as session:
            response = session.get(URL, timeout=10)
            response.raise_for_status()
            logging.info(f'Successfully received data from URL: {URL}')
            return response.json()
    except req.RequestException as e:
        logging.error(f'Failed to retrieve data from URL: {URL} with error: {e}')
        return []
def read_json_from_file(filename):
    logging.info(f'Reading data from JSON file: {filename}')
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    logging.info(f'Successfully read data from JSON file: {filename}')
    return data


def main():
    logging.basicConfig(level=logging.INFO,filename='logs/app.log',filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Application started')
    URL='https://jsonplaceholder.typicode.com/users'
    if os.path.exists("data/users.json"):
        dataset = read_json_from_file('data/users.json')
    else:
        dataset = request_data(URL)
        write_json_to_file('data/users.json', dataset)
    processedData = format_data_list(dataset)
    write_json_to_file('data/processed_users.json', processedData)
    write_csv_to_file('data/report.csv', processedData)
    logging.info('Application finished successfully')
    
if __name__ == "__main__":
    main()
    
