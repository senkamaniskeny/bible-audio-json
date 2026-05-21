import json
import os

# Define all 66 books with their information
books_data = [
    # Old Testament - Pentateuch
    {"name": "Genesis", "number": 1, "testament": "OT", "chapters": 50, "category": "Pentateuch"},
    {"name": "Exodus", "number": 2, "testament": "OT", "chapters": 40, "category": "Pentateuch"},
    {"name": "Leviticus", "number": 3, "testament": "OT", "chapters": 27, "category": "Pentateuch"},
    {"name": "Numbers", "number": 4, "testament": "OT", "chapters": 36, "category": "Pentateuch"},
    {"name": "Deuteronomy", "number": 5, "testament": "OT", "chapters": 34, "category": "Pentateuch"},
    
    # Old Testament - Historical Books
    {"name": "Joshua", "number": 6, "testament": "OT", "chapters": 24, "category": "Historical"},
    {"name": "Judges", "number": 7, "testament": "OT", "chapters": 21, "category": "Historical"},
    {"name": "Ruth", "number": 8, "testament": "OT", "chapters": 4, "category": "Historical"},
    {"name": "1 Samuel", "number": 9, "testament": "OT", "chapters": 31, "category": "Historical"},
    {"name": "2 Samuel", "number": 10, "testament": "OT", "chapters": 24, "category": "Historical"},
    {"name": "1 Kings", "number": 11, "testament": "OT", "chapters": 22, "category": "Historical"},
    {"name": "2 Kings", "number": 12, "testament": "OT", "chapters": 25, "category": "Historical"},
    {"name": "1 Chronicles", "number": 13, "testament": "OT", "chapters": 29, "category": "Historical"},
    {"name": "2 Chronicles", "number": 14, "testament": "OT", "chapters": 36, "category": "Historical"},
    {"name": "Ezra", "number": 15, "testament": "OT", "chapters": 10, "category": "Historical"},
    {"name": "Nehemiah", "number": 16, "testament": "OT", "chapters": 13, "category": "Historical"},
    {"name": "Esther", "number": 17, "testament": "OT", "chapters": 10, "category": "Historical"},
    
    # Old Testament - Wisdom Literature
    {"name": "Job", "number": 18, "testament": "OT", "chapters": 42, "category": "Wisdom"},
    {"name": "Psalms", "number": 19, "testament": "OT", "chapters": 150, "category": "Wisdom"},
    {"name": "Proverbs", "number": 20, "testament": "OT", "chapters": 31, "category": "Wisdom"},
    {"name": "Ecclesiastes", "number": 21, "testament": "OT", "chapters": 12, "category": "Wisdom"},
    {"name": "Song of Solomon", "number": 22, "testament": "OT", "chapters": 8, "category": "Wisdom"},
    
    # Old Testament - Major Prophets
    {"name": "Isaiah", "number": 23, "testament": "OT", "chapters": 66, "category": "Major Prophets"},
    {"name": "Jeremiah", "number": 24, "testament": "OT", "chapters": 52, "category": "Major Prophets"},
    {"name": "Lamentations", "number": 25, "testament": "OT", "chapters": 5, "category": "Major Prophets"},
    {"name": "Ezekiel", "number": 26, "testament": "OT", "chapters": 48, "category": "Major Prophets"},
    {"name": "Daniel", "number": 27, "testament": "OT", "chapters": 12, "category": "Major Prophets"},
    
    # Old Testament - Minor Prophets
    {"name": "Hosea", "number": 28, "testament": "OT", "chapters": 14, "category": "Minor Prophets"},
    {"name": "Joel", "number": 29, "testament": "OT", "chapters": 3, "category": "Minor Prophets"},
    {"name": "Amos", "number": 30, "testament": "OT", "chapters": 9, "category": "Minor Prophets"},
    {"name": "Obadiah", "number": 31, "testament": "OT", "chapters": 1, "category": "Minor Prophets"},
    {"name": "Jonah", "number": 32, "testament": "OT", "chapters": 4, "category": "Minor Prophets"},
    {"name": "Micah", "number": 33, "testament": "OT", "chapters": 7, "category": "Minor Prophets"},
    {"name": "Nahum", "number": 34, "testament": "OT", "chapters": 3, "category": "Minor Prophets"},
    {"name": "Habakkuk", "number": 35, "testament": "OT", "chapters": 3, "category": "Minor Prophets"},
    {"name": "Zephaniah", "number": 36, "testament": "OT", "chapters": 3, "category": "Minor Prophets"},
    {"name": "Haggai", "number": 37, "testament": "OT", "chapters": 2, "category": "Minor Prophets"},
    {"name": "Zechariah", "number": 38, "testament": "OT", "chapters": 14, "category": "Minor Prophets"},
    {"name": "Malachi", "number": 39, "testament": "OT", "chapters": 4, "category": "Minor Prophets"},
    
    # New Testament - Gospels
    {"name": "Matthew", "number": 40, "testament": "NT", "chapters": 28, "category": "Gospels"},
    {"name": "Mark", "number": 41, "testament": "NT", "chapters": 16, "category": "Gospels"},
    {"name": "Luke", "number": 42, "testament": "NT", "chapters": 24, "category": "Gospels"},
    {"name": "John", "number": 43, "testament": "NT", "chapters": 21, "category": "Gospels"},
    
    # New Testament - Acts
    {"name": "Acts", "number": 44, "testament": "NT", "chapters": 28, "category": "Acts"},
    
    # New Testament - Paul's Epistles
    {"name": "Romans", "number": 45, "testament": "NT", "chapters": 16, "category": "Paul's Epistles"},
    {"name": "1 Corinthians", "number": 46, "testament": "NT", "chapters": 16, "category": "Paul's Epistles"},
    {"name": "2 Corinthians", "number": 47, "testament": "NT", "chapters": 13, "category": "Paul's Epistles"},
    {"name": "Galatians", "number": 48, "testament": "NT", "chapters": 6, "category": "Paul's Epistles"},
    {"name": "Ephesians", "number": 49, "testament": "NT", "chapters": 6, "category": "Paul's Epistles"},
    {"name": "Philippians", "number": 50, "testament": "NT", "chapters": 4, "category": "Paul's Epistles"},
    {"name": "Colossians", "number": 51, "testament": "NT", "chapters": 4, "category": "Paul's Epistles"},
    {"name": "1 Thessalonians", "number": 52, "testament": "NT", "chapters": 5, "category": "Paul's Epistles"},
    {"name": "2 Thessalonians", "number": 53, "testament": "NT", "chapters": 3, "category": "Paul's Epistles"},
    {"name": "1 Timothy", "number": 54, "testament": "NT", "chapters": 6, "category": "Paul's Epistles"},
    {"name": "2 Timothy", "number": 55, "testament": "NT", "chapters": 4, "category": "Paul's Epistles"},
    {"name": "Titus", "number": 56, "testament": "NT", "chapters": 3, "category": "Paul's Epistles"},
    {"name": "Philemon", "number": 57, "testament": "NT", "chapters": 1, "category": "Paul's Epistles"},
    
    # New Testament - Hebrews
    {"name": "Hebrews", "number": 58, "testament": "NT", "chapters": 13, "category": "Hebrews"},
    
    # New Testament - James
    {"name": "James", "number": 59, "testament": "NT", "chapters": 5, "category": "James"},
    
    # New Testament - Peter's Epistles
    {"name": "1 Peter", "number": 60, "testament": "NT", "chapters": 5, "category": "Peter's Epistles"},
    {"name": "2 Peter", "number": 61, "testament": "NT", "chapters": 3, "category": "Peter's Epistles"},
    
    # New Testament - John's Epistles
    {"name": "1 John", "number": 62, "testament": "NT", "chapters": 5, "category": "John's Epistles"},
    {"name": "2 John", "number": 63, "testament": "NT", "chapters": 1, "category": "John's Epistles"},
    {"name": "3 John", "number": 64, "testament": "NT", "chapters": 1, "category": "John's Epistles"},
    
    # New Testament - Jude
    {"name": "Jude", "number": 65, "testament": "NT", "chapters": 1, "category": "Jude"},
    
    # New Testament - Revelation
    {"name": "Revelation", "number": 66, "testament": "NT", "chapters": 22, "category": "Revelation"},
]

# Create directories
os.makedirs('api/v1/niv/reference', exist_ok=True)
os.makedirs('api/v1/niv/reference/ot', exist_ok=True)
os.makedirs('api/v1/niv/reference/nt', exist_ok=True)

def get_book_slug(name):
    """Convert book name to URL slug."""
    return name.lower().replace(' ', '_')

def get_bible_gateway_url(book_name, chapter=None):
    """Generate Bible Gateway URL for a book."""
    slug = get_book_slug(book_name)
    base = f"https://www.biblegateway.com/passage/?search={book_name}&version=NIV"
    return base

def get_youversion_url(book_name, chapter=None):
    """Generate YouVersion/Bible.com URL for a book."""
    base = f"https://www.bible.com/search?q={book_name}&version=111"  # 111 is NIV
    return base

def get_api_bible_url(book_name):
    """Generate API.Bible reference URL."""
    return f"https://docs.api.bible/#/bibles/getVerses?book={get_book_slug(book_name)}"

# Generate metadata for each book
for book in books_data:
    book_slug = get_book_slug(book['name'])
    
    # Create reference data for each book
    reference_data = {
        "book": {
            "name": book['name'],
            "number": book['number'],
            "testament": book['testament'],
            "chapters": book['chapters'],
            "category": book['category']
        },
        "translation": {
            "name": "New International Version",
            "abbreviation": "NIV",
            "version": "2011",
            "language": "English",
            "copyright": "Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®",
            "publisher": "Biblica, Inc.",
            "license_url": "https://www.biblica.com/",
            "note": "This API provides reference links only. No copyrighted text is reproduced."
        },
        "official_sources": {
            "bible_gateway": {
                "name": "Bible Gateway",
                "url": get_bible_gateway_url(book['name']),
                "description": "Search and read NIV Bible on Bible Gateway"
            },
            "youversion": {
                "name": "YouVersion (Bible.com)",
                "url": get_youversion_url(book['name']),
                "description": "Read NIV Bible on YouVersion platform",
                "app_url": "https://www.bible.com"
            },
            "api_bible": {
                "name": "API.Bible",
                "url": "https://scripture.api.bible/",
                "description": "Access NIV through API.Bible (requires free signup)",
                "docs": "https://docs.api.bible/"
            }
        },
        "search_instructions": {
            "bible_gateway": f"Visit https://www.biblegateway.com and search for '{book['name']}' with NIV translation",
            "youversion": f"Visit https://www.bible.com and search for '{book['name']}' or download the app",
            "api_bible": "Sign up at https://api.bible/sign-up and use their API endpoints"
        }
    }
    
    # Save individual book reference
    testament_dir = "ot" if book['testament'] == "OT" else "nt"
    with open(f'api/v1/niv/reference/{testament_dir}/{book_slug}.json', 'w') as f:
        json.dump(reference_data, f, indent=2)

# Generate testament-level metadata
ot_books = [b for b in books_data if b['testament'] == 'OT']
nt_books = [b for b in books_data if b['testament'] == 'NT']

ot_reference = {
    "testament": "Old Testament",
    "books_count": len(ot_books),
    "chapters_count": sum(b['chapters'] for b in ot_books),
    "books": [
        {
            "name": b['name'],
            "number": b['number'],
            "chapters": b['chapters'],
            "category": b['category'],
            "reference_endpoint": f"/api/v1/niv/reference/ot/{get_book_slug(b['name'])}.json"
        }
        for b in ot_books
    ],
    "translation": {
        "name": "New International Version",
        "abbreviation": "NIV",
        "version": "2011",
        "copyright": "Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®"
    }
}

nt_reference = {
    "testament": "New Testament",
    "books_count": len(nt_books),
    "chapters_count": sum(b['chapters'] for b in nt_books),
    "books": [
        {
            "name": b['name'],
            "number": b['number'],
            "chapters": b['chapters'],
            "category": b['category'],
            "reference_endpoint": f"/api/v1/niv/reference/nt/{get_book_slug(b['name'])}.json"
        }
        for b in nt_books
    ],
    "translation": {
        "name": "New International Version",
        "abbreviation": "NIV",
        "version": "2011",
        "copyright": "Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®"
    }
}

# Generate complete reference
all_reference = {
    "bible": {
        "name": "Holy Bible",
        "translation": "New International Version (NIV)",
        "version": "2011",
        "total_books": len(books_data),
        "total_chapters": sum(b['chapters'] for b in books_data),
        "copyright": "Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®",
        "publisher": "Biblica, Inc.",
        "license_url": "https://www.biblica.com/"
    },
    "note": "This is a reference API that provides links to official NIV Bible sources. No copyrighted text is reproduced. Users should access the actual Bible text through the official sources listed below.",
    "old_testament": {
        "books": len(ot_books),
        "chapters": sum(b['chapters'] for b in ot_books),
        "reference_endpoint": "/api/v1/niv/reference/ot.json"
    },
    "new_testament": {
        "books": len(nt_books),
        "chapters": sum(b['chapters'] for b in nt_books),
        "reference_endpoint": "/api/v1/niv/reference/nt.json"
    },
    "official_sources": {
        "bible_gateway": {
            "name": "Bible Gateway",
            "url": "https://www.biblegateway.com",
            "description": "Search and read NIV Bible online"
        },
        "youversion": {
            "name": "YouVersion (Bible.com)",
            "url": "https://www.bible.com",
            "description": "Read NIV Bible on web or mobile app"
        },
        "api_bible": {
            "name": "API.Bible",
            "url": "https://scripture.api.bible/",
            "description": "Access NIV through free API (requires signup)"
        },
        "biblica": {
            "name": "Biblica (Copyright Holder)",
            "url": "https://www.biblica.com/",
            "description": "Official NIV publisher and copyright holder"
        }
    }
}

# Save all reference files
with open('api/v1/niv/reference/all.json', 'w') as f:
    json.dump(all_reference, f, indent=2)

with open('api/v1/niv/reference/ot.json', 'w') as f:
    json.dump(ot_reference, f, indent=2)

with open('api/v1/niv/reference/nt.json', 'w') as f:
    json.dump(nt_reference, f, indent=2)

print("NIV Reference API generated successfully!")
print(f"  - Old Testament: {len(ot_books)} books, {sum(b['chapters'] for b in ot_books)} chapters")
print(f"  - New Testament: {len(nt_books)} books, {sum(b['chapters'] for b in nt_books)} chapters")
print(f"  - Total: {len(books_data)} books, {sum(b['chapters'] for b in books_data)} chapters")
print(f"  - Total endpoints: {len(books_data) + 3} JSON files")
