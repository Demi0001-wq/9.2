Banking Operations Widget

Banking utility for masking data, processing transactions, and logging.

Features
Masking card and account numbers
Filtering and sorting transactions
Efficient iterative processing
Automated function logging
CSV and Excel file reading support

How to Run

1 Install Dependencies
pip install pandas openpyxl requests python-dotenv

2 Set Up API Key
Create .env file and add API_KEY=your_key

3 Example Usage
from src.file_readers import read_csv, read_excel
transactions = read_csv("data/transactions.csv")
if transactions:
    print(transactions[0])

Testing
pytest --cov=src --cov-report=term-missing
