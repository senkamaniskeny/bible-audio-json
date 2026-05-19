import json
import os

def generate_api():
    with open('bible_audio.json', 'r') as f:
        data = json.load(f)

    # Create api/v1 directory
    os.makedirs('api/v1', exist_ok=True)

    # 1. Full data endpoint
    with open('api/v1/all.json', 'w') as f:
        json.dump(data, f, indent=2)

    # 2. Old Testament endpoint
    with open('api/v1/ot.json', 'w') as f:
        json.dump(data.get('old_testament', []), f, indent=2)

    # 3. New Testament endpoint
    with open('api/v1/nt.json', 'w') as f:
        json.dump(data.get('new_testament', []), f, indent=2)

    # 4. Individual books (optional but good for "API" feel)
    os.makedirs('api/v1/books', exist_ok=True)
    for section in ['old_testament', 'new_testament']:
        for book_data in data.get(section, []):
            book_name = book_data['book'].lower().replace(' ', '_')
            with open(f'api/v1/books/{book_name}.json', 'w') as f:
                json.dump(book_data, f, indent=2)

    print("API endpoints generated successfully.")

if __name__ == "__main__":
    generate_api()
