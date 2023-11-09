# Your Project Name - Backend

This is the backend for ToDo. It is built with Django and Django Rest Framework.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/noobie7/TodoAppDjango
   ```

2. **Navigate to the project directory:**

   ```bash
   cd ToDoProject
   ```

3. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Create a superuser:**

   ```bash
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

8. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

The backend server will be running at `http://localhost:8000/`.
