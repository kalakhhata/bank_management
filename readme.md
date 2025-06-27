### 🏦 Banking System - Object-Oriented Programming Project

This project simulates a simple banking system using core OOP principles in Python. Users can create accounts, deposit and withdraw money, transfer funds, and view transaction history — all from a command-line interface.

---

### 📌 Features

- Create new bank accounts (savings or current)
- Deposit and withdraw funds with validation
- Check account balance
- Transfer money between accounts
- View transaction history with timestamps
- Account management via a centralized `Bank` class

---

### 🧠 Concepts Practiced

- Encapsulation and data hiding
- Inheritance (`SavingsAccount` and `CurrentAccount`)
- Polymorphism (custom `withdraw` and `deposit` logic)
- Abstraction and modular design
- Class interaction and object lifecycle management

---

### 🛠️ Tech Stack

- Language: Python 3
- Interface: Command-Line (CLI)
- Modules: `datetime`, custom OOP design

---

### 📂 File Structure (Sample)

```
banking_system/
├── main.py               # CLI menu and app runner
├── bank.py               # Bank class for managing accounts
├── account.py            # Account, SavingsAccount, CurrentAccount classes
├── transaction.py        # Optional transaction history tracker
└── README.md             # Project overview and instructions
```

---

### 🚀 How to Run

```bash
python main.py
```

---

### 🙌 Contributions

Feel free to fork this repo, suggest improvements, or add new features like:

- User authentication (PIN)
- Interest calculation for savings accounts
- GUI using Tkinter or Flask

---
