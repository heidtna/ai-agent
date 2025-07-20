# AI Agent

This project is an experimental Python-based AI agent framework that allows interaction with a Large Language Model (LLM) and provides utilities for file management and code execution within a specified working directory.

## Features

- Run prompts through an LLM (Gemini API)
- List files and directories recursively
- Read and write files safely within a working directory
- Execute arbitrary Python files with arguments

## Usage

1. **Install dependencies**  
   Make sure you have Python 3.8+ and install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. **Set up environment variables**  
   Create a `.env` file with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

3. **Run the main agent**  
   ```sh
   python main.py "<your prompt here>"
   ```

4. **Run tests**  
   ```sh
   python -m unittest tests.py
   ```

## WARNING

**This project contains code that allows an LLM to execute arbitrary Python code on your system.**  
Running this project may pose significant security risks, especially if exposed to untrusted input or users. 
There are no security protections in place. 
**Do not run this code on a production system or with sensitive data. Use only in a secure, isolated environment.**
**RUN AT YOUR OWN RISK**

##