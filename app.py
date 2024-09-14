import streamlit as st
from io import BytesIO

from llm import get_flashcards, get_question

# Below code is generated mainly by ChatGPT

# Streamlit app layout
st.title('LearnAnything - The Fleshcard and Quiz Generator')

# Upload a document
uploaded_file = st.file_uploader("Upload a document", type=['txt', 'docx', 'pdf'])

if uploaded_file is not None:
    st.write("File uploaded successfully!")
    
    # If the file is uploaded, send it to the Langflow API
    # For this example, we mock the API call with a local CSV generation, but
    # you should use the real Langflow API endpoint.
    
    num_lines = st.number_input(
            label="Set number of flashcards",
            min_value=5,  # Minimum value for the input
            max_value=50,  # Maximum value is the total rows in the dataframe
            value=30  # Default value is the total number of rows
        )

    # Create a simple mock CSV from the document (or use the API response)
    if st.button('Generate flashcards'):
        st.write("Processing the file...")

            # Send the request to the Langflow API (POST request)
        df = get_flashcards(uploaded_file.getvalue(), num_lines)
        
        st.write("File processed successfully!")
        
        # Display DataFrame in the app
        st.dataframe(df)
        
        # Convert DataFrame to CSV and prepare download link
        csv_file = BytesIO()
        df.to_csv(csv_file, index=False)
        csv_file.seek(0)
        
        # Provide download link for the CSV
        st.download_button(
            label="Download CSV",
            data=csv_file,
            file_name="output.csv",
            mime="text/csv"
        )
           
# Add a "Check my knowledge" button
if st.button("Quiz"):
    # After the button is clicked, show the options

    # Expander for the quiz (same as the previous code)
    with st.expander("Quiz", expanded=True):
        st.subheader("Quiz Time!")

        #df = get_flashcards(uploaded_file.getvalue(), 15)
        #quiz_data = df.set_index('Question')['Answer'].to_dict()

        quiz_data = {
     "What is the capital of France?": "Paris",
     "Who wrote '1984'?": "George Orwell",
     "What is the square root of 64?": "8"
 }
        # Initialize the score
        score = 0  
        total_questions = len(quiz_data)

        # Display each question and get the user's answer
        for question, correct_answer in quiz_data.items():
            user_answer = st.text_input(f"Question: {question}", key=question)

            # Check if the answer is correct
            if user_answer:
                if user_answer.lower().strip() == correct_answer.lower().strip():
                    st.write("✅ Correct!")
                    score += 1
                else:
                    st.write(f"❌ Incorrect! The correct answer is: {correct_answer}")
        
        # Submit quiz button
        if st.button("Submit Quiz"):
            st.write(f"Your score: {score}/{total_questions}")

#     # Define a list of open questions for the chat interface
# open_questions = [
#     "What is the importance of machine learning in modern AI?",
#     "How does gradient descent work?",
#     "Explain the concept of overfitting in machine learning.",
#     "What is the difference between supervised and unsupervised learning?",
#     "Describe the steps of a typical data science pipeline."
# ]

# # Initialize state variables for question index and help request
# if "current_question_index" not in st.session_state:
#     st.session_state.current_question_index = 0
# if "help_requested" not in st.session_state:
#     st.session_state.help_requested = False

# # Display the current question
# if st.button("Get question"):
#     current_question = get_question(uploaded_file.getvalue()) #open_questions[st.session_state.current_question_index]
#     st.write(f"Question: {current_question}")
#     # Text input for user's answer
#     user_answer = st.text_input("Your answer:", key=f"answer_{st.session_state.current_question_index}")

# # Button for requesting help
# if st.button("Help me"):
#     st.session_state.help_requested = True

# # If help is requested, show a hint or suggested answer
# if st.session_state.help_requested:
#     st.write(f"Hint: Think about the basic principles ")

# # Button to move to the next question
# if st.button("Next question"):
#     # Move to the next question, reset help state
#     st.session_state.current_question_index += 1
#     st.session_state.help_requested = False

#     # Loop back to the first question if reaching the end
#     if st.session_state.current_question_index >= len(open_questions):
#         st.session_state.current_question_index = 0

