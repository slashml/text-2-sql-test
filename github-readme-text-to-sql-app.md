# Text-to-SQL Generator

This Streamlit app showcases a text-to-SQL model from slashML, allowing users to generate SQL queries from natural language questions about a given database schema.

## Features

- Ask questions about a database schema in natural language
- Generate SQL queries based on the questions
- Customize the database schema
- Add special instructions for query generation
- User-friendly interface with real-time results

## Requirements

- Python 3.7+
- Streamlit
- Requests

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/text-to-sql-generator.git
   cd text-to-sql-generator
   ```

2. Install the required packages:
   ```
   pip install streamlit requests
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to `http://localhost:8501` (or the URL provided in the terminal).

3. Use the app:
   - Enter your question about the database in the "Ask a Question" section.
   - Click the "Generate SQL" button to generate a SQL query.
   - View the generated SQL query in the "SQL Query Result" section.
   - Modify the database schema in the "Database Schema" section if needed.
   - Customize special instructions in the "Special Instructions" section.

## Customizing the App

- **Database Schema**: You can modify the default schema or add your own in the "Database Schema" section.
- **Special Instructions**: Add or modify instructions for the SQL generation in the "Special Instructions" section.

## API Integration

This app uses the slashML API to generate SQL queries. Make sure you have the correct API endpoint and credentials set up in the `generate_sql_query` function.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to slashML for providing the text-to-SQL model API.
- Built with Streamlit, making it easy to create data apps.

