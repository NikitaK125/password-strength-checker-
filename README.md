# 🔐 Password Strength Checker

A Python tool that analyzes your password and tells you exactly how secure it is — with detailed feedback and improvement tips.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 💻 Demo

```
==================================================
   🔐 Password Strength Checker
   Check how secure your password is!
==================================================

Enter password: hello123

==================================================
  Password : ********
  Strength : 🟠 WEAK
  Score    : 3 points
  Meter    : [██░░░]
==================================================

📋 Analysis:
   ⚠️  Minimum length met (8+ characters)
   ❌ Missing uppercase letters (A-Z)
   ✅ Contains lowercase letters
   ✅ Contains multiple digits
   ❌ Missing special characters (!@#$%^&*...)

💡 Suggestions:
   → Make your password at least 12 characters long
   → Add uppercase letters like A, B, C...
   → Add special characters like @, #, $, !
```

---

## ✨ Features

- 📏 Length analysis (short / good / great)
- 🔠 Uppercase & lowercase detection
- 🔢 Digit count check
- 💥 Special character detection
- 🚨 Common password blacklist (15 passwords)
- 🔁 Repeated character detection
- 🔢 Sequential pattern detection (abc, 123)
- 📊 Visual strength meter
- 💡 Actionable improvement suggestions
- ✅ Zero external dependencies

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/password-strength-checker.git

# Navigate into folder
cd password-strength-checker

# Run it
python password_checker.py
```

---

## 🧪 Run Tests

```bash
python test_password_checker.py
```

---

## 📁 Project Structure

```
password-strength-checker/
│
├── password_checker.py        # Main program
├── test_password_checker.py   # Unit tests
├── requirements.txt           # Dependencies (none!)
└── README.md                  # You are here
```

---

## 📊 Scoring System

| Check | Points |
|---|---|
| Length 16+ chars | +3 |
| Length 12+ chars | +2 |
| Length 8+ chars | +1 |
| Uppercase letters | +1 |
| Lowercase letters | +1 |
| 2+ digits | +2 |
| 2+ special chars | +2 |
| Common password | -3 |
| Repeated chars | -1 |
| Sequential pattern | -1 |

| Score | Strength |
|---|---|
| 0–2 | 🔴 Very Weak |
| 3–4 | 🟠 Weak |
| 5–6 | 🟡 Moderate |
| 7–8 | 🟢 Strong |
| 9+ | 💪 Very Strong |

---

## 🌱 Future Improvements

- [ ] Add a GUI using Tkinter
- [ ] Show estimated time to crack the password
- [ ] Export results to a text file
- [ ] Add more common password patterns

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙋‍♂️ Author

Made with ❤️ and Python by **YOUR_NAME**  
⭐ Star this repo if you found it helpful!
