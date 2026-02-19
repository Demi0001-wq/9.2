# Demi Banking Widget

## Description
This project is a banking widget application that provides utility functions for masking sensitive data (card and account numbers), processing dates, and filtering/sorting transaction records.

## Features
- **Data Masking**: Securely mask card and account numbers.
- **Date Processing**: Format dates from ISO strings.
- **Transaction Filtering**: Filter transactions by status (e.g., `EXECUTED`, `CANCELED`).
- **Transaction Sorting**: Sort transactions by date in ascending or descending order.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd demi
   ```
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage
You can run the demonstration script:
```bash
python main.py
```

### Examples
#### Filtering Transactions
```python
from src.processing import filter_by_state

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2023-01-01'},
    {'id': 2, 'state': 'CANCELED', 'date': '2023-01-02'}
]
executed = filter_by_state(data, 'EXECUTED')
```

#### Sorting Transactions
```python
from src.processing import sort_by_date

sorted_data = sort_by_date(data, reverse=True)
```

## Development
- **GitFlow**: Development follows the GitFlow branching model.
- **Branching**:
  - `main`: Production-ready code.
  - `develop`: Main development branch.
  - `feature/homework_10_1`: Specific homework assignment branch.
