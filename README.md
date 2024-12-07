# Trading Utilities and Algorithms using IBKR API

This repository provides tools and frameworks for **algorithmic trading** using the **Interactive Brokers (IBKR) API**. It includes utilities for automating trades, managing orders, analyzing market data, and implementing algorithmic trading strategies.


## 🌟 Features

- **Market Data**: Fetch real-time and historical market data from IBKR.
- **Order Management**: Automate placing, modifying, and canceling orders.
- **Algorithmic Trading**:
  - Includes a sample **gap-up overnight trading** strategy.
  - Supports developing custom trading algorithms.
- **Utilities**: Modules for API connection, error handling, and price calculations.
- **Backtesting Support**: Test strategies using historical data.


## 📂 Project Structure
```plaintext
ALGOTRADING/
│
├── algorithm/
│   ├── gapUpOverNight.py   # Example trading strategy
│   ├── ...                 # Add your custom strategies here
│
├── data/
│   ├── historical.py       # Retrieve and process historical market data
│   ├── ...                 
│
├── utility/
│   ├── connection.py       # IBKR API connection utilities
│   ├── order.py            # Place and manage orders
│   ├── price.py            # Helper functions for price handling
│   ├── tickets.py          # Manage trade tickets and executions
│
├── notebook.ipynb          # Jupyter Notebook for demos and tests
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
```
Here’s the updated version from the Installation section onward, fully written in proper Markdown:


## ⚙️ Installation

### Prerequisites
1. **Interactive Brokers Account**:
   - Ensure you have an active IBKR account.
   - Enable API access in **TWS** (Trader Workstation) or **IB Gateway**.
2. **Python 3.8 or later**:
   - Make sure Python is installed on your system.

### Steps
1. Clone the repository:
```bash
   git clone https://github.com/yourusername/trading-ibkr.git
   cd trading-ibkr
```

2.	Install dependencies:
```bash
pip install -r requirements.txt
```

3.	Configure the IBKR API:
	•	Open utility/connection.py and update the host, port, and client ID settings to match your IBKR TWS or IB Gateway configuration.

### 🚀 Usage

Running Pre-Built Algorithms

You can run the pre-built gap-up overnight trading strategy using the following command:

```bash
python -m algorithm.gapUpOverNight
```

Developing Custom Strategies:

1.	Create a new Python script in the algorithm/ directory.
2.	Use the provided utilities (e.g., connection.py, order.py) to interact with the IBKR API.
3.	Implement your trading logic.

#### Example Code

Below is an example of how to connect to IBKR and place an order programmatically:

```python
from utility.connection import connect
from utility.order import submitOrder

# Establish connection to IBKR API
client = connect()

# Submit a market order to buy 10 shares of AAPL
submitOrder(client, action="BUY", symbol="AAPL", quantity=10)
```

### 🧪 Backtesting

The data/historical.py module enables you to retrieve historical market data, which you can use for testing your strategies. Example workflow:

1.	Fetch historical data for a symbol.
2.	Write a script to simulate trades based on your strategy logic.
3.	Analyze the performance metrics of your strategy.

### 💻 Contributing

We welcome contributions to enhance this repository! Here’s how you can contribute:

1.	Fork this repository.
2.	Create a feature branch:

```bash
git checkout -b feature-name
```


3.	Commit your changes:
```bash
git commit -m "Add new feature or fix"
```

4.	Push your branch:
```bash
git push origin feature-name
```

5.	Submit a pull request for review.

### ⚠️ Disclaimer

This project is for educational purposes only. Algorithmic trading carries risks. Always test your strategies extensively in simulated environments before deploying them to live trading. The maintainers are not responsible for any financial losses or API-related issues.

### 📜 License

This repository is licensed under the MIT License. You can find the full license text in the LICENSE file.

This version ensures the entire document uses proper Markdown syntax for headings, code blocks, lists, and other elements. Let me know if there are more changes you’d like!