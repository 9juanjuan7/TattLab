from website import create_app
import atexit
import os
import glob

app = create_app()
# Function to delete all files in uploads folder when Flask stops
def cleanup_uploads():
    files = glob.glob(os.path.join("website/uploads", "*"))  # Get all files in uploads/
    for file in files:
        try:
            os.remove(file)  # Delete each file
        except Exception as e:
            print(f"Error deleting {file}: {e}")
  
atexit.register(cleanup_uploads)

if __name__ == "__main__":
    app.run(debug=True)
