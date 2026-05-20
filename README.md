# Bible Audio JSON API

A comprehensive static JSON API for the King James Version (KJV) Bible Audio Narration with synchronized text data. This repository hosts the complete Bible with audio CDN metadata and full text synchronization, deployed via GitHub Pages.

## 🚀 Base URL

The API is hosted on GitHub Pages. Use the following base URL for all requests:

```text
https://senkamaniskeny.github.io/bible-audio-json/
```

## 📂 API Endpoints

### Audio-Only Endpoints

#### 1. Complete Bible Data
Returns the entire collection including both Old and New Testaments with audio URLs.
- **Endpoint:** `/api/v1/all.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/all.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/all.json)

#### 2. Old Testament (Audio Only)
Returns only the books and audio links for the Old Testament.
- **Endpoint:** `/api/v1/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/ot.json)

#### 3. New Testament (Audio Only)
Returns only the books and audio links for the New Testament.
- **Endpoint:** `/api/v1/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/nt.json)

#### 4. Individual Books (Audio Only)
You can fetch data for a specific book by using its name (lowercase, spaces replaced with underscores).
- **Endpoint:** `/api/v1/books/{book_name}.json`
- **Example (Genesis):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json)
- **Example (John):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/john.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/john.json)

### Synchronized Text & Audio Endpoints

These endpoints include both audio URLs and complete text data with sentence and word-level segmentation for precise synchronization.

#### 5. Complete Synchronized Bible
- **Endpoint:** `/api/v1/sync/ot.json` (Old Testament)
- **Endpoint:** `/api/v1/sync/nt.json` (New Testament)
- **URL (OT):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot.json)
- **URL (NT):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt.json)

#### 6. Individual Synchronized Books
- **Endpoint (OT):** `/api/v1/sync/ot/{book_name}.json`
- **Endpoint (NT):** `/api/v1/sync/nt/{book_name}.json`
- **Example (Genesis):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot/genesis.json)
- **Example (Matthew):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/matthew.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/matthew.json)

## 📊 Data Structure

### Audio-Only Format
```json
{
  "book": "Genesis",
  "book_number": 1,
  "total_chapters": 50,
  "chapters": [
    {
      "chapter": 1,
      "audio_url": "https://kjv-bible-audio-cdn.netlify.app/ot/01_Genesis_01.mp3"
    }
  ]
}
```

### Synchronized Format
Each synchronized chapter contains verses with text segmentation:

```json
{
  "book": "Genesis",
  "chapter": 1,
  "audio_url": "https://kjv-bible-audio-cdn.netlify.app/ot/01_Genesis_01.mp3",
  "verses": [
    {
      "verse": 1,
      "text": "In the beginning God created the heaven and the earth.",
      "sentences": [
        "In the beginning God created the heaven and the earth."
      ],
      "words": [
        "In", "the", "beginning", "God", "created", "the", "heaven", "and", "the", "earth."
      ]
    }
  ],
  "verse_count": 31
}
```

## 🛠 Usage Examples

### JavaScript - Fetch Synchronized Data
```javascript
// Fetch Genesis chapter 1 with synchronized text and audio
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot/genesis.json')
  .then(response => response.json())
  .then(data => {
    const chapter1 = data.chapters[0];
    console.log('Chapter:', chapter1.chapter);
    console.log('Audio URL:', chapter1.audio_url);
    console.log('Verses:', chapter1.verses);
  });
```

### JavaScript - Fetch Old Testament
```javascript
// Fetch all Old Testament books with synchronization
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/ot.json')
  .then(response => response.json())
  .then(books => {
    console.log('Total OT books:', books.length);
    books.forEach(book => {
      console.log(`${book.book}: ${book.total_chapters} chapters`);
    });
  });
```

### Python - Process Synchronized Data
```python
import json
import requests

# Fetch John chapter 3 with word-level synchronization
url = 'https://senkamaniskeny.github.io/bible-audio-json/api/v1/sync/nt/john.json'
response = requests.get(url)
data = response.json()

chapter3 = data['chapters'][2]  # Chapter 3
for verse in chapter3['verses']:
    print(f"Verse {verse['verse']}: {verse['text']}")
    print(f"  Words: {verse['words']}")
    print(f"  Sentences: {verse['sentences']}")
```

## 🎯 Use Cases

- **Audio Bible Players**: Build applications that play Bible audio with real-time text highlighting
- **Bible Study Tools**: Create study applications with synchronized text and audio
- **Accessibility**: Provide text alternatives for audio content
- **Language Learning**: Use the structured word and sentence data for learning applications
- **Research**: Analyze text patterns with pre-segmented sentences and words

## 📜 Source Information
- **Text Source:** farskipper/kjv repository (King James Version)
- **Audio Source:** audiotreasure.com
- **Version:** King James Version (KJV) - 1769 Edition
- **Audio CDN:** Netlify
- **Total Books:** 66 (39 Old Testament, 27 New Testament)
- **Total Verses:** 31,102

## 🔄 Synchronization Strategy

The synchronized endpoints use a linear time-mapping approach:
- Each chapter's audio duration is divided equally among all verses
- Verses are further subdivided into sentences and words
- As audio plays, the current position is mapped to the corresponding verse, sentence, or word
- This enables both sentence-level and word-level highlighting during playback

## 📝 Notes

- Text data has been processed to remove formatting markers (`#` for paragraphs, `[]` for italics)
- Words are extracted by splitting on whitespace
- Sentences are extracted by splitting on sentence terminators (`.`, `!`, `?`)
- Audio URLs point to Netlify CDN and are pre-generated based on book and chapter numbers
