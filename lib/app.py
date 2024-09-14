import streamlit as st
from io import BytesIO
import json

from llm import get_flashcards, get_question, get_quiz

# Streamlit app layout
st.title('LearnAnything - The Flashcard and Quiz Generator')

# Upload a document
uploaded_file = st.file_uploader("Upload a document", type=['txt', 'docx', 'pdf'])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    num_lines = st.number_input(
        label="Set number of flashcards",
        min_value=5,
        max_value=50,
        value=30
    )

    if st.button('Generate flashcards'):
        st.write("Processing the file...")

        df = get_flashcards(uploaded_file.getvalue(), num_lines)
        
        st.write("File processed successfully!")
        
        st.dataframe(df)
        
        csv_file = BytesIO()
        df.to_csv(csv_file, index=False)
        csv_file.seek(0)
        
        st.download_button(
            label="Download CSV",
            data=csv_file,
            file_name="output.csv",
            mime="text/csv"
        )

    # Add a button to start the quiz
    if st.button('Start Quiz'):
        st.session_state.quiz_data = get_quiz(uploaded_file.getvalue(), 15)
        st.session_state.quiz_started = True
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.selected_option = None
        st.session_state.answer_submitted = False

# Initialize session variables if they do not exist
default_values = {
    'current_index': 0,
    'score': 0,
    'selected_option': None,
    'answer_submitted': False,
    'quiz_started': False
}
for key, value in default_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

def restart_quiz():
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

def submit_answer():
    if st.session_state.selected_option is not None:
        st.session_state.answer_submitted = True
        if st.session_state.selected_option == st.session_state.quiz_data[st.session_state.current_index].answer:
            st.session_state.score += 1
    else:
        st.warning("Please select an option before submitting.")

def next_question():
    st.session_state.current_index += 1
    st.session_state.selected_option = None
    st.session_state.answer_submitted = False

if st.session_state.quiz_started and 'quiz_data' in st.session_state:
    # Progress bar
    progress_bar_value = (st.session_state.current_index + 1) / len(st.session_state.quiz_data)
    st.metric(label="Score", value=f"{st.session_state.score} / {len(st.session_state.quiz_data)}")
    st.progress(progress_bar_value)

    # Display the question and answer options
    question_item = st.session_state.quiz_data[st.session_state.current_index]
    st.subheader(f"Question {st.session_state.current_index + 1}")
    st.title(f"{question_item.question}")

    st.markdown(""" ___""")

    # Answer selection
    options = question_item.options
    correct_answer = question_item.answer

    if st.session_state.answer_submitted:
        for i, option in enumerate(options):
            label = option
            if option == correct_answer:
                st.success(f"{label} (Correct answer)")
            elif option == st.session_state.selected_option:
                st.error(f"{label} (Incorrect answer)")
            else:
                st.write(label)
    else:
        for i, option in enumerate(options):
            if st.button(option, key=i, use_container_width=True):
                st.session_state.selected_option = option

    st.markdown(""" ___""")

    # Submission button and response logic
    if st.session_state.answer_submitted:
        if st.session_state.current_index < len(st.session_state.quiz_data) - 1:
            st.button('Next', on_click=next_question)
        else:
            st.write(f"Quiz completed! Your score is: {st.session_state.score} / {len(st.session_state.quiz_data)}")
            if st.button('Restart', on_click=restart_quiz):
                pass
    else:
        if st.session_state.current_index < len(st.session_state.quiz_data):
            st.button('Submit', on_click=submit_answer)