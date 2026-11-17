# Python Student Management UI

A beginner-friendly student management web UI built with Python and Streamlit.

## Features
- Add a student name, age, and course
- View student records
- Delete student records

> Note: This starter project stores records in Streamlit session state. Records are temporary and are cleared when the session resets. It does not use a database.

## Run locally

1. Install Python 3.12 or a compatible Python version.
2. Open a terminal in this project folder.
3. Create and activate a virtual environment (optional but recommended).
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the app:

   ```bash
   streamlit run app.py
   ```

6. Open http://localhost:8501 in your browser.

## Build and run with Docker

Build the image from the folder containing the Dockerfile:

```bash
docker build -t student-management-ui:1.0 .
```

Run a container:

```bash
docker run --name student-ui -p 8501:8501 student-management-ui:1.0
```

Open http://localhost:8501.

Stop the container:

```bash
docker stop student-ui
```

Remove the stopped container:

```bash
docker rm student-ui
```

## Push the source code to GitHub

Create an empty GitHub repository, then run these commands from this project folder
(replace YOUR_USERNAME with your GitHub username):

```bash
git init
git add .
git commit -m "Initial student management UI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/python-student-management.git
git push -u origin main
```

## Build directly from the GitHub repository

After pushing the code, you can also build the image by cloning the repository:

```bash
git clone https://github.com/YOUR_USERNAME/python-student-management.git
cd python-student-management
docker build -t student-management-ui:1.0 .
docker run --name student-ui -p 8501:8501 student-management-ui:1.0
```
