import json
import os

# Load data
with open('bible_audio.json', 'r') as f:
    audio_data = json.load(f)

with open('../farskipper-kjv/json/verses-1769.json', 'r') as f:
    verses_data = json.load(f)

def calculate_book_stats(book_name):
    """Calculate statistics for a book."""
    verses_in_book = {k: v for k, v in verses_data.items() if k.startswith(f"{book_name} ")}
    
    total_verses = len(verses_in_book)
    total_characters = sum(len(text) for text in verses_in_book.values())
    total_words = sum(len(text.split()) for text in verses_in_book.values())
    
    chapters = set()
    for key in verses_in_book.keys():
        parts = key.split(':')
        if len(parts) >= 1:
            chapter_part = parts[0].split()[-1]
            try:
                chapters.add(int(chapter_part))
            except:
                pass
    
    return {
        'verses': total_verses,
        'characters': total_characters,
        'words': total_words,
        'chapters': len(chapters)
    }

def get_book_text(book_name):
    """Get all text for a book organized by chapter and verse."""
    verses_in_book = {k: v for k, v in verses_data.items() if k.startswith(f"{book_name} ")}
    
    chapters_dict = {}
    for verse_key, verse_text in verses_in_book.items():
        parts = verse_key.split(':')
        if len(parts) == 2:
            chapter_str = parts[0].split()[-1]
            verse_str = parts[1]
            try:
                chapter_num = int(chapter_str)
                verse_num = int(verse_str)
                
                if chapter_num not in chapters_dict:
                    chapters_dict[chapter_num] = {}
                
                chapters_dict[chapter_num][verse_num] = verse_text
            except:
                pass
    
    return chapters_dict

# Create directories
os.makedirs('api/v1/text', exist_ok=True)
os.makedirs('api/v1/text/ot', exist_ok=True)
os.makedirs('api/v1/text/nt', exist_ok=True)
os.makedirs('api/v1/metadata', exist_ok=True)

# Generate metadata
metadata = {
    'old_testament': [],
    'new_testament': [],
    'summary': {}
}

ot_total_verses = 0
ot_total_chars = 0
ot_total_words = 0

for book_data in audio_data['old_testament']:
    book_name = book_data['book']
    stats = calculate_book_stats(book_name)
    
    metadata['old_testament'].append({
        'book': book_name,
        'book_number': book_data['book_number'],
        'chapters': book_data['total_chapters'],
        'verses': stats['verses'],
        'characters': stats['characters'],
        'words': stats['words'],
        'text_endpoint': f"/api/v1/text/ot/{book_name.lower().replace(' ', '_')}.json",
        'audio_url_pattern': f"https://kjv-bible-audio-cdn.netlify.app/ot/{str(book_data['book_number']).zfill(2)}_{book_name.replace(' ', '_')}_{{chapter}}.mp3"
    })
    
    ot_total_verses += stats['verses']
    ot_total_chars += stats['characters']
    ot_total_words += stats['words']

nt_total_verses = 0
nt_total_chars = 0
nt_total_words = 0

for book_data in audio_data['new_testament']:
    book_name = book_data['book']
    stats = calculate_book_stats(book_name)
    
    metadata['new_testament'].append({
        'book': book_name,
        'book_number': book_data['book_number'],
        'chapters': book_data['total_chapters'],
        'verses': stats['verses'],
        'characters': stats['characters'],
        'words': stats['words'],
        'text_endpoint': f"/api/v1/text/nt/{book_name.lower().replace(' ', '_')}.json",
        'audio_url_pattern': f"https://kjv-bible-audio-cdn.netlify.app/nt/{str(book_data['book_number'] - 39).zfill(2)}_{book_name.replace(' ', '_')}_{{chapter}}.mp3"
    })
    
    nt_total_verses += stats['verses']
    nt_total_chars += stats['characters']
    nt_total_words += stats['words']

metadata['summary'] = {
    'total_books': 66,
    'old_testament': {
        'books': 39,
        'verses': ot_total_verses,
        'characters': ot_total_chars,
        'words': ot_total_words
    },
    'new_testament': {
        'books': 27,
        'verses': nt_total_verses,
        'characters': nt_total_chars,
        'words': nt_total_words
    },
    'total': {
        'verses': ot_total_verses + nt_total_verses,
        'characters': ot_total_chars + nt_total_chars,
        'words': ot_total_words + nt_total_words
    }
}

# Save metadata endpoints
with open('api/v1/metadata/all.json', 'w') as f:
    json.dump(metadata, f, indent=2)

with open('api/v1/metadata/ot.json', 'w') as f:
    json.dump({'books': metadata['old_testament'], 'summary': metadata['summary']['old_testament']}, f, indent=2)

with open('api/v1/metadata/nt.json', 'w') as f:
    json.dump({'books': metadata['new_testament'], 'summary': metadata['summary']['new_testament']}, f, indent=2)

# Generate text endpoints for each book
for book_data in audio_data['old_testament']:
    book_name = book_data['book']
    book_text = get_book_text(book_name)
    
    text_data = {
        'book': book_name,
        'book_number': book_data['book_number'],
        'chapters': {}
    }
    
    for chapter_num in sorted(book_text.keys()):
        verses = book_text[chapter_num]
        text_data['chapters'][str(chapter_num)] = {
            'chapter': chapter_num,
            'verses': verses,
            'verse_count': len(verses)
        }
    
    book_file = book_name.lower().replace(' ', '_')
    with open(f'api/v1/text/ot/{book_file}.json', 'w') as f:
        json.dump(text_data, f, indent=2)

for book_data in audio_data['new_testament']:
    book_name = book_data['book']
    book_text = get_book_text(book_name)
    
    text_data = {
        'book': book_name,
        'book_number': book_data['book_number'],
        'chapters': {}
    }
    
    for chapter_num in sorted(book_text.keys()):
        verses = book_text[chapter_num]
        text_data['chapters'][str(chapter_num)] = {
            'chapter': chapter_num,
            'verses': verses,
            'verse_count': len(verses)
        }
    
    book_file = book_name.lower().replace(' ', '_')
    with open(f'api/v1/text/nt/{book_file}.json', 'w') as f:
        json.dump(text_data, f, indent=2)

# Generate complete OT and NT text files
ot_complete = {'testament': 'Old Testament', 'books': []}
for book_data in audio_data['old_testament']:
    book_name = book_data['book']
    book_file = book_name.lower().replace(' ', '_')
    with open(f'api/v1/text/ot/{book_file}.json', 'r') as f:
        ot_complete['books'].append(json.load(f))

with open('api/v1/text/ot.json', 'w') as f:
    json.dump(ot_complete, f, indent=2)

nt_complete = {'testament': 'New Testament', 'books': []}
for book_data in audio_data['new_testament']:
    book_name = book_data['book']
    book_file = book_name.lower().replace(' ', '_')
    with open(f'api/v1/text/nt/{book_file}.json', 'r') as f:
        nt_complete['books'].append(json.load(f))

with open('api/v1/text/nt.json', 'w') as f:
    json.dump(nt_complete, f, indent=2)

print("Text and metadata endpoints generated successfully!")
print(f"  - Old Testament: {len(metadata['old_testament'])} books")
print(f"  - New Testament: {len(metadata['new_testament'])} books")
print(f"  - Total verses: {metadata['summary']['total']['verses']}")
print(f"  - Total characters: {metadata['summary']['total']['characters']}")
print(f"  - Total words: {metadata['summary']['total']['words']}")
