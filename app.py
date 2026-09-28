import streamlit as st
import csv
import os

CSV_FILE = "pacha_malayalam.csv"

if not os.path.exists(CSV_FILE):
    sample_data = [
        {"old_word": "ആലം", "phonetic": "alam", "meaning": "World, earth, universe"},
        {"old_word": "അവിവേകം", "phonetic": "avivekam", "meaning": "Lack of proper judgment or foolishness"}
    ]
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["old_word", "phonetic", "meaning"])
        writer.writeheader()
        writer.writerows(sample_data)

st.set_page_config(page_title="Pacha Malayalam Lexicon", page_icon="🏛️")
st.title("🏛️ Pacha Malayalam Digital Lexicon")
st.write("Search for old, rare, and regional Malayalam words that standard search engines miss.")

query = st.text_input("Search for a word (Type in Malayalam or English phonetic):")

if query:
    found_results = []
    with open(CSV_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if query.strip() in row['old_word'] or query.strip().lower() in row['phonetic'].lower():
                found_results.append(row)
                
    if found_results:
        st.success(f"Found {len(found_results)} result(s):")
        for item in found_results:
            st.markdown(f"### 📖 {item['old_word']}")
            st.write(f"**Meaning:** {item['meaning']}")
            st.divider()
    else:
        st.warning("❌ Word not found in your database yet.")
