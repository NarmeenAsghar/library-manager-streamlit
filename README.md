# 📚 Personal Library Manager 📚

## 🎯 Description
Personal Library Manager is a simple **Streamlit** application that helps users manage their book collection. It allows users to **add**, **remove**, **search**, and **display** books in their library. The app also provides basic **statistics** such as the total number of books and the percentage of books that have been read. It uses **session state** to persist data during the session.

## 🔧 Features
- **➕ Add a Book**: Add a new book to the library by specifying the title, author, publication year, genre, and read status.
- **❌ Remove a Book**: Remove a book from the library by its title.
- **🔍 Search for a Book**: Search for books based on title or author.
- **📖 Display All Books**: View the entire library with detailed book information.
- **📊 Display Statistics**: View statistics on the total number of books and the percentage of books that have been read.

## 🛠️ Installation

### 📋 Prerequisites
To run the Personal Library Manager, you need to have **Python 3.x** installed on your machine.

### 🚀 Setup
1. **Clone the repository**:
   ```bash
   git clone https://github.com/NarmeenAsghar/library-manager-streamlit.git
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   Create a `requirements.txt` file or use the following command to install the necessary libraries:
   ```bash
   pip install streamlit
   ```

4. **Run the app**:
   ```bash
   streamlit run app.py
   ```

5. The app will be available at `http://localhost:8501` in your browser. 🌐

## 🧑‍💻 Usage

Once the app is running, you will see the following menu options on the left sidebar:

- **➕ Add a book**: Add a new book to your library by entering the book's details.
- **❌ Remove a book**: Remove a book from your library by entering its title.
- **🔍 Search for a book**: Search for a book by title or author.
- **📖 Display all books**: View all the books in your library.
- **📊 Display statistics**: See statistics on the total books and the percentage read.
- **🚪 Exit**: Close the app.

### 📚 Example Usage

- **Add a Book**: Enter the title, author, publication year, genre, and whether you've read it or not. Click the "Add Book" button to save. ✅
- **Remove a Book**: Enter the title of the book you want to remove and click "Remove Book." 🧹
- **Search for a Book**: Choose whether to search by title or author, and enter the keyword. The app will display all matching books. 🔎
- **Display All Books**: View a list of all books in your library. 📜
- **Display Statistics**: See the total number of books and the percentage of books that have been read. 📊
