import streamlit as st
from io import BytesIO

from llm import get_flashcards, get_question

# Streamlit app layout
st.title('LearnAnything - The Flashcard and Quiz Generator')

# Upload a document
uploaded_file = st.file_uploader("Upload a document", type=['txt', 'docx', 'pdf'])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    num_lines = st.number_input(
        label="Set number of flashcards",
        min_value=5,  # Minimum value for the input
        max_value=50,  # Maximum value is the total rows in the dataframe
        value=30  # Default value is the total number of rows
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

# Add a "Check my knowledge" button
if st.button("Quiz"):
    with st.expander("Quiz", expanded=True):
        st.subheader("Quiz Time!")

        quiz_data = {
            "What is the capital of France?": "Paris",
            "Who wrote '1984'?": "George Orwell",
            "What is the square root of 64?": "8"
        }

        score = 0  
        total_questions = len(quiz_data)

        user_answers = {}
        for question in quiz_data.keys():
            user_answers[question] = st.text_input(f"Question: {question}", key=question)

        if st.button("Submit Quiz"):
            for question, correct_answer in quiz_data.items():
                user_answer = user_answers[question]
                if user_answer:
                    if user_answer.lower().strip() == correct_answer.lower().strip():
                        st.write(f"Question: {question} - ✅ Correct!")
                        score += 1
                    else:
                        st.write(f"Question: {question} - ❌ Incorrect! The correct answer is: {correct_answer}")
            
            st.write(f"Your score: {score}/{total_questions}")

