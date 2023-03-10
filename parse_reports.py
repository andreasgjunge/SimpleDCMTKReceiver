import csv
import os



def read_reports(file_name):
    # Open the CSV file and read in the contents
    reports_path = 'reports/'
    full_path = reports_path + file_name

    if not os.path.exists(full_path):
        return {'status': 'failure', 'reason': f"The file {full_path} does not exist."}

    with open(full_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        
        # Initialize an empty list to store the data
        data = []
        
        # Iterate over the rows in the CSV file
        for row in csv_reader:
            # Sometimes, a case can contain multiple studies separated by a comma additionally
            substrings = row['procedurestudyinstanceuid'].split(',')
            for substring in substrings:    
                data.append({
                'procedurestudyinstanceuid': substring
                })

    # The data is now stored in the "data" list
    return {'status': 'success', 'data': data}