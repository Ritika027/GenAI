# 💱 Currency Converter using API & Tool Calling

## 📌 Project Description

This project is a **Currency Converter** that uses an external **Exchange Rate API** along with **LangChain Tool Calling** to perform real-time currency conversions. The system leverages a Large Language Model (LLM) to understand user queries and automatically decide when to call the conversion tool.

Instead of manually handling API calls, the LLM intelligently triggers the tool, fetches the latest exchange rates, and returns accurate results to the user.

---

## 🚀 Features

* 🌍 Real-time currency conversion (e.g., USD to INR)
* 🤖 Intelligent tool calling using LangChain
* 🔗 Integration with external API for live data
* ⚡ Automated workflow (LLM + Tool execution)
* 📊 Accurate and dynamic responses

---

## 🛠️ Tech Stack

* Python
* LangChain
* OpenAI / LLM
* Exchange Rate API
* Requests Library

---

## ⚙️ How It Works

1. User enters a query like “Convert USD to INR”
2. LLM processes the input and detects the need for a tool
3. Tool (`get_conversion_factor`) is invoked automatically
4. API call is made to fetch live exchange rate
5. Tool returns the result to the LLM
6. LLM generates the final human-readable response

---

## 🔧 Tool Description

### `get_conversion_factor`

This function is responsible for:

* Taking `base_currency` and `target_currency` as input
* Calling the exchange rate API
* Returning conversion data in JSON format

---

## 📡 API Integration

The project uses an Exchange Rate API to fetch real-time currency values, ensuring up-to-date and accurate conversions.

---

## ▶️ Usage

* Run the application
* Provide a currency conversion query
* The system automatically processes and returns the result

---

## 💡 Example

**Input:**
Convert USD to INR

**Output:**
1 USD = 83.2 INR (example)

---

## 📈 Future Enhancements

* Support for custom amount conversion (e.g., 100 USD)
* UI integration using Streamlit
* Support for multiple currencies at once
* Performance optimization with caching

---

## 👩‍💻 Author

This project is built to demonstrate **API integration with LangChain tool calling** and how LLMs can automate real-world tasks like currency conversion.

---
