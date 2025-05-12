# 📘 BookWorld - A Flask Book Management App

**BookWorld** is a lightweight web application built with Flask. It allows users to browse, add, and search for books in a clean, responsive interface.

## 🚀 Features

- View a list of available books
- Add new books via a form
- View detailed info about each book
- Search for books by title
- Responsive navigation bar
- Professional UI with separate CSS per page

## 📁 Project Structure

```

book-web-app/
│
├── static/
│   └── css/
│       ├── base.css
│       ├── books.css
│       ├── home.css
│       ├── add\_book.css
│       └── book\_detail.css
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── books.html
│   ├── add\_book.html
│   ├── book\_detail.html
│   └── search.html
│
├── books.json
├── app.py
├── requirements.txt
└── README.md

````

## 🛠 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/sparknet-innovations/book-web-app.git
cd book-web-app
````

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install the dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
python app.py
```

5. **Open your browser**

```
http://127.0.0.1:5000/
```


