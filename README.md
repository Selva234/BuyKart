1. Clone the Repository
git clone https://github.com/your-username/amazonApp.git
cd amazonApp

2. Create and Activate Virtual Environment
python -m venv venv
source venv/bin/activate        # On Windows use: venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Admin)
python manage.py createsuperuser

6. Run the Server
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to access the app.

