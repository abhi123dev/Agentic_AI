# Study Buddy Bot using Anthropic API

## Overview

This project is a simple **Study Buddy** chatbot built using the **Anthropic Claude API**. It accepts a study topic from the user, sends it to the Claude model, and returns a simple explanation in **under 100 words**.

This project demonstrates:
- Using the Anthropic API
- Handling user input
- Basic input validation
- Printing AI-generated responses in the terminal

---

## Features

- Accepts a topic from the user
- Explains the topic in simple language
- Limits the explanation to under 100 words
- Handles empty input gracefully
- Uses the Anthropic API securely through an environment variable

---

## Requirements

- Python 3.8 or above
- Anthropic Python SDK

Install the required package:

```bash
pip install anthropic
```

---

## Setting Up the API Key

Create an API key from Anthropic.

### Windows (PowerShell)

```powershell
$env:ANTHROPIC_API_KEY="your_api_key_here"
```

### macOS/Linux

```bash
export ANTHROPIC_API_KEY="your_api_key_here"
```

Alternatively, you can permanently add the environment variable to your system settings.

---

## Project Structure

```
StudyBuddy/
│
├── study_buddy.py
└── README.md
└── Sample_Output_image.png

```

---

## How to Run

Run the program using:

```bash
python study_buddy.py
```

The program will ask for a topic:

```
Enter a topic to study:
```

Type any topic, for example:

```
Context window in LLMs
```

The bot will generate a simple explanation and display it in the terminal.

---

## Sample Output 
<p align="center">
  <img src="https://github.com/abhi123dev/Agentic_AI/blob/main/Q2_Assignment1/Sample_Output_image.png?raw=true" alt="Sample Output" width="800">
</p>



## Input Validation

If the user enters an empty topic:

### Input

```
Enter a topic to study:
```

### Output

```
Error: Topic cannot be empty.
```

---

## Technologies Used

- Python
- Anthropic Claude API

---

## Learning Objectives

This project helps understand:
- How APIs work
- How to interact with an LLM using Python
- Basic prompt engineering
- Secure API key handling
- User input validation
