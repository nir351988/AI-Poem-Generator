# AI Poem Generator

## Overview

The AI Poem Generator is a web application designed to create unique poems based on user input. By leveraging predefined poem templates, the application fills in the user's input to generate a personalized poem each time.

## Features

- **User-Friendly Interface**: Styled with Bootstrap for a clean and responsive design.
- **Dynamic Poem Generation**: Creates a poem based on the user's input.
- **Result Display**: Shows the generated poem on a separate result page.
- **Input Validation**: Utilizes flash messages for user input validation.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, Bootstrap

## Installation

To set up the AI Poem Generator locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/nir351988/AI-Poem-Generator.git
    cd AI-Poem-Generator
    ```

2. **Create and Activate a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Flask Development Server**:
    ```bash
    python app.py
    ```

2. **Access the Application**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.

## Usage

1. **Input**: Enter a word or phrase in the input field on the home page.
2. **Generate**: Click the "Generate Poem" button.
3. **View**: The generated poem will be displayed on the result page.
4. **Repeat**: Click "Generate Another Poem" to create a new poem.

## Project Structure

```
AI-Poem-Generator/
├── app.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── (optional static files like CSS, JS, images)
├── requirements.txt
└── README.md
```

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests. For major changes, open an issue first to discuss the proposed modifications.

## License

This project is licensed under the MIT License.
