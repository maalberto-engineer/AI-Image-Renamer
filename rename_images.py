import ollama
import os
import re

FOLDER = input("Enter the full path to the image folder: ").strip('"')

extensions = (".jpg", ".jpeg", ".png", ".webp")

def clean_filename(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")[:60]


for filename in os.listdir(FOLDER):

    if not filename.lower().endswith(extensions):
        continue

    path = os.path.join(FOLDER, filename)

    print(f"Analyzing: {filename}")

    response = ollama.chat(
        model="qwen2.5vl",
        messages=[
            {
                "role": "user",
                "content": """
Create a short descriptive filename for this image.

Rules:
- 3 to 6 words
- lowercase
- describe the main subject
- mention important objects, clothing, pose, or environment when useful
- no filler words
- no file extension
- output ONLY the filename
""",
                "images": [path]
            }
        ]
    )

    description = response["message"]["content"]
    new_base = clean_filename(description)

    extension = os.path.splitext(filename)[1].lower()
    new_filename = new_base + extension
    new_path = os.path.join(FOLDER, new_filename)

    counter = 2

    while os.path.exists(new_path):
        new_filename = f"{new_base}_{counter}{extension}"
        new_path = os.path.join(FOLDER, new_filename)
        counter += 1

    os.rename(path, new_path)

    print(f"  -> {new_filename}")