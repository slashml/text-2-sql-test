import streamlit as st
import requests
import json
from datetime import datetime

# Set page config to wide mode
st.set_page_config(layout="wide")

def generate_sql_query(question, schema, instructions):
    base_prompt = f"""### Task
Generate a SQL query to answer [QUESTION]{{question}}[/QUESTION]

### Instructions
{instructions}

### Database Schema
This query will run on a database whose schema is represented in this string:
{{schema}}

### Answer
Given the database schema, here is the SQL query that answers [QUESTION]{{question}}[/QUESTION]
[SQL]
"""

    url = "http://3.17.59.73:8000/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }

    formatted_prompt = base_prompt.format(question=question, schema=schema)
    data = {
        "model": "slashml/text-to-sql",
        "messages": [
            {"role": "user", "content": formatted_prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    return response.json()['choices'][0]['message']['content']

def main():
    st.title("Text-to-SQL Generator")

    # Create two columns for the main layout
    left_column, right_column = st.columns([3, 2])

    with left_column:
        # Section 1: User Question
        st.header("Ask a Question")
        question = st.text_area("Enter your question about the database:", height=100)
        generate_button = st.button("Generate SQL", use_container_width=True)

        # Section 2: SQL Code Output
        st.header("SQL Query Result")
        sql_output = st.empty()

    with right_column:
        # Section 3: Database Schema
        st.header("Database Schema")
        default_schema = """CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(200) NOT NULL,
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""
        schema = st.text_area("Enter or modify the database schema:", value=default_schema, height=300)

        # Section 4: Special Instructions
        st.header("Special Instructions")
        default_instructions = """- If the question cannot be answered given the database schema, return "I do not know"
- Recall that the current date in YYYY-MM-DD format is {current_date}""".format(current_date=datetime.now().strftime("%Y-%m-%d"))
        instructions = st.text_area("Enter any special instructions:", value=default_instructions, height=100)

    # Generate SQL when the button is clicked
    if generate_button:
        if question and schema:
            with st.spinner("Generating SQL query..."):
                result = generate_sql_query(question, schema, instructions)
            sql_output.code(result, language="sql")
        else:
            st.warning("Please enter both a question and a database schema.")

if __name__ == "__main__":
    main()