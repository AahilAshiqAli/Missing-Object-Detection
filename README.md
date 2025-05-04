  The Missing Object Detector utilizes YOLO for image localization and object detection within a room. The system
  generates accurate bounding boxes around identified objects, allowing users to track their locations in real-time. Users
  can see objects that have been found at any point in history directly from their dashboard or landing page. Additionally,
  a secure login and logout system has been implemented.

  DEMO AVAILABLE ON GITHUB

  DJANGO, PYTHON, HTML, CSS, JAVASCRIPT, SQLITE

  <h1>How to run the code</h1>

1. **Clone the repository**
 ```bash
 git clone https://github.com/AahilAshiqAli/Missing-Object-Detection.git
 ```
   
2. **Navigate to the project folder**

  ```bash
  cd Missing-Object-Detection
  ```

3. **Install dependencies**

  ```bash
  python -m venv venv
  venv\Scripts\activate
  pip install -r requirements.txt
  ```

3. Run Migrations and Start the development server

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```



