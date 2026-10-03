# VisionQuery AI — Usage Guide

VisionQuery AI lets you upload a video and interact with it using natural-language questions powered by Google Gemini.

## 1. Requirements

Make sure you have:

- Python 3.9 or newer
- A Google Gemini API key
- An internet connection

## 2. Install the dependencies

Open PowerShell inside the project folder:

    cd C:\Users\DELL\OneDrive\Desktop\VisionQuery-AI

Create and activate the virtual environment:

    python -m venv .venv
    .\.venv\Scripts\Activate.ps1

Install the required packages:

    pip install -r requirements.txt

## 3. Configure the Gemini API key

Create a file named:

    .env

Add:

    GEMINI_API_KEY=your_api_key_here

Do not upload your `.env` file to GitHub.

The project already includes `.gitignore` rules to keep sensitive environment files out of the repository.

## 4. Test the Gemini setup

Run:

    python test_setup.py

A successful setup should show that the API key was found and that the Gemini API connection was successful.

## 5. Run VisionQuery AI

Start the Streamlit application:

    streamlit run app.py

Streamlit will provide a local URL, usually:

    http://localhost:8501

Open the URL in your browser.

## 6. Using the application

### Step 1 — Upload a video

Use the upload section in the sidebar.

Supported formats include:

- MP4
- AVI
- MOV
- MKV
- WEBM

### Step 2 — Wait for processing

After uploading the video, VisionQuery AI sends the video to Gemini for processing.

Processing time depends on the video size and length.

### Step 3 — Ask questions

Once the video is processed, type questions about its content.

Example questions:

- What happens in this video?
- Summarize the main events.
- What objects are visible?
- What actions are taking place?
- Describe the scene.
- What happens at the beginning?
- What happens near the end?
- How does the scene change throughout the video?

The application generates answers based on the uploaded video.

## 7. Demo script

The project also includes `demo.py`, which provides a simple command-line way to test video analysis.

Run:

    python demo.py

Enter the path to your video when prompted and then enter your question.

## 8. Project workflow

The application follows this general pipeline:

    Video Upload
         ↓
    Gemini File Upload
         ↓
    Video Processing
         ↓
    Gemini Multimodal Model
         ↓
    User Question
         ↓
    AI Generated Answer

## 9. Important notes

### API key security

Never share your Gemini API key publicly.

Do not commit:

    .env

to GitHub.

If an API key is accidentally exposed, revoke it and create a new one.

### Video processing

Uploaded videos are processed using Google's Gemini API.

Processing time can vary depending on video size and other API conditions.

### Internet connection

VisionQuery AI requires an internet connection because video processing and AI inference use the Gemini API.

## 10. Troubleshooting

### API key not found

If you see:

    GEMINI_API_KEY not found

check that:

- `.env` exists in the project directory.
- The variable is named exactly `GEMINI_API_KEY`.
- The API key is valid.

### Gemini API connection failed

Check:

- Your internet connection.
- Your Gemini API key.
- Your Google AI API access.
- Whether the API request has reached its usage limits.

### Streamlit does not start

Make sure the virtual environment is activated and dependencies are installed:

    .\.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

Then run:

    streamlit run app.py

## 11. Live Demo

The deployed Streamlit application can be accessed from the project's GitHub README.

## 12. Technology Stack

- Python
- Streamlit
- Google Gemini
- Google GenAI Python SDK
- python-dotenv

## 13. Project Structure

    VisionQuery-AI/
    │
    ├── app.py
    ├── demo.py
    ├── test_setup.py
    ├── requirements.txt
    ├── env.example
    ├── USAGE.md
    ├── README.md
    └── .gitignore

## 14. Limitations

VisionQuery AI depends on the capabilities, availability, rate limits, and supported video-processing features of the Gemini API.

Large videos may require additional processing time.

The quality of generated answers depends on the video content and the question asked.

## 15. Future Improvements

Potential improvements include:

- Timestamp-based answers
- More detailed video summaries
- Multi-video analysis
- Conversation history
- Improved error handling
- Video chapter generation
- Automatic scene detection
- Support for additional multimodal models