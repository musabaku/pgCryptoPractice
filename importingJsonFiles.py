import psycopg2
import json

# Database connection
conn = psycopg2.connect("dbname=TDEpractice2 user=postgres password=aak101010 host=localhost port=5432")
cursor = conn.cursor()

# Function to read JSON file
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# JSON files list
json_files = [
    "C:\\Users\\musab\\Desktop\\tde\\json\\data1.json",
    "C:\\Users\\musab\\Desktop\\tde\\json\\data2.json",
    "C:\\Users\\musab\\Desktop\\tde\\json\\data3.json"
]

# Insert JSON data into the table
for file_path in json_files:
    json_data = read_json_file(file_path)
    json_text = json.dumps(json_data)  # Convert dict to JSON string
    cursor.execute("""
        INSERT INTO encrypted_json_data (data_json, enc_data_json)
        VALUES (%s, pgp_sym_encrypt(%s, 'S3cr3tK3y!2025'))
    """, (json_text, json_text))

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("JSON data inserted successfully.")
