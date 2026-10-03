# VisionQuery AI

An AI-powered video understanding application that lets users upload videos and ask natural-language questions about their content using Google's Gemini multimodal AI.

## Live Demo

🚀 **Try VisionQuery AI:** https://visionquery-ai-6tykvdqbccbagmdoquki3g.streamlit.app/

## Features

- 📹 **Video Upload**: Support for multiple video formats (MP4, AVI, MOV, MKV, WEBM)
- 🤖 **AI-Powered Video Analysis**: Ask questions about video content using Gemini's video understanding
- 💬 **Interactive Chat**: Have a conversational interaction with the uploaded video
- 🔄 **Session Management**: Maintain chat history and video context during a session
- ⚡ **Real-time Processing**: Upload and process videos with progress feedback
- 🎬 **Video Preview**: Preview the uploaded video directly in the application

## Setup

### 1. Install Dependencies

    pip install -r requirements.txt

### 2. Get Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Create a new API key
3. Keep the API key secure

Create a `.env` file in the project root:

    GEMINI_API_KEY=your_api_key_here

### 3. Run the Application

    streamlit run app.py

The application will open in your browser at:

    http://localhost:8501

## Usage

### 1. Configure API Key

Add your Gemini API key to the `.env` file:

    GEMINI_API_KEY=your_api_key_here

### 2. Upload Video

Choose a video file from the sidebar.

Supported formats:

- MP4
- AVI
- MOV
- MKV
- WEBM

### 3. Wait for Processing

The video will be uploaded to Gemini and processed automatically.

### 4. Ask Questions

Enter a natural-language question about the uploaded video.

### 5. View Results

Gemini analyzes the video and generates an AI-powered response.

## Example Questions

- "What is happening in this video?"
- "Summarize the main events."
- "What objects are visible?"
- "Describe the setting and environment."
- "What actions are taking place?"
- "Describe the people and objects you see."

## How It Works

    Video Upload
          ↓
    Gemini File API
          ↓
    Video Processing
          ↓
    Natural-Language Question
          ↓
    Gemini Video Understanding
          ↓
    AI-Generated Response

## Technical Details

- **Video Processing**: Uses the Gemini File API for video upload and processing
- **Multimodal AI**: Uses Gemini's multimodal capabilities to understand video content
- **Natural Language Interaction**: Allows users to ask questions about uploaded videos
- **Supported Formats**: MP4, AVI, MOV, MKV, WEBM
- **Maximum File Size**: Large files may require additional processing time

## Project Structure

    VisionQuery-AI/
    │
    ├── app.py
    ├── demo.py
    ├── test_setup.py
    ├── requirements.txt
    ├── README.md
    ├── USAGE.md
    ├── env.example
    └── .gitignore

## Limitations

- Video processing time depends on file size and content
- Gemini API usage is subject to available quotas and limits
- Large videos may take longer to upload and process
- Internet access is required for Gemini API requests

## Troubleshooting

### Upload Fails

Check the video format and file size.

### Processing Takes Time

Larger videos may require additional processing time.

### API Errors

Verify that your Gemini API key is valid and has available quota.

### No Response

Try refreshing the page, re-uploading the video, and submitting the question again.

## Built With

- [Streamlit](https://streamlit.io/) - Web application framework
- [Google Gemini API](https://ai.google.dev/gemini-api) - Multimodal video understanding
- [Google GenAI Python SDK](https://github.com/googleapis/python-genai) - Gemini API integration
- [Python](https://www.python.org/) - Application development

## Future Improvements

- Timestamp-based video answers
- Automatic video summarization
- Downloadable analysis reports
- Multi-video comparison
- Scene and topic extraction
- Improved conversational memory

---

**VisionQuery AI** — Ask your videos anything.
