from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# -------- Gemini Setup --------
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-2.0-flash')
    response = model.generate_content([prompt, question])
    return response.text.strip()

def read_sql_query(sql, db="student.db"):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        columns = [description[0] for description in cur.description]
        conn.close()
        return pd.DataFrame(rows, columns=columns)
    except Exception as e:
        return f"Error: {e}"

# -------- Prompt --------
prompt = """
You are an AI assistant that converts English questions into SQL queries.

✅ Return only valid SQL queries  
❌ No explanations, no quotes, no markdown, no headings  

The database table is STUDENT with columns:
- NAME
- CLASS
- SECTION
- MARKS

Examples:

Q: Show all records  
A: SELECT * FROM STUDENT;

Q: Students with marks above 85  
A: SELECT * FROM STUDENT WHERE MARKS > 85;

Q: How many students are in DevOps class  
A: SELECT COUNT(*) FROM STUDENT WHERE CLASS = "Devops";

Q: What are the average marks?  
A: SELECT AVG(MARKS) FROM STUDENT;
"""

# -------- Streamlit UI --------
st.set_page_config(page_title="DataAssist - Query SQL with Natural Language", layout="wide")

# Sidebar
st.sidebar.title("📌 About DataAssist")
st.sidebar.markdown("""
**DataAssist** is an AI-powered app that helps users query SQL databases using plain English.

🔸 Designed for students, teachers, schools, offices  
🔸 Works with a preloaded demo database  
🔸 No SQL knowledge required

📘 *Try asking:*  
- "Who scored more than 90?"  
- "How many students in class A?"  
- "Show all data"

Powered by 💡 Google Gemini + Streamlit
""")

# Main UI
st.markdown("<h1 style='color:#2c3e50;'>🧠 DataAssist: Natural Language SQL Interface</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#34495e;'>Ask questions like you're talking to your database. No coding required.</p>", unsafe_allow_html=True)

st.markdown("#### 🗨️ Ask your question")
question = st.text_input("e.g. List students who scored more than 80 marks", key="input", label_visibility="collapsed")

if st.button("🚀 Run Query"):
    with st.spinner("Thinking..."):
        generated_sql = get_gemini_response(question, prompt)
        if not generated_sql.lower().startswith("select"):
            st.error("❌ Gemini returned an invalid SQL query. Try rephrasing.")
        else:
            result = read_sql_query(generated_sql)
            st.markdown("### 📊 Result")
            if isinstance(result, pd.DataFrame):
                if result.empty:
                    st.info("No matching records found.")
                else:
                    st.dataframe(result, use_container_width=True)
            else:
                st.error(result)

# -------- Light Theme CSS --------
st.markdown("""
<style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f8f9fa;
    }
    .stButton>button {
        background-color: #6366f1;
        color: white;
        font-weight: bold;
        padding: 0.5rem 1.2rem;
        border-radius: 8px;
        border: none;
    }
    .stTextInput>div>div>input {
        padding: 0.6rem;
        border-radius: 6px;
    }
</style>
""", unsafe_allow_html=True)
