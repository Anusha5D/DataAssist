# 🧠 DataAssist: Natural Language SQL Interface

> Ask questions like you're talking to your database. No coding required.

---

## 📌 Overview

**DataAssist** is a user-friendly Streamlit-based tool powered by **Google Gemini AI**, built to help users interact with databases in plain English.

Instead of writing complex SQL queries, users can type queries like:

> "Show students with marks greater than 85"  
> "List all students from the Data Science class"

The app automatically converts the input to SQL using Gemini and fetches the results from an SQLite database — displayed in an interactive table.

---

## ✨ Features

- 🧠 Natural language interface using **Gemini AI**
- 💬 Ask questions — no SQL or programming needed
- 📊 Results shown in table format instantly
- 🔄 Upload your own `.db` SQLite database
- 🎨 Clean and professional **Streamlit UI**
- 🚀 Lightweight, works in browser — no setup for users

---

## 💼 Real-World Use Case: Teacher-Friendly Result Generation

### 🎓 **Context**  
Many teachers in colleges and schools handle internal marks data stored in Excel or databases. They often rely on IT support for filtering results like:

- Toppers in a subject
- Students scoring above a threshold
- List of students failing a subject
- Average class performance

### ✅ **Solution with DataAssist**  
Teachers can:

1. Upload their database (`student.db`)
2. Type queries like:
   - _“Who scored less than 35 marks?”_
   - _“Top 5 students in DevOps”_
   - _“Show marks of Anvesha and Lilavati”_
3. Instantly get results as a **sorted table**
4. Export or screenshot for report generation

🔗 **No SQL knowledge required**  
💡 **Saves hours of manual filtering & formula work**

---

## 🛠️ Tech Stack

| Tool | Role |
|------|------|
| **Python** | Core language |
| **Streamlit** | Frontend UI |
| **Google Generative AI (Gemini)** | NLP to SQL |
| **SQLite** | Local database |
| **Pandas** | Table rendering |
| **dotenv** | API key management |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8+
- A valid **Gemini API Key** (get from [makersuite.google.com](https://makersuite.google.com))

### 📦 Installation

```bash
git clone https://github.com/yourusername/dataassist.git
cd dataassist
pip install -r requirements.txt
