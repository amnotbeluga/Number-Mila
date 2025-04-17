# 📞 Number-Mila — Phone Number Lookup Bot

**Number-Mila** is a Python-based command-line tool that checks phone number validity and retrieves detailed information such as the country, location, and coordinates using the [Numverify](https://numverify.com) and [OpenCage](https://opencagedata.com) APIs.

---

## ✨ Features

- ✅ Validates phone numbers using **Numverify API**
- 🌍 Retrieves geolocation data using **OpenCage API**
- 📌 Displays country, location, latitude, and longitude
- 🔁 Interactive CLI to look up multiple numbers
- 🔒 Secure API key management via `config.json`

---

## 📦 Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) library

Install the required package (if you don't have it already):

```bash
pip install requests
```

---

## 🚀 Getting Started

1. **Clone the repo:**

```bash
git clone https://github.com/amnotbeluga/Number-Mila.git
cd Number-Mila
```

2. **Run the script:**

```bash
python Number-Mila.py
```

3. **Enter your API keys** (only once, saved to `config.json`):

- [Get your Numverify API key](https://numverify.com/)
- [Get your OpenCage API key](https://opencagedata.com/)

4. **Start checking phone numbers!**  
   Example input: `+14155552671`

---

## 🧠 How It Works

- The script validates the phone number using **Numverify**.
- It retrieves geolocation data using **OpenCage**.
- If OpenCage fails to find a location, it falls back to Numverify coordinates (if available).
- All details are printed in a readable format.

---

## 📁 Project Structure

```
Number-Mila/
├── Number-Mila.py       # Main script
└── config.json          # Created on first run with your API keys
```

---

## 🔐 API Key Safety

Your API keys are stored locally in `config.json`.  
**Do not share or commit this file to public repositories.**

To prevent accidental commits:

```bash
echo "config.json" >> .gitignore
```

---

## 🚧 Roadmap

- GUI version with Tkinter or PyQt
- Option to export results as CSV/JSON
- More APIs for deeper number intelligence
- Country-specific formatting and info

---

## 🙌 Contributions

Pull requests are welcome!  
Fork it, improve it, and submit a PR.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📣 Credits

- [Numverify](https://numverify.com)
- [OpenCage Geocoder](https://opencagedata.com)

---
