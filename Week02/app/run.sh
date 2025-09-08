# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py

# How to see the expected output: 
# Visit 👉 http://localhost:5000
# → you should see:
# {"message": "Hello, KSW Capstone!"}

# Run Tests
#pytest -v

# test_app.py::test_home PASSED

# This gives the students a working baseline Flask API + unit test right in Week 2.
# It will integrate smoothly with the Jenkinsfile and Dockerfile we defined earlier.
