# NIV Bible Reference API

A comprehensive reference API for the New International Version (NIV) Bible that provides links to official sources without reproducing copyrighted text. This API helps developers integrate NIV Bible references into their applications while respecting copyright and licensing requirements.

## 🎯 Purpose

This API serves as a **reference and discovery tool** that directs users to official NIV Bible sources. It does not reproduce copyrighted text but instead provides:

- Complete book and chapter metadata
- Direct links to official NIV sources
- Search instructions for multiple platforms
- Copyright and licensing information
- Integration guidance for developers

## 📋 Important Notice

**Copyright & Licensing:** The New International Version (NIV) Bible is protected by copyright held by Biblica, Inc. This API provides **reference links only** and does not reproduce any copyrighted Bible text. To access the actual Bible content, users must visit the official sources listed below.

## 🌐 Base URL

```text
https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/
```

## 📊 Bible Statistics

| Metric | Count |
|--------|-------|
| **Total Books** | 66 (39 OT + 27 NT) |
| **Total Chapters** | 1,189 (929 OT + 260 NT) |
| **Translation** | New International Version (NIV) 2011 |
| **Copyright** | © 1973, 1978, 1984, 2011 by Biblica, Inc.® |

## 📂 API Endpoints

### 1. Complete Bible Reference

#### All Books Reference
- **Endpoint:** `/api/v1/niv/reference/all.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/all.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/all.json)
- **Description:** Complete NIV Bible reference with all books and official sources

**Response Structure:**
```json
{
  "bible": {
    "name": "Holy Bible",
    "translation": "New International Version (NIV)",
    "version": "2011",
    "total_books": 66,
    "total_chapters": 1189,
    "copyright": "Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®",
    "publisher": "Biblica, Inc.",
    "license_url": "https://www.biblica.com/"
  },
  "note": "This is a reference API that provides links to official NIV Bible sources...",
  "official_sources": {
    "bible_gateway": {...},
    "youversion": {...},
    "api_bible": {...},
    "biblica": {...}
  }
}
```

### 2. Testament-Level References

#### Old Testament Reference
- **Endpoint:** `/api/v1/niv/reference/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot.json)
- **Description:** All 39 Old Testament books with metadata

#### New Testament Reference
- **Endpoint:** `/api/v1/niv/reference/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/nt.json)
- **Description:** All 27 New Testament books with metadata

**Response Structure:**
```json
{
  "testament": "Old Testament",
  "books_count": 39,
  "chapters_count": 929,
  "books": [
    {
      "name": "Genesis",
      "number": 1,
      "chapters": 50,
      "category": "Pentateuch",
      "reference_endpoint": "/api/v1/niv/reference/ot/genesis.json"
    }
  ],
  "translation": {
    "name": "New International Version",
    "abbreviation": "NIV",
    "version": "2011",
    "copyright": "Copyright © 1973, 1978, 1984, 2011 by Biblica, Inc.®"
  }
}
```

### 3. Individual Book References

#### Old Testament Books
- **Endpoint:** `/api/v1/niv/reference/ot/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot/genesis.json)

**Available OT Books:** genesis, exodus, leviticus, numbers, deuteronomy, joshua, judges, ruth, 1_samuel, 2_samuel, 1_kings, 2_kings, 1_chronicles, 2_chronicles, ezra, nehemiah, esther, job, psalms, proverbs, ecclesiastes, song_of_solomon, isaiah, jeremiah, lamentations, ezekiel, daniel, hosea, joel, amos, obadiah, jonah, micah, nahum, habakkuk, zephaniah, haggai, zechariah, malachi

#### New Testament Books
- **Endpoint:** `/api/v1/niv/reference/nt/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/nt/matthew.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/nt/matthew.json)

**Available NT Books:** matthew, mark, luke, john, acts, romans, 1_corinthians, 2_corinthians, galatians, ephesians, philippians, colossians, 1_thessalonians, 2_thessalonians, 1_timothy, 2_timothy, titus, philemon, hebrews, james, 1_peter, 2_peter, 1_john, 2_john, 3_john, jude, revelation

**Response Structure:**
```json
{
  "book": {
    "name": "Genesis",
    "number": 1,
    "testament": "OT",
    "chapters": 50,
    "category": "Pentateuch"
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
      "url": "https://www.biblegateway.com/passage/?search=Genesis&version=NIV",
      "description": "Search and read NIV Bible on Bible Gateway"
    },
    "youversion": {
      "name": "YouVersion (Bible.com)",
      "url": "https://www.bible.com/search?q=Genesis&version=111",
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
    "bible_gateway": "Visit https://www.biblegateway.com and search for 'Genesis' with NIV translation",
    "youversion": "Visit https://www.bible.com and search for 'Genesis' or download the app",
    "api_bible": "Sign up at https://api.bible/sign-up and use their API endpoints"
  }
}
```

## 🔗 Official NIV Sources

### 1. Bible Gateway
- **Website:** https://www.biblegateway.com
- **Features:** Search, read, and compare Bible versions online
- **NIV Access:** Free, no registration required
- **API:** Available with registration

### 2. YouVersion (Bible.com)
- **Website:** https://www.bible.com
- **Features:** Read Bible on web or mobile app
- **NIV Access:** Free, available in app
- **API:** Developer API available at https://developers.youversion.com/
- **Platform:** https://platform.youversion.com/

### 3. API.Bible
- **Website:** https://scripture.api.bible/
- **Features:** Nearly 2,500 Bible versions in 1,600+ languages
- **NIV Access:** Free tier available
- **Signup:** https://api.bible/sign-up
- **Documentation:** https://docs.api.bible/
- **Use Cases:** Non-commercial use allowed

### 4. Biblica (Copyright Holder)
- **Website:** https://www.biblica.com/
- **Role:** Official NIV publisher and copyright holder
- **Licensing:** Contact for commercial or special use cases
- **Products:** Study Bible apps, translations, resources

## 💻 Usage Examples

### JavaScript - Fetch Book Reference
```javascript
// Get Genesis reference
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot/genesis.json')
  .then(response => response.json())
  .then(data => {
    console.log('Book:', data.book.name);
    console.log('Chapters:', data.book.chapters);
    console.log('Bible Gateway:', data.official_sources.bible_gateway.url);
    console.log('YouVersion:', data.official_sources.youversion.url);
  });
```

### JavaScript - Fetch Testament Reference
```javascript
// Get all Old Testament books
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot.json')
  .then(response => response.json())
  .then(data => {
    console.log(`Old Testament: ${data.books_count} books, ${data.chapters_count} chapters`);
    data.books.forEach(book => {
      console.log(`${book.number}. ${book.name} - ${book.chapters} chapters`);
    });
  });
```

### Python - Process Reference Data
```python
import json
import requests

# Fetch all NIV reference
url = 'https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/all.json'
response = requests.get(url)
data = response.json()

print(f"Bible: {data['bible']['translation']}")
print(f"Total Books: {data['bible']['total_books']}")
print(f"Total Chapters: {data['bible']['total_chapters']}")
print(f"\nOfficial Sources:")
for source_name, source_info in data['official_sources'].items():
    print(f"  - {source_info['name']}: {source_info['url']}")
```

### cURL - Fetch References
```bash
# Get all NIV reference
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/all.json | jq '.bible'

# Get Matthew reference
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/nt/matthew.json | jq '.official_sources'

# Get Old Testament books list
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/niv/reference/ot.json | jq '.books[] | {name, chapters}'
```

## 📚 Book Categories

### Old Testament (39 books, 929 chapters)

**Pentateuch (5 books):** Genesis, Exodus, Leviticus, Numbers, Deuteronomy

**Historical Books (12 books):** Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther

**Wisdom Literature (5 books):** Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon

**Major Prophets (5 books):** Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel

**Minor Prophets (12 books):** Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi

### New Testament (27 books, 260 chapters)

**Gospels (4 books):** Matthew, Mark, Luke, John

**Acts (1 book):** Acts

**Paul's Epistles (13 books):** Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon

**Hebrews (1 book):** Hebrews

**James (1 book):** James

**Peter's Epistles (2 books):** 1 Peter, 2 Peter

**John's Epistles (3 books):** 1 John, 2 John, 3 John

**Jude (1 book):** Jude

**Revelation (1 book):** Revelation

## 🛠 Integration Guide

### Step 1: Fetch Reference Data
Use any of the endpoints above to get book metadata and official source links.

### Step 2: Display to Users
Show the book information and provide links to official sources where users can read the actual Bible text.

### Step 3: Direct to Official Sources
When users want to read the Bible, direct them to one of the official sources using the provided URLs.

### Step 4: Consider Using Official APIs
For programmatic access to actual Bible text, consider using one of the official APIs:
- **API.Bible** - Free tier, 2,500+ versions
- **YouVersion API** - Free tier with license agreements
- **Bible Gateway API** - Requires registration

## ⚖️ Copyright & Licensing

**NIV Bible Copyright:** © 1973, 1978, 1984, 2011 by Biblica, Inc.®

**This API:** Provides reference links only. No copyrighted text is reproduced.

**Biblica License:** For commercial use or special licensing needs, contact Biblica directly at https://www.biblica.com/

**Fair Use:** This reference API is designed to comply with fair use principles by providing metadata and links without reproducing copyrighted content.

## 📝 Data Format

All endpoints return valid JSON with the following characteristics:

- **Content-Type:** `application/json`
- **Encoding:** UTF-8
- **Formatting:** Indented for readability
- **CORS:** Enabled for cross-origin requests

## 🔄 Related APIs

- **KJV Bible API** - Full text of King James Version (public domain)
- **Bible Sync Player** - Audio-to-text synchronization with highlighting
- **KJV Text Endpoints** - Complete KJV Bible text with metadata

## 🚀 Getting Started

1. **Choose an endpoint** based on your needs (all books, testament, or individual book)
2. **Fetch the reference data** using your preferred HTTP client
3. **Extract the official source links** from the response
4. **Direct users to official sources** for reading the actual Bible text
5. **Consider using official APIs** if you need programmatic access to Bible content

## 📞 Support & Questions

For questions about this reference API, please open an issue on the GitHub repository.

For questions about NIV Bible licensing or usage, contact Biblica at https://www.biblica.com/

## 📄 License

- **Reference API:** MIT License
- **NIV Bible Text:** Copyright by Biblica, Inc. (not included in this API)
- **Official Sources:** See respective websites for terms of use

---

**Last Updated:** May 2026  
**Total Endpoints:** 69 JSON files  
**Status:** Active and maintained  
**Copyright Notice:** This API respects all copyright and licensing requirements
