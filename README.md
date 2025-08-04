from pathlib import Path

readme_content = """
# 📚 Library Management System (Python + Tkinter)

A feature-rich **Library Management System** with a graphical interface built using Python and Tkinter. It supports user authentication, book issuing/returning, fine calculation, usage analytics, and AI-powered book recommendations.

---

## 🚀 Features

- 🔐 Admin & User Login System
- 📘 Add, View, Issue & Return Books
- 📅 Due Date Management with Fine Calculation
- 🧠 AI-based Book Recommendations (based on search patterns)
- 📊 Usage Stats & Analytics Dashboard
- 🔍 Book Search Functionality
- 💾 JSON-based Data Storage (no DB required)
- 🖥️ Responsive GUI with Tkinter

---

## 🛠 Technologies Used

- Python 3.x
- Tkinter (GUI)
- JSON (Data Storage)
- Standard Python Libraries

---

## 📂 File Structure

```bash
📁 library_management_system/
├── main.py # Main application file with GUI logic
├── users.json # Stores user login credentials
├── books.json # Book data and issuance records
├── stats.json # Analytics and usage stats
├── README.md # Project documentation
```

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/SupritMandal015/Advance-Library-Manangement-System.git
```

## 2️⃣ Run the Application

```bash
python library_management_system.py
```

---

## 🧪 Sample Admin Credentials

- **Username:** `admin`
- Password:** `admin123`
- Users can register from the login screen.

 ---

## 📌 Notes 


- Fine is calculated as ₹2 per day after the due date.

- Recommendations improve as more books are issued/searched.

- Data is persisted using JSON files in the current directory.

