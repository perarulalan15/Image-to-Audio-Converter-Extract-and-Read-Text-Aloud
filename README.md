# Image to Speech: Extract Text from Images and Convert to Voice

## 📌 Project Description

This project extracts text from an image using Optical Character Recognition (OCR) and converts the extracted text into speech using Text-to-Speech (TTS) technology. It leverages the **Qwen/Qwen2-VL-2B-Instruct** model for enhanced vision-language understanding, ensuring accurate text extraction from complex images. This can be useful for visually impaired individuals, language learners, or situations where reading text manually is inconvenient.


## 🛠️ Features
- Uses **Qwen/Qwen2-VL-2B-Instruct** for high-accuracy text extraction.
- Converts extracted text to speech using a text-to-speech engine.
- Supports multiple image formats (JPG, PNG, etc.).
- Outputs audio in a clear and natural voice.

## ⚡ Technologies Used
- **Python**
- **Qwen/Qwen2-VL-2B-Instruct** (for vision-language understanding)
- **Tesseract OCR** (for text extraction)
- **gTTS (Google Text-to-Speech)** (for voice conversion)
- **PIL (Pillow)** (for image processing)

## 📂 Installation & Setup

### Prerequisites
Ensure you have Python installed (preferably Python 3.x).

1. Clone the repository:
   ```bash
   git clone https://github.com/perarulalan15/Image-to-Audio-Converter-Extract-and-Read-Text-Aloud.git
   cd Image-to-Audio-Converter-Extract-and-Read-Text-Aloud
2. Install Tesseract OCR:

   Windows: Download and install Tesseract-OCR.

   Linux/Mac: Install via package manager:
   ```bash
   sudo apt install tesseract-ocr  # Ubuntu
   brew install tesseract          # macOS

## 📷 Example

Input Image:

![Image](https://github.com/user-attachments/assets/58817128-65e0-4beb-9912-0f074f465e9d)

Extracted Text: We start with good Because all businesses should be doing something good.

The Audio file will be stored as a "output.mp3" file.
