# AI Poem Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.6%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0.1-green)

A Flask-based web application that generates poems based on user input. This application demonstrates fundamental web development concepts including Flask routing, template rendering, form handling, and string manipulation.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

The AI Poem Generator provides a simple interface for users to input words or phrases, which are then incorporated into predefined poem templates or generated using AI models. The application randomly selects a template or uses AI to create a personalized poem.

**Note:** This application now uses both template-based text generation and artificial intelligence (AI) for generating poems.

## Features

- **AI-Powered Generation**: Utilizes Hugging Face's text generation models for creating unique poems
- **Template-Based Generation**: Falls back to predefined poem templates if AI generation fails
- **Dynamic Content Insertion**: Incorporates user input into selected templates or AI-generated poems
- **Responsive Design**: Optimized for both desktop and mobile devices using Bootstrap
- **Input Validation**: Prevents form submission with empty inputs
- **User-Friendly Interface**: Clean, intuitive design for seamless user experience

## Technical Architecture

### Technology Stack

- **Backend**: Python 3.6+, Flask 2.0.1
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Development Tools**: Git, Virtual Environment

### Component Structure

```
AI-Poem-Generator/
├── app.py                  # Application entry point and core logic
├── templates/              # Jinja2 HTML templates
│   ├── index.html          # Home page with input form
│   └── result.html         # Results page displaying generated poem
├── static/                 # Static assets (if applicable)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

### Core Functionality

The application follows a simple MVC-like pattern:

1. **Controller** (app.py): Handles HTTP requests, processes form data, and manages application logic
2. **View** (templates): Renders HTML templates with Jinja2
3. **Model**: Implemented as Python functions that generate poem content

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package manager)
- Git (optional, for cloning the repository)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nir351988/AI-Poem-Generator.git
   cd AI-Poem-Generator
   ```

2. **Create and activate a virtual environment**:
   ```bash
   # Create virtual environment
   python -m venv venv
   
   # Activate on Linux/macOS
   source venv/bin/activate
   
   # Activate on Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python app.py
   ```

5. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`

## Usage

### Generating a Poem

1. Navigate to the home page
2. Enter a word or phrase in the provided input field
3. Optionally, choose a poem style from the dropdown menu
4. Click the "Generate Poem" button
5. View your personalized poem on the results page
6. Click "Generate Another Poem" to create a new poem

### Example

Input: "ocean"

Possible output:
```
The ocean whispers secrets
In the depths of my heart
Like ocean waves crashing
We shall never part
```

## API Documentation

### Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/` | GET | Renders the home page with input form | None |
| `/generate` | POST | Processes user input and generates poem | `user_input`: String, `poem_style`: String (optional) |
| `/result` | GET | Displays the generated poem | None |

## Development

### Project Structure

- **app.py**: Contains Flask application setup, route definitions, and poem generation logic
- **templates/**: Contains Jinja2 HTML templates for rendering pages
  - **index.html**: Home page template with input form
  - **result.html**: Results page template displaying the generated poem

### Adding New Templates

To add new poem templates, modify the `templates` list in `app.py`:

```python
templates = [
    # Existing templates
    "The {} whispers secrets\nIn the depths of my heart\nLike {} waves crashing\nWe shall never part",
    
    # Add new template
    "Your new template with {} placeholders for {} user input"
]
```

## Contributing

Contributions are welcome and appreciated. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Implement your changes
4. Add appropriate tests if applicable
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please ensure your code adheres to the project's coding standards and includes appropriate documentation.

### Development Guidelines

- Follow PEP 8 style guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Update documentation when adding new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Flask framework and its contributors
- Bootstrap for responsive design components
- Hugging Face for the text generation models
- All contributors who have helped improve this project.