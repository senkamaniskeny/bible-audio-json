# Bible Audio JSON API

A comprehensive static JSON API for the King James Version (KJV) Bible with complete text data, audio URLs, and detailed metadata. This repository provides multiple endpoints for accessing Bible text, audio information, and statistical metadata, all deployed via GitHub Pages.

## 🚀 Base URL

```text
https://senkamaniskeny.github.io/bible-audio-json/
```

## 📊 Quick Statistics

| Metric | Count |
|--------|-------|
| **Total Books** | 66 (39 OT + 27 NT) |
| **Total Verses** | 30,985 |
| **Total Characters** | 4,142,381 |
| **Total Words** | 789,891 |

---

## 📂 API Endpoints

### 1. Metadata Endpoints

Retrieve comprehensive metadata about books including verse counts, character counts, and word counts.

#### All Books Metadata
- **Endpoint:** `/api/v1/metadata/all.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/all.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/all.json)
- **Description:** Complete metadata for all 66 books with summary statistics

#### Old Testament Metadata
- **Endpoint:** `/api/v1/metadata/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/ot.json)
- **Description:** Metadata for all 39 Old Testament books with OT summary

#### New Testament Metadata
- **Endpoint:** `/api/v1/metadata/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/nt.json)
- **Description:** Metadata for all 27 New Testament books with NT summary

**Metadata Structure:**
```json
{
  "book": "Genesis",
  "book_number": 1,
  "chapters": 50,
  "verses": 1533,
  "characters": 197803,
  "words": 38452,
  "text_endpoint": "/api/v1/text/ot/genesis.json",
  "audio_url_pattern": "https://kjv-bible-audio-cdn.netlify.app/ot/01_Genesis_{chapter}.mp3"
}
```

---

### 2. Text-Only Endpoints

Access the complete KJV Bible text organized by book and chapter.

#### Complete Old Testament Text
- **Endpoint:** `/api/v1/text/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot.json)
- **Description:** All 39 Old Testament books with complete text

#### Complete New Testament Text
- **Endpoint:** `/api/v1/text/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/nt.json)
- **Description:** All 27 New Testament books with complete text

#### Individual Book Text (Old Testament)
- **Endpoint:** `/api/v1/text/ot/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot/genesis.json)
- **Available Books:** genesis, exodus, leviticus, numbers, deuteronomy, joshua, judges, ruth, 1_samuel, 2_samuel, 1_kings, 2_kings, 1_chronicles, 2_chronicles, ezra, nehemiah, esther, job, psalms, proverbs, ecclesiastes, song_of_solomon, isaiah, jeremiah, lamentations, ezekiel, daniel, hosea, joel, amos, obadiah, jonah, micah, nahum, habakkuk, zephaniah, haggai, zechariah, malachi

#### Individual Book Text (New Testament)
- **Endpoint:** `/api/v1/text/nt/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/nt/matthew.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/nt/matthew.json)
- **Available Books:** matthew, mark, luke, john, acts, romans, 1_corinthians, 2_corinthians, galatians, ephesians, philippians, colossians, 1_thessalonians, 2_thessalonians, 1_timothy, 2_timothy, titus, philemon, hebrews, james, 1_peter, 2_peter, 1_john, 2_john, 3_john, jude, revelation

**Text Structure:**
```json
{
  "book": "Genesis",
  "book_number": 1,
  "chapters": {
    "1": {
      "chapter": 1,
      "verses": {
        "1": "In the beginning God created the heaven and the earth.",
        "2": "And the earth was without form, and void..."
      },
      "verse_count": 31
    }
  }
}
```

---

### 3. Audio Endpoints

Access audio URLs and chapter information.

#### Complete Audio Data
- **Endpoint:** `/api/v1/all.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/all.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/all.json)
- **Description:** All books with audio URLs for each chapter

#### Old Testament Audio
- **Endpoint:** `/api/v1/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/ot.json)
- **Description:** All 39 Old Testament books with audio URLs

#### New Testament Audio
- **Endpoint:** `/api/v1/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/nt.json)
- **Description:** All 27 New Testament books with audio URLs

#### Individual Book Audio
- **Endpoint:** `/api/v1/books/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json)

---

### 4. Synchronized Audio-Text Endpoints

Real-time synchronization with sentence and word-level highlighting.

#### Complete Synchronized Old Testament
- **Endpoint:** `/api/v1/sync/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot.json)
- **Description:** All OT books with audio URLs and text segmentation

#### Complete Synchronized New Testament
- **Endpoint:** `/api/v1/sync/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt.json)
- **Description:** All NT books with audio URLs and text segmentation

#### Individual Synchronized Books (Old Testament)
- **Endpoint:** `/api/v1/sync/ot/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot/genesis.json)

#### Individual Synchronized Books (New Testament)
- **Endpoint:** `/api/v1/sync/nt/{book_name}.json`
- **Example:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/matthew.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/matthew.json)

**Synchronized Structure:**
```json
{
  "book": "Genesis",
  "chapter": 1,
  "audio_url": "https://kjv-bible-audio-cdn.netlify.app/ot/01_Genesis_01.mp3",
  "verses": [
    {
      "verse": 1,
      "text": "In the beginning God created the heaven and the earth.",
      "sentences": ["In the beginning God created the heaven and the earth."],
      "words": ["In", "the", "beginning", "God", "created", "the", "heaven", "and", "the", "earth."]
    }
  ],
  "verse_count": 31
}
```

---

## 🛠 Usage Examples

### JavaScript - Fetch Metadata
```javascript
// Get all books metadata
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/all.json')
  .then(response => response.json())
  .then(data => {
    console.log('Total books:', data.summary.total_books);
    console.log('Total verses:', data.summary.total.verses);
    console.log('Total characters:', data.summary.total.characters);
  });
```

### JavaScript - Fetch Book Text
```javascript
// Get Genesis text
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot/genesis.json')
  .then(response => response.json())
  .then(data => {
    const chapter1 = data.chapters['1'];
    console.log('Genesis Chapter 1:');
    Object.entries(chapter1.verses).forEach(([verse, text]) => {
      console.log(`${verse}: ${text}`);
    });
  });
```

### JavaScript - Fetch Synchronized Data
```javascript
// Get Matthew with synchronization
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/matthew.json')
  .then(response => response.json())
  .then(data => {
    const chapter1 = data.chapters[0];
    console.log('Audio URL:', chapter1.audio_url);
    chapter1.verses.forEach(verse => {
      console.log(`Verse ${verse.verse}:`, verse.text);
      console.log('  Sentences:', verse.sentences);
      console.log('  Words:', verse.words);
    });
  });
```

### Python - Process Bible Data
```python
import json
import requests

# Fetch Old Testament metadata
url = 'https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/ot.json'
response = requests.get(url)
data = response.json()

print(f"Old Testament Summary:")
print(f"  Books: {data['summary']['books']}")
print(f"  Verses: {data['summary']['verses']}")
print(f"  Characters: {data['summary']['characters']}")
print(f"  Words: {data['summary']['words']}")

# List all OT books
for book in data['books']:
    print(f"\n{book['book']} ({book['chapters']} chapters)")
    print(f"  Verses: {book['verses']}")
    print(f"  Characters: {book['characters']}")
    print(f"  Words: {book['words']}")
```

### cURL - Fetch Data
```bash
# Get all metadata
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/all.json | jq '.summary'

# Get Genesis text
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot/genesis.json | jq '.chapters["1"].verses["1"]'

# Get Matthew with synchronization
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/matthew.json | jq '.chapters[0].verses[0]'
```

---

## 📋 Complete Book List

### Old Testament (39 books)

**Pentateuch:** Genesis, Exodus, Leviticus, Numbers, Deuteronomy

**Historical Books:** Joshua, Judges, Ruth, 1 Samuel, 2 Samuel, 1 Kings, 2 Kings, 1 Chronicles, 2 Chronicles, Ezra, Nehemiah, Esther

**Wisdom Literature:** Job, Psalms, Proverbs, Ecclesiastes, Song of Solomon

**Major Prophets:** Isaiah, Jeremiah, Lamentations, Ezekiel, Daniel

**Minor Prophets:** Hosea, Joel, Amos, Obadiah, Jonah, Micah, Nahum, Habakkuk, Zephaniah, Haggai, Zechariah, Malachi

### New Testament (27 books)

**Gospels:** Matthew, Mark, Luke, John

**Acts:** Acts

**Paul's Epistles:** Romans, 1 Corinthians, 2 Corinthians, Galatians, Ephesians, Philippians, Colossians, 1 Thessalonians, 2 Thessalonians, 1 Timothy, 2 Timothy, Titus, Philemon

**Hebrews:** Hebrews

**James:** James

**Peter's Epistles:** 1 Peter, 2 Peter

**John's Epistles:** 1 John, 2 John, 3 John

**Jude:** Jude

**Revelation:** Revelation

---

## 🎯 Use Cases

- **Bible Study Applications:** Build apps with searchable text and audio playback
- **Language Learning:** Use structured text data for language studies
- **Accessibility:** Provide text alternatives for audio content
- **Research:** Analyze Bible text patterns and statistics
- **Audio Players:** Create synchronized audio-text players with highlighting
- **Mobile Apps:** Develop offline-capable Bible applications
- **Web Services:** Integrate Bible data into websites and services

---

## 📊 Data Statistics by Testament

### Old Testament
- **Books:** 39
- **Verses:** 23,145
- **Characters:** 3,116,480
- **Words:** 592,439

### New Testament
- **Books:** 27
- **Verses:** 7,840
- **Characters:** 1,025,901
- **Words:** 197,452

---

## 🔄 Data Format Notes

- **Text Encoding:** UTF-8
- **Verse Keys:** Format is `"Book Chapter:Verse"` (e.g., `"Genesis 1:1"`)
- **Sentence Segmentation:** Split by periods, exclamation marks, and question marks
- **Word Segmentation:** Split by whitespace
- **Formatting Markers Removed:** Paragraph markers (`#`) and italic markers (`[]`) have been removed for clean text
- **Audio URLs:** Point to Netlify CDN with pattern `{testament}/{number}_{book}_{chapter}.mp3`

---

## 📜 Source Information

- **Text Source:** farskipper/kjv repository (King James Version 1769)
- **Audio Source:** audiotreasure.com
- **Version:** King James Version (KJV)
- **Edition:** 1769 Edition
- **Audio CDN:** Netlify
- **Text License:** Public Domain
- **Audio License:** Check audiotreasure.com for licensing information

---

## 🚀 Getting Started

### 1. Fetch Metadata First
Start by getting the metadata to understand available books and statistics:
```bash
curl https://senkamaniskeny.github.io/bible-audio-json/api/v1/metadata/all.json
```

### 2. Choose Your Endpoint
Select the appropriate endpoint based on your needs:
- **Text Only:** Use `/api/v1/text/` endpoints
- **Audio Only:** Use `/api/v1/` endpoints
- **Synchronized:** Use `/api/v1/sync/` endpoints
- **Metadata:** Use `/api/v1/metadata/` endpoints

### 3. Access Individual Books
Use the book name (lowercase, spaces as underscores) to access specific books:
```bash
# Old Testament example
https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/ot/genesis.json

# New Testament example
https://senkamaniskeny.github.io/bible-audio-json/api/v1/text/nt/matthew.json
```

### 4. Parse and Use
Process the JSON data in your application for display, search, or analysis.

---

## ✨ Features

✅ Complete KJV Bible text (30,985 verses)  
✅ Audio URLs for all chapters  
✅ Detailed metadata with statistics  
✅ Sentence and word-level segmentation  
✅ Organized by book and chapter  
✅ Static JSON API (no server required)  
✅ GitHub Pages hosted (always available)  
✅ Multiple endpoint options  
✅ Zero authentication required  
✅ CORS-enabled for web applications  

---

## 📝 API Response Format

All endpoints return valid JSON with the following characteristics:

- **Content-Type:** `application/json`
- **Encoding:** UTF-8
- **Formatting:** Indented for readability
- **CORS:** Enabled for cross-origin requests

---

## 🔗 Related Resources

- [GitHub Repository](https://github.com/senkamaniskeny/bible-audio-json)
- [Bible Sync Player](https://github.com/senkamaniskeny/bible-sync-player) - Interactive player with highlighting
- [farskipper/kjv](https://github.com/farskipper/kjv) - Original KJV text source
- [audiotreasure.com](https://audiotreasure.com) - Audio source

---

## 📄 License

- **Text:** Public Domain (King James Version)
- **Data Structure:** MIT License
- **Audio:** See audiotreasure.com for licensing

---

## 🤝 Contributing

To contribute improvements, corrections, or additional endpoints:

1. Fork the repository
2. Make your changes
3. Submit a pull request

---

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Last Updated:** May 2026  
**Total Endpoints:** 20+  
**Data Freshness:** Real-time (generated from source data)
