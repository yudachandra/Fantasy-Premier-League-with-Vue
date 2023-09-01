from flask import Flask, render_template
import csv

app = Flask(__name__)

# Load your CSV data into a list of dictionaries
def load_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data


# Define the route to display the HTML table
@app.route('/')
def display_table():
    data = load_csv('data/2023-24/gws/merged_gw.csv')  # Replace 'your_data.csv' with your CSV file path
    return render_template('FPL.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
