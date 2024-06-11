from ebooklib import epub
from bs4 import BeautifulSoup
import re

def clean_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text()
    # Remove various forms of "Page xx"
    cleaned_text = re.sub(r'\b(\d{1,4} \| Page|Page \d{1,4}|\d{1,4} \. Page|\d{1,4} Page)\b', '', text)
    # Fix line breaks
    cleaned_text = re.sub(r'\.\n', '. ', cleaned_text)
    return cleaned_text

def clean_epub(input_file, output_file):
    book = epub.read_epub(input_file)
    for item in book.get_items():
        if item.get_type() == epub.ITEM_DOCUMENT:
            cleaned_content = clean_html(item.get_content().decode('utf-8'))
            item.set_content(cleaned_content.encode('utf-8'))
    epub.write_epub(output_file, book)

# Change this to your file paths
input_path = '/home/documents/book.epub'
output_path = '/home/documents/cleaned_book.epub'

clean_epub(input_path, output_path)
