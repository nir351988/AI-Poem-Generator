# AI Poem Generator  
[![Build Status](https://github.com/nir351988/AI-Poem-Generator/actions/workflows/docker-image.yml/badge.svg)](https://github.com/nir351988/AI-Poem-Generator/actions)  
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)  
[![Docker Image Version](https://img.shields.io/docker/v/ninadranade/ai-poem-generator?logo=docker)](https://hub.docker.com/r/ninadranade/ai-poem-generator)

A Flask-based web application that generates personalized poems using both AI-driven and template-based methods, highlighted with clear code examples and badges for easy navigation.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technical Architecture](#technical-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Dockerization](#dockerization)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The AI Poem Generator lets you supply words or phrases that are dynamically integrated into creative poem outputs. It leverages both AI-powered generation and pre-defined templates, demonstrating innovative use of modern web and machine learning technologies.

---

## Features

- **Dual Generation Approaches:** Combines AI-powered text generation with customizable poem templates.
- **Dynamic Input Handling:** Seamlessly incorporates user-provided words/phrases into generated poetry.
- **Responsive Design:** Optimized for both desktop and mobile devices.
- **Intuitive Interface:** Easy-to-use UI for generating unique and personalized poems.

---

## Technical Architecture

The application is built using:
- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, and Bootstrap
- **AI Integration:** State-of-the-art text generation libraries
- **Containerization:** Docker for consistent deployments
- **CI/CD:** GitHub Actions automates the build and deployment pipeline

---

## Installation

### Prerequisites

- Python 3.10 or later
- Git
- (Optional) Virtual Environment setup (e.g., venv)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nir351988/AI-Poem-Generator.git
   cd AI-Poem-Generator
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Create a `.env` file if your application requires custom configurations.

---

## Usage

### Running Locally

Start the Flask development server:
```bash
flask run
```
Then open your browser and navigate to:
```
http://127.0.0.1:5000
```

### Running Tests

If tests are provided, you can run:
```bash
pytest
```

---

## Dockerization

This project includes a `Dockerfile` and a `docker-compose.yml` for containerized deployments.

### Using Docker

- **Build the Docker Image:**
  ```bash
  docker build -t ai-poem-generator .
  ```
- **Run the Docker Container:**
  ```bash
  docker run -p 5000:5000 ai-poem-generator
  ```

### Using Docker Compose

- **Build and Start the Container:**
  ```bash
  docker-compose up --build
  ```
- **Stop the Container:**
  ```bash
  docker-compose down
  ```

---

## CI/CD Pipeline

This repository uses GitHub Actions to automatically build and push Docker images on every push to the master branch.

- The workflow file is located at [`.github/workflows/docker-image.yml`](.github/workflows/docker-image.yml).
- It uses Docker Buildx, logs into Docker Hub, and pushes the image to [ninadranade/ai-poem-generator](https://hub.docker.com/r/ninadranade/ai-poem-generator).

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Follow coding conventions and add tests where appropriate.
4. Submit a pull request detailing your changes.

For more detailed instructions, please refer to [CONTRIBUTING.md](CONTRIBUTING.md) (if available).

---

## License

This project is licensed under the [MIT License](LICENSE).
