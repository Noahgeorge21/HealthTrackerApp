# Health Tracker CLI Application

A simple, interactive **command-line health tracking application** built in Python.  
This project allows users to create a profile, log health records, and view calculated BMI values over time — all through a terminal-based interface.

---

## 📌 Project Status

🚧 **Actively in development**

This project is being continuously expanded and refined. Planned enhancements include:

- User login and authentication
- Saving and loading user data (persistence)
- Deleting and editing health records
- Improved analytics and health trend insights
- Potential machine learning or statistical analysis features
- Enhanced user interface (CLI improvements or GUI exploration)

The current version focuses on core functionality and clean architecture.

---

## 🎯 Purpose & Motivation

This project was built as a hands-on way to **refresh and strengthen object-oriented programming (OOP) skills in Python**.

Rather than learning concepts in isolation, the goal was to:
- Design real objects with clear responsibilities
- Practice composition, ownership, and encapsulation
- Build a small but complete application from the ground up
- Reinforce object-oriented development through practical use

The project reflects a **learning-by-building approach**, where understanding emerges naturally through implementation, iteration, and refactoring.

---

## 🧠 Key Concepts Practiced

- Object-Oriented Programming (OOP)
- Composition over inheritance
- Object ownership and lifecycle management
- Encapsulation and separation of concerns
- CLI-based application flow and state management
- Incremental development and refactoring

---

## 🛠️ Current Features

- Create a user profile during runtime
- Add health records (weight, date)
- Automatic BMI calculation per record
- View all health records
- View most recent health record
- Interactive menu-driven CLI interface

---

## 🧩 Project Structure

- `Person`  
  Represents a user and owns all associated health records.

- `HealthRecord`  
  Represents a single health snapshot, including BMI calculation.

- CLI Controller  
  Handles user input, navigation, and application flow.

---

## 🚀 Future Enhancements

Some ideas currently being explored or planned:

- Multi-user support
- Persistent storage (files or database)
- Record deletion and editing
- Health trend visualization
- Basic analytics or ML-driven insights
- UI improvements beyond the terminal

---

## ▶️ How to Run

1. Clone the repository
2. Navigate to the project directory
3. Run the Python script:
   ```bash
   python HealthTracker.py
