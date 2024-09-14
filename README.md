# LearnAnything

This project is a simple interactive web app built using [Streamlit](https://streamlit.io/). The app allows users to upload a document with information to learn (e.g. courses, Wikipedia, etc), create flashcards, take a knowledge quiz, or participate in an open-ended question answering session.

## Features

1. **Upload Document to Generate CSV**: Users can upload a document (e.g., `.txt`, `.docx`, or `.pdf`), and the app sends it to the LLM API to retrieve and download a generated CSV with flashcards.
   
2. **Knowledge Check Options**:
    - **Quiz**: A simple quiz interface where users answer predefined questions.
    - **Open Questions**: A chat-like experience where users receive a question, can either answer it or request help, and then move on to the next question.

## Tech Stack

- [Streamlit](https://streamlit.io/) - Web framework for building the interactive UI.
- [AIML API](https://aimlapi.com/a) - Used to process documents and generate questions.
- Python - The programming language used to create the app.

## Installation

To run the app locally, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/adamgdobrakowski/LearnAnything.git
    ```

2. Navigate to the project directory:

    ```bash
    cd LearnAnything
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      .\venv\Scripts\activate
      ```

    - For MacOS/Linux:

      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:

    ```bash
    streamlit run lib/app.py
    ```

## Usage

1. Open the app in your browser at `http://localhost:8501`.
   
2. **Main Features**:
    - **Upload Document**: Upload a file, set the number of flashcards, click "Generate flashcards" and download the generated CSV.
    - **Upload flashcards to your favourite tool** You can use [Memrise](https://community-courses.memrise.com/dashboard) or DuoLingo to learn this information 
    - **Check My Knowledge**: Click the "Check my knowledge" button, and choose from the available options:
        - **Start Quiz**: Take a predefined knowledge quiz.
        - **Open Questions**: Answer open-ended questions with an option to get help.

3. **Quiz**: You can answer each question, submit your answer, and see the final score.
   
4. **Open Questions**: Respond to one question at a time, ask for help, and move on to the next question.


## Dependencies

The dependencies for this project are listed in the `requirements.txt` file. They include:

- `streamlit`
- `requests`
- `pandas`