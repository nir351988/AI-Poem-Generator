
Below is an updated version of your README file that incorporates additional details on Dockerization, CI/CD setup, and usage instructions, while also refining the overall project documentation.



```
# AI Poem Generator

A Flask-based web application that generates customized poems based on user input. This project demonstrates fundamental web development concepts including Flask routing, template rendering, form handling, and both template-based and AI-powered text generation.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [CI/CD Pipeline](#cicd-pipeline)
- [API Documentation](#api-documentation)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The AI Poem Generator allows users to supply words or phrases that are then incorporated into poem templates or used by AI models to generate unique poems. The application randomly selects from template-based generation or employs AI techniques to produce personalized poetry.

**Note:** The project utilizes both template-based approaches and AI-driven generation methods to create diverse poetic outputs.

---

## Features

- **AI-Powered Generation:** Uses Hugging Face's text generation models for creating unique poems.
- **Template-Based Generation:** Falls back to predefined poem templates if AI generation is not available.
- **Dynamic Content Insertion:** Incorporates user input directly into the generated poem.
- **Responsive Design:** Optimized for both desktop and mobile devices (using Bootstrap).
- **Input Validation:** Prevents form submission with empty or invalid inputs.
- **User-Friendly Interface:** Clean, intuitive design for a seamless user experience.

---

## Technical Architecture

The application is built using Flask for the backend, with HTML5, CSS3, and Bootstrap enhancing the frontend. It leverages modern Python libraries for both AI text generation and template manipulation.

---

## Installation

### Prerequisites

- Python 3.6+
- Virtual Environment tools (optional but recommended)

### Steps

1. Clone the repository:
   ```
   git clone https://github.com/nir351988/AI-Poem-Generator.git
   cd AI-Poem-Generator
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate   # On Windows, run .venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure environment variables (if applicable):
   Create a `.env` file (optional) for settings specific to your environment.

---

## Usage

To run the application locally:
```
flask run
```
By default, the app runs on port 5000. Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## Dockerization

You can containerize this application using Docker. Two configuration files have been provided:

### Dockerfile

The Dockerfile installs system dependencies, Python libraries, and sets up the environment with a non-root user. It uses Gunicorn to serve the app in production.

### docker-compose.yml

This file simplifies the building, configuration, and running of your container, and supports loading environment variables from a `.env` file.

### Basic Commands

- **Build the Docker Image:**
  ```
  docker build -t ai-poem-generator .
  ```
- **Run the Docker Container:**
  ```
  docker run -p 5000:5000 ai-poem-generator
  ```
- **Using Docker Compose:**
  Build and run with:
  ```
  docker-compose up --build
  ```
  Run in detached mode:
  ```
  docker-compose up --build -d
  ```
- **Stop and Remove Containers (Docker Compose):**
  ```
  docker-compose down
  ```

---

## CI/CD Pipeline

A GitHub Actions workflow has been set up to automate the following:
- Build your Docker image.
- Log in to Docker Hub.
- Tag and push the image to Docker Hub (repository: `ninadranade/ai-poem-generator`).

**Setup Steps:**

1. Add the following secrets in your GitHub repository’s settings:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_PASSWORD`

2. The workflow file is located at `.github/workflows/docker-image.yml` and is triggered on pushes to the main branch.

This automation allows you to have a reliable CI/CD pipeline without the need for external platforms; the GitHub-hosted runners handle the build process.

---

## API Documentation

Detailed API documentation (if applicable) can be added here. Outline endpoints, expected parameters, sample request/response bodies, and any authentication details.

---

## Development

For local development:
- Use a virtual environment.
- Leverage the volume mapping feature in `docker-compose.yml` for live code syncing.
- Update environment variables as needed during development.

Refer to the [Dockerization](#dockerization) section for running the app in a container during development.

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request with your improvements.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

This README serves as a comprehensive guide to understanding, deploying, and contributing to the AI Poem Generator application. Adjust sections as needed based on future changes or project requirements.
```


Feel free to modify or enhance further based on your project's evolving needs.
