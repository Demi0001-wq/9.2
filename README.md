# Banking Operations Widget

Banking utility for masking data, processing transaction records, and automated logging.

## Features
- **Masking**: Card and account numbers.
- **Processing**: Filtering and sorting transactions.
- **Generators**: Efficient iterative processing.
- **Decorators**: Automated function logging.

## Generators Module
The `src/generators.py` module provides tools for working with large volumes of transaction data:
- `filter_by_currency`: Filters transactions by currency code.
- `transaction_descriptions`: Yields descriptions for each transaction.
- `card_number_generator`: Generates bank card numbers in `XXXX XXXX XXXX XXXX` format.

## Decorators Module
The `src/decorators.py` module provides the `@log` decorator:
- Logs function name and result on success.
- Logs function name, error type, and inputs on failure.
- Optional `filename` argument to log to a file instead of the console.

## How to Run

### 1. Install Dependencies
Ensure you have `requests` and `python-dotenv` installed:
```bash
pip install requests python-dotenv
```

### 2. Set Up Environment Variables
Create a `.env` file in the root directory based on `.env.template` and add your [API Layer Key](https://apilayer.com/market/exchangerates_data-api):
```bash
API_KEY=your_actual_api_key_here
```

### 3. Usage Example
You can use the functions in your scripts like this:
```python
from src.utils import get_transactions
from src.external_api import convert_to_rub

# Get transactions from JSON
transactions = get_transactions("data/operations.json")

# Convert the first transaction to RUB
if transactions:
    rub_amount = convert_to_rub(transactions[0])
    print(f"Amount in RUB: {rub_amount}")
```

## Testing
Run tests with coverage:
```bash
pytest --cov=src --cov-report=term-missing
```
HTML coverage reports are saved in the `htmlcov/` directory.
