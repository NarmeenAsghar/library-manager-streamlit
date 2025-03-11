import streamlit as st

# Initialize library in session state if it doesn't exist
if 'library' not in st.session_state:
    st.session_state.library = []

# adding function 
def add_book(title, author, year, genre, read_status):
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    st.session_state.library.append(book)

# removing function
def remove_book(title):
    st.session_state.library = [book for book in st.session_state.library if book["title"].lower() != title.lower()]

# searching function
def search_books(search_by, search_value):
    result = []
    for book in st.session_state.library:
        if search_by == "Title" and search_value.lower() in book["title"].lower():
            result.append(book)
        elif search_by == "Author" and search_value.lower() in book["author"].lower():
            result.append(book)
    return result

# displaying function
def display_books():
    if st.session_state.library:
        for idx, book in enumerate(st.session_state.library, start=1):
            status = "Read" if book["read_status"] else "Unread"
            st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.write("📚 Your library is empty. 📚")

def display_statistics():
    total_books = len(st.session_state.library)
    read_books = len([book for book in st.session_state.library if book["read_status"]])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0
    st.write(f"📘 Total books: {total_books}")
    st.write(f"📖 Percentage read: {percentage_read:.2f}%")

def main():
    st.title("📚 Personal Library Manager 📚")

    # Menubar
    menu = ["➕ Add a book", "❌ Remove a book", "🔍 Search for a book", "📖 Display all books", "📊 Display statistics", "🚪 Exit"]
    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == "➕ Add a book":
        st.subheader("Add a New Book 📝")
        title = st.text_input("Enter the book title")
        author = st.text_input("Enter the author")
        year = st.number_input("Enter the publication year", min_value=1000, max_value=9999)
        genre = st.text_input("Enter the genre")
        read_status = st.radio("Have you read this book?", ("Yes", "No"))

        if read_status == "Yes":
            read_status = True
        else:
            read_status = False

        if st.button("Add Book ✅"):
            add_book(title, author, year, genre, read_status)
            st.success(f"'{title}' added successfully! 🎉")

    elif choice == "❌ Remove a book":
        st.subheader("Remove a Book 🗑️")
        title_to_remove = st.text_input("Enter the title of the book to remove")
        if st.button("Remove Book 🧹"):
            remove_book(title_to_remove)
            st.success(f"'{title_to_remove}' removed successfully! ✂️")

    elif choice == "🔍 Search for a book":
        st.subheader("Search Books 🔎")
        search_by = st.radio("Search by:", ["Title", "Author"])
        search_value = st.text_input(f"Enter the {search_by.lower()} to search for")
        if st.button("Search 🔍"):
            results = search_books(search_by, search_value)
            if results:
                for idx, book in enumerate(results, start=1):
                    status = "Read" if book["read_status"] else "Unread"
                    st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
            else:
                st.write(f"No books found matching '{search_value}' 😞.")

    elif choice == "📖 Display all books":
        st.subheader("Your Library 📚")
        display_books()

    elif choice == "📊 Display statistics":
        st.subheader("Library Statistics 📈")
        display_statistics()

    elif choice == "🚪 Exit":
        st.write("Thank you for using the Personal Library Manager. Goodbye! 👋")

if __name__ == "__main__":
    main()
