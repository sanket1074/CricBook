🏏 Cricket Stadium Seat Booking System

A web-based cricket stadium ticket booking application developed using Python Flask, MySQL, HTML, and CSS.
This system allows users to book cricket match tickets online while providing a secure admin panel to manage matches and view booking reports.

🚀 Features
👤 User

User Registration & Login

View available matches

Seat booking with payment simulation

View personal booking history

Logout functionality

🛡 Admin

Separate Admin Login

Add new matches

Set total seats and ticket price

Delete matches

View complete booking reports

💳 Payment Simulation

Simulated payment gateway (UPI / Card / Net Banking)

Automatic seat deduction after payment

🛠 Tech Stack
Layer	Technology
Frontend	HTML, CSS
Backend	Python Flask
Database	MySQL
Payment	Simulated Gateway
📁 Project Structure
cricket_booking/
│
├── app.py
├── database.sql
│
├── static/
│   └── style.css
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── admin_dashboard.html
│   ├── user_dashboard.html
│   ├── payment.html
│   ├── mybookings.html
│   └── report.html

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/cricket-booking-system.git
cd cricket-booking-system

2️⃣ Install Dependencies
pip install flask mysql-connector-python

3️⃣ Setup Database

Import database.sql into MySQL

Update your MySQL credentials in app.py

4️⃣ Run the Project
python app.py


Open browser:

http://127.0.0.1:5000

🔐 Default Admin Login
Email: admin@gmail.com
Password: admin123

🎓 Academic Purpose

This project is developed as a college mini / final year project to demonstrate:

Flask Web Development

Database Connectivity

Session Management

Payment Simulation

Admin & User Role Handling

📜 License

This project is for educational use only.
