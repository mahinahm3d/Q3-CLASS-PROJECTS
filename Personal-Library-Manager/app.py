import streamlit as st
import json
import os

# Data Model
class LibraryEntry:
    def __init__(self, title, author, year, genre, read_status):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.read_status = read_status

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "genre": self.genre,
            "read_status": self.read_status
        }

    @staticmethod
    def from_dict(data):
        return LibraryEntry(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            genre=data["genre"],
            read_status=data["read_status"]
        )

# Manager
class Library:
    def __init__(self, file_path="library.json"):
        self.file_path = file_path
        self.entries = []
        self.load()

    def load(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    self.entries = [LibraryEntry.from_dict(entry) for entry in json.load(file)]
            except json.JSONDecodeError:
                self.entries = []
        else:
            self.entries = []

    def save(self):
        with open(self.file_path, "w") as file:
            json.dump([entry.to_dict() for entry in self.entries], file, indent=4)

    def add(self, entry):
        self.entries.append(entry)
        self.save()

    def remove(self, title):
        self.entries = [entry for entry in self.entries if entry.title.lower() != title.lower()]
        self.save()

    def filter(self, genre=None, read_status=None):
        filtered = self.entries
        if genre:
            filtered = [e for e in filtered if e.genre.lower() == genre.lower()]
        if read_status is not None:
            filtered = [e for e in filtered if e.read_status == read_status]
        return filtered

    def stats(self):
        total = len(self.entries)
        read = sum(1 for e in self.entries if e.read_status)
        return total, read, (read / total * 100) if total > 0 else 0


# --- Streamlit App ---
st.set_page_config(page_title="Personal Library", layout="centered")
st.title("My Library")

lib = Library()

# Add Entry
st.subheader("Add Entry")
with st.form("entry_form"):
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read_status = st.toggle("Read?", value=False)
    submitted = st.form_submit_button("Save")
    if submitted:
        if title and author:
            entry = LibraryEntry(title, author, year, genre, read_status)
            lib.add(entry)
            st.success("Entry saved.")
        else:
            st.warning("Title and Author are required.")

st.divider()

# Filters
st.subheader("Browse")
genre_filter = st.text_input("Filter by genre", placeholder="e.g. Sci-Fi")
read_filter = st.selectbox("Read status", ["All", "Read", "Unread"])
read_map = {"All": None, "Read": True, "Unread": False}

# List Entries
filtered = lib.filter(genre_filter, read_map[read_filter])
for entry in filtered:
    col1, col2 = st.columns([0.9, 0.1])
    with col1:
        status = "✅" if entry.read_status else "❌"
        st.markdown(f"**{entry.title}** by {entry.author} ({entry.year}) — *{entry.genre}* {status}")
    with col2:
        if st.button("Delete", key=entry.title):
            lib.remove(entry.title)
            st.experimental_rerun()

st.divider()

# Stats
st.subheader("Summary")
total, read, percent = lib.stats()
cols = st.columns(3)
cols[0].metric("Total", total)
cols[1].metric("Read", read)
cols[2].metric("Completion", f"{percent:.2f}%")

