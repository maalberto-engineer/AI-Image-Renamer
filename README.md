# AI Image Renamer

A simple Python tool that uses a local vision model through Ollama to automatically generate descriptive filenames for images.

The script scans a folder, analyzes each supported image, generates a short descriptive filename, and renames the file automatically.

## Why I Built This

I created this project because I had a large collection of reference images with generic filenames such as `Pinterest Image (1).jpg`, `Pinterest Image (2).png`, and so on.

Manually opening and renaming every image would have been repetitive and time-consuming, especially when working with dozens or hundreds of files. I wanted a faster way to organize the collection based on what was actually shown in each image.

That led me to experiment with a local vision model through Ollama. The goal was to create a simple tool that could look at each image, generate a short descriptive filename, and rename the files automatically.

What started as a small personal automation task became a useful way to explore Python file handling, local AI models, image analysis, and workflow automation.

## Features

- Automatically analyzes images using a local AI vision model
- Generates short descriptive filenames
- Supports:
  - `.jpg`
  - `.jpeg`
  - `.png`
  - `.webp`
- Automatically handles duplicate filenames
- Runs locally through Ollama
- Does not require uploading images to a cloud service
- Works with any folder selected by the user

## Example

Before:

`
Pinterest Image (1).jpg
Pinterest Image (2).jpg
Pinterest Image (3).png
`

After:

`pixel_art_gothic_lady.jpg
dark_knight_with_sword.jpg
cherry_blossom_temple.png
`

## Requirements

You will need:

- Python 3
- Ollama
- A compatible Ollama vision model

This project currently uses:

`
qwen2.5vl
`

## Installation

### 1. Install Ollama

Download and install Ollama from:

https://ollama.com

After installing Ollama, confirm that it works:

```bash
ollama --version
```

### 2. Download the Vision Model

Run:

```bash
ollama pull qwen2.5vl
```

You can test the model with:

```bash
ollama run qwen2.5vl
```

### 3. Install Python Dependencies

Clone or download this repository.

Then install the required Python package:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file currently contains:

```text
ollama
```

## Usage

Run the script with:

```bash
python rename_images.py
```

The program will ask for the full path to the folder containing your images.

Example:

```text
Enter the full path to the image folder:
C:\Users\YourName\Pictures\Images
```

The script will then analyze each supported image and rename it.

Example output:

```text
Analyzing: image_001.jpg
  -> dark_knight_with_sword.jpg

Analyzing: image_002.png
  -> cherry_blossom_temple.png
```

## How It Works

The script:

1. Reads the images inside the selected folder.
2. Sends each image to the local Ollama vision model.
3. Asks the model to generate a short descriptive filename.
4. Cleans the generated text so it can safely be used as a filename.
5. Preserves the original file extension.
6. Checks for duplicate filenames.
7. Renames the image.

If a generated filename already exists, the script automatically adds a number.

Example:

```text
dark_knight.jpg
dark_knight_2.jpg
dark_knight_3.jpg
```

## Privacy

Image processing is performed locally through Ollama.

Images do not need to be uploaded to an external AI service for the renaming process.

## Important Notes

The AI-generated filenames are based on the model's interpretation of each image and may not always be completely accurate.

It is recommended to review renamed files after processing, especially when working with important image collections.

Consider testing the script on a copied folder before using it on important files.

## Project Structure

```text
AI-Image-Renamer/
│
├── rename_images.py
├── requirements.txt
├── README.md
└── .gitignore
```

## AI Assistance

This project was developed with the assistance of AI tools for code generation, troubleshooting, and refinement.

The implementation was configured, tested, debugged, and modified for the intended use case.

## Disclaimer

This project only renames files that already exist on the user's computer.

Users are responsible for ensuring that they have the appropriate rights or permissions for any images they process, distribute, or publish.

## Future Improvements

Possible future improvements include:

- Preview filenames before applying changes
- Add a graphical folder picker
- Add a graphical user interface
- Allow users to choose naming styles
- Add configurable filename length
- Add undo functionality
- Add support for additional image formats
- Add custom prompts for different types of image collections

## License

This project is intended for personal and educational use.

If you plan to distribute or expand the project, consider adding an open-source license such as the MIT License.
