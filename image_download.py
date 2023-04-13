import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

def image_downloads():
    # Initialize Firebase app and storage client

    cred = credentials.Certificate('attendance-34c91-firebase-adminsdk-n1vj8-18f67ea82c.json')
    app = firebase_admin.initialize_app(cred, {'storageBucket': 'attendance-34c91.appspot.com'})
    client = storage.bucket(app=app)

    # List all the files in the bucket
    all_files = client.list_blobs()

    # Download each file in the bucket
    for file in all_files:
        file_name = file.name
        file_path = f"faces/{file_name}"
        file.download_to_filename(file_path)
        print(f"Downloaded {file_name} to {file_path}")

    # Delete the Firebase app
    firebase_admin.delete_app(app)