# Bible Audio JSON API

A static JSON API for the King James Version (KJV) Bible Audio Narration. This repository hosts the audio CDN metadata in a structured format, deployed via GitHub Pages.

## 🚀 Base URL

The API is hosted on GitHub Pages. Use the following base URL for all requests:

```text
https://senkamaniskeny.github.io/bible-audio-json/
```

## 📂 API Endpoints

### 1. Complete Bible Data
Returns the entire collection including both Old and New Testaments.
- **Endpoint:** `/api/v1/all.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/all.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/all.json)

### 2. Old Testament
Returns only the books and audio links for the Old Testament.
- **Endpoint:** `/api/v1/ot.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/ot.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/ot.json)

### 3. New Testament
Returns only the books and audio links for the New Testament.
- **Endpoint:** `/api/v1/nt.json`
- **URL:** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/nt.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/nt.json)

### 4. Individual Books
You can fetch data for a specific book by using its name (lowercase, spaces replaced with underscores).
- **Endpoint:** `/api/v1/books/{book_name}.json`
- **Example (Genesis):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json)
- **Example (John):** [https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/john.json](https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/john.json)

## 📊 Data Structure

Each book entry contains:
- `book`: Name of the book
- `book_number`: Canonical order
- `total_chapters`: Number of chapters
- `chapters`: Array of objects containing:
    - `chapter`: Chapter number
    - `audio_url`: Direct link to the MP3 file

## 🛠 Usage Example (JavaScript)

```javascript
fetch('https://senkamaniskeny.github.io/bible-audio-json/api/v1/books/genesis.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 📜 Source Information
- **Source:** audiotreasure.com
- **Version:** King James Version (KJV)
- **CDN:** Netlify (Audio files hosted on Netlify)
