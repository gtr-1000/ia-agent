# AI Agent — Gemini Chatbot

A simple AI chatbot built with Python and Streamlit, powered by Google's Gemini API through the OpenAI-compatible API interface.

This project was developed to practice API integration, Python application development, conversation history management, and secure configuration of API credentials.

## Features

- Interactive chat interface built with Streamlit.
- Integration with Google's Gemini API.
- Conversation history maintained during the user session.
- API credentials stored separately from the application code.
- Error handling for failed API requests.
- Loading indicator while waiting for the model's response.

## Technologies

- **Python**
- **Streamlit** — Web interface
- **OpenAI Python SDK** — API client
- **Google Gemini API** — Language model

## Project Structure

```text
ia-agent/
├── .streamlit/
│   └── secrets.toml.example
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/gtr-1000/ia-agent.git
cd ia-agent
```

### 2. Create a virtual environment

**Windows (Command Prompt):**

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your API key

Create a file named `secrets.toml` inside the `.streamlit` directory.

Copy the structure from `.streamlit/secrets.toml.example` and replace the placeholder with your Google AI Studio API key:

```toml
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"
```

Get an API key from [Google AI Studio](https://aistudio.google.com/apikey).

**Security:** Never commit your real `secrets.toml` file or publish your API key. The file is excluded through `.gitignore`.

### 5. Run the application

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually `http://localhost:8501`.

## Configuration

The application reads the API key through Streamlit's secrets management:

```python
api_key = st.secrets["GOOGLE_API_KEY"]
```

The configured Gemini model must be available to your Google AI Studio project and API quota.

## Current Limitations

- Conversation history is stored in session state and is not permanent.
- API requests require an internet connection and an available Gemini API quota.
- The application currently provides a basic text-chat experience.

## Future Improvements

- Add a clear-chat button.
- Improve handling of rate limits and temporary API errors.
- Add conversation export.
- Improve the interface and user experience.
- Deploy the application online.

## License

No license has been specified yet.
