# 📚 BlogMate: AI Blog Buddy

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Gemini API](https://img.shields.io/badge/Google_Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemini-api/docs/oauth)

Welcome to **BlogMate**, an AI-driven blog generation tool designed for efficient and high-quality content creation. Utilizing the Google Gemini API with advanced language models, BlogMate can help generate articles on a wide range of topics with academic keyword intensity.

## 🌟 Features

- **Automated Blog Generation**: Generate fully customized blogs using AI.
- **Adjustable Content Parameters**: Customize blog title, keywords, word count, and images.
- **Streamlit UI**: Interactive, user-friendly interface for seamless input.

## 🚀 Tech Stack

- **[Streamlit](https://streamlit.io/)**: For creating an interactive web-based interface.
- **[Python](https://www.python.org/)**: The programming language behind BlogMate.
- **[Google Generative AI (Gemini-1.5 Pro Model)](https://ai.google.dev/gemini-api/docs/oauth)**: Utilized for blog content generation with customizable parameters.

## 🔧 Configuration

To use BlogMate, set up the environment variable `GEMINI_API_KEY` to authenticate with Google Gemini's API.

```bash
export GEMINI_API_KEY='YOUR_API_KEY'

## 🌟 Features

- **Automated Blog Generation**: Generate fully customized blogs using AI.
- **Adjustable Content Parameters**: Customize blog title, keywords, word count, and images.
- **Streamlit UI**: Interactive, user-friendly interface for seamless input.

## 🚀 Tech Stack

- **[Streamlit](https://streamlit.io/)**: For creating an interactive web-based interface.
- **[Python](https://www.python.org/)**: The programming language behind BlogMate.
- **[Google Generative AI (Gemini-1.5 Pro Model)](https://ai.google.dev/gemini-api/docs/oauth)**: Utilized for blog content generation with customizable parameters.

## 🔧 Configuration

To use BlogMate, set up the environment variable `GEMINI_API_KEY` to authenticate with Google Gemini's API.

```bash
export GEMINI_API_KEY='YOUR_API_KEY'
```

Ensure the API key is stored securely and not hardcoded into the application source.

## 📜 How to Use

1. **Setup Environment**:
   - Ensure you have the required dependencies installed:
     ```bash
     pip install streamlit google-generativeai
     ```

2. **Run the Application**:
   - Start the application locally by running:
     ```bash
     streamlit run app.py
     ```

3. **User Interaction**:
   - Use the sidebar to input the blog title, keywords, desired word count, and number of images.
   - Click **Generate Blog** to create an AI-powered blog on your chosen topic.

