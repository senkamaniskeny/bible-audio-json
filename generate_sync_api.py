import json
import os
import re

# Load audio data
with open('bible_audio.json', 'r') as f:
    audio_data = json.load(f)

# Load text data
with open('../farskipper-kjv/json/verses-1769.json', 'r') as f:
    verses_data = json.load(f)

def split_into_sentences(text):
    """Split text into sentences."""
    # Remove paragraph markers and italic markers
    text = text.replace('# ', '').replace('[', '').replace(']', '')
    # Split by periods, exclamation marks, and question marks
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return [s.strip() for s in sentences if s.strip()]

def split_into_words(text):
    """Split text into words."""
    text = text.replace('# ', '').replace('[', '').replace(']', '')
    words = text.split()
    return [w.strip() for w in words if w.strip()]

def create_sync_chapter(book_name, chapter_num, audio_url, verses_dict):
    """Create a synchronized chapter object."""
    verses_in_chapter = []
    
    for verse_num in range(1, 200):  # Arbitrary high number
        verse_key = f"{book_name} {chapter_num}:{verse_num}"
        if verse_key not in verses_dict:
            break
        
        verse_text = verses_dict[verse_key]
        sentences = split_into_sentences(verse_text)
        words = split_into_words(verse_text)
        
        verses_in_chapter.append({
            "verse": verse_num,
            "text": verse_text,
            "sentences": sentences,
            "words": words
        })
    
    return {
        "book": book_name,
        "chapter": chapter_num,
        "audio_url": audio_url,
        "verses": verses_in_chapter,
        "verse_count": len(verses_in_chapter)
    }

# Create directories
os.makedirs('api/v1/sync', exist_ok=True)
os.makedirs('api/v1/sync/ot', exist_ok=True)
os.makedirs('api/v1/sync/nt', exist_ok=True)

# Generate Old Testament sync data
ot_sync = []
for book_data in audio_data['old_testament']:
    book_name = book_data['book']
    book_sync = {
        "book": book_name,
        "book_number": book_data['book_number'],
        "total_chapters": book_data['total_chapters'],
        "chapters": []
    }
    
    for chapter_data in book_data['chapters']:
        chapter_num = chapter_data['chapter']
        audio_url = chapter_data['audio_url']
        
        sync_chapter = create_sync_chapter(book_name, chapter_num, audio_url, verses_data)
        book_sync['chapters'].append(sync_chapter)
    
    ot_sync.append(book_sync)

# Generate New Testament sync data
nt_sync = []
for book_data in audio_data['new_testament']:
    book_name = book_data['book']
    book_sync = {
        "book": book_name,
        "book_number": book_data['book_number'],
        "total_chapters": book_data['total_chapters'],
        "chapters": []
    }
    
    for chapter_data in book_data['chapters']:
        chapter_num = chapter_data['chapter']
        audio_url = chapter_data['audio_url']
        
        sync_chapter = create_sync_chapter(book_name, chapter_num, audio_url, verses_data)
        book_sync['chapters'].append(sync_chapter)
    
    nt_sync.append(book_sync)

# Save OT sync data
with open('api/v1/sync/ot.json', 'w') as f:
    json.dump(ot_sync, f, indent=2)

# Save NT sync data
with open('api/v1/sync/nt.json', 'w') as f:
    json.dump(nt_sync, f, indent=2)

# Save individual book sync data
for book_data in ot_sync:
    book_name = book_data['book'].lower().replace(' ', '_')
    with open(f'api/v1/sync/ot/{book_name}.json', 'w') as f:
        json.dump(book_data, f, indent=2)

for book_data in nt_sync:
    book_name = book_data['book'].lower().replace(' ', '_')
    with open(f'api/v1/sync/nt/{book_name}.json', 'w') as f:
        json.dump(book_data, f, indent=2)

print("Synchronized API endpoints generated successfully!")
print(f"  - Old Testament: {len(ot_sync)} books")
print(f"  - New Testament: {len(nt_sync)} books")
