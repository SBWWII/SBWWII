import csv  # No indentation (0 spaces)

csv_file = "F:/GitHub/SBWWII/signup.csv"  # No indentation (0 spaces)

# Open the CSV file safely
with open(csv_file, mode="r", encoding="utf-8") as file:  # No indentation (0 spaces)
    reader = csv.reader(file)  # Indented exactly 4 spaces inside 'with open'

    for row in reader:  # Indented exactly 4 spaces inside 'reader'
        print(row)  # Indented exactly 4 spaces inside 'for row in reader'
from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

# ✅ New route to read CSV contents
@app.route('/read_csv', methods=['GET'])
def read_csv():
    csv_file = "F:/GitHub/SBWWII/signup.csv"
    with open(csv_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        data = [row for row in reader]  # Store rows in a list
    return jsonify({"data": data})  # Return CSV content

# ✅ Route to handle form submission
@app.route('/submit', methods=['POST'])
def save_to_csv():
    data = request.json
    
    with open("F:/GitHub/SBWWII/signup.csv", 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([data["name"], data["email"], data["phone"]])
    
    return jsonify({"message": "Data saved successfully"})

if __name__ == '__main__':
    print("🚀 Flask server is starting...")
    app.run(port=8000, debug=True)