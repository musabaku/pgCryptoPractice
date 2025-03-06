import psycopg2

# Database connection parameters
conn = psycopg2.connect("dbname=TDEpractice2 user=postgres password=aak101010 host=localhost port=5432")
cursor = conn.cursor()

cursor = conn.cursor()

# Function to read binary file
def read_audio_file(file_path):
    with open(file_path, 'rb') as f:
        return f.read()

# Example audio file paths
audio_files = [
    ("audio1.mp3", "C:\\Users\\musab\\Desktop\\tde\\audio\\audio1.mp3"),
    ("audio2.mp3", "C:\\Users\\musab\\Desktop\\tde\\audio\\audio2.mp3"),
    ("audio3.mp3", "C:\\Users\\musab\\Desktop\\tde\\audio\\audio3.mp3")
]

# Insert audio data into the table
for filename, filepath in audio_files:
    audio_data = read_audio_file(filepath)
    cursor.execute("""
        INSERT INTO encrypted_audio_files (filename, audio_data, enc_audio_data)
        VALUES (%s, %s, pgp_sym_encrypt_bytea(%s, 'S3cr3tK3y!2025'))
    """, (filename, audio_data, audio_data))

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Audio files inserted successfully.")
