# AI-Powered Customer Service Support System

## Overview

This project implements an intelligent customer service support system using OpenAI's GPT models and LangChain framework. The system provides automated responses to customer queries across multiple service categories including billing, technical support, account management, and general product inquiries.

## Key Features

- Query classification using GPT-4
- Content moderation and safety checks
- Prompt injection detection
- Vector-based product information retrieval
- Chain-of-thought reasoning for accurate responses
- Response validation system

## Technologies Used

- OpenAI GPT-4
- LangChain
- FAISS Vector Store
- Python
- JSON

## Setup

1. Clone the repository
2. Install required dependencies:

```bash
pip install langchain-openai langchain-core langchain-community openai python-dotenv faiss-cpu
```

3. Create a `.env` file with your OpenAI API key
4. Place your product data in `Backend/products.json`

## Usage

```python
from Moderations import moderateInput

def AskQuestions(user_input):
    return moderateInput(user_input)

response = AskQuestions(
    "I want to what is the price difference between the cheapest and the most expensive phone ")
```

## Learn More

For a detailed presentation about this project, including architecture diagrams, implementation details, and future improvements, please visit our [Google Slides presentation](https://docs.google.com/presentation/d/1XY0hfPFPodNJ9FpcEbo9kB21XfniKOsUCs41LVV3ESQ/edit?usp=sharing).

## Contributing

Feel free to submit issues and pull requests to help improve the system.

## License

MIT License
