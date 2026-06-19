# Setup Guide

## Prerequisites

* Python 3.12+
* OpenAI API Key
* SendGrid API Key

## Installation

```bash
git clone <repo-url>
cd ai-deep-research-assistant
uv sync
```

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_key
SENDGRID_API_KEY=your_key
```

## Run

```bash
python app/main.py
```

This launches the Gradio application locally.
