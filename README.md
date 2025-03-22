
# Government Job Portal

The **Government Job Portal** is a Django-based project that scrapes and displays government job postings and services from various sources, providing users with a centralized platform for real-time job and service updates.

---

## Installation Guide

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository
Open your terminal or command prompt and run the following command:
```bash
git clone https://github.com/Rohan-A-R/govt-job-portal.git
```

### 2. Navigate to the Project Directory
```bash
cd govt-job-portal
```

### 3. Install `venv`
Install the virtual environment package:
```bash
pip install venv
```

### 4. Create and Activate the Virtual Environment
Create the virtual environment and activate it:
```bash
.\env\Scriptsctivate
```

### 5. Install Required Libraries
Install all required dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

### 6. Navigate to the Main Project Directory
```bash
cd .\jobmain\
```

### 7. Run the Development Server
Start the Django development server:
```bash
python manage.py runserver
```

### 8. Open the Application
You will see the following output in the terminal:
```
System check identified no issues (0 silenced).
March 22, 2025 - 09:45:25
Django version 5.1.5, using settings 'jobmain.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Press the `Ctrl` key and click on the provided link:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Features
- **Job Listings**: Automatically scrapes and displays government job postings.
- **Service Listings**: Provides a centralized platform for government-related services.
- **Search and Filtering**: Users can filter jobs and services by type, location, and keywords.
- **Real-Time Updates**: Data is updated periodically using automated scraping.
- **Responsive Design**: Built with Bootstrap for a user-friendly experience.

---

## Future Plans
- Integration with PostgreSQL for better database management.
- AI-based job and service recommendations for personalized user experiences.
- User authentication for saved jobs and alerts.

---

## Contributing
Feel free to contribute to this project by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

Happy coding! 🚀
