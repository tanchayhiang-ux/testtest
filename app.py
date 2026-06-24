import streamlit as st
import random

# Page setup
st.set_page_config(
    page_title="Composition Quest Adventure",
    page_icon="✏️",
    layout="centered"
)

# Questions
QUESTIONS = [
    {
        "skill": "Character",
        "question": "Which description creates the most interesting character?",
        "options": [
            "Tom was a boy.",
            "Tom was a cheerful boy who always helped others.",
            "Tom was ten years old.",
            "Tom lived in Singapore."
        ],
        "answer": 1,
        "explanation": "Good characters have personality traits that make them memorable."
    },
    {
        "skill": "Setting",
        "question": "Which sentence creates the best setting?",
        "options": [
            "I went to the park.",
            "The park was big.",
            "The colourful playground buzzed with laughter under the bright morning sun.",
            "There were people."
        ],
        "answer": 2,
        "explanation": "Strong settings use descriptive details."
    },
    {
        "skill": "Problem",
        "question": "Which is the most interesting story problem?",
        "options": [
            "I ate lunch.",
            "I lost my favourite wallet during a school trip.",
            "I watched television.",
            "I played football."
        ],
        "answer": 1,
        "explanation": "Stories become exciting when characters face problems."
    },
    {
        "skill": "Feelings",
        "question": "Which sentence best shows feelings?",
        "options": [
            "I was scared.",
            "Fear gripped me as my hands trembled.",
            "I walked away.",
            "The room was dark."
        ],
        "answer": 1,
        "explanation": "Showing feelings creates a stronger story."
    },
    {
        "skill": "Show, Don't Tell",
        "question": "Which sentence is better?",
        "options": [
            "I was happy.",
            "Joy filled my heart and a wide smile spread across my face.",
            "I went home.",
            "The day ended."
        ],
        "answer": 1,
        "explanation": "Showing emotions helps readers imagine the scene."
    },
    {
        "skill": "Ending",
        "question": "Which ending is strongest?",
        "options": [
            "The End.",
            "I learned that honesty is always the best policy.",
            "Then I went home.",
            "It happened yesterday."
        ],
        "answer": 1,
        "explanation": "Good endings often include a lesson learned."
    }
]

TIPS = [
    "Use adjectives to describe people and places.",
    "Describe what characters see, hear and feel.",
    "Include a problem and solution.",
    "Use exciting action verbs.",
    "Show feelings instead of simply telling.",
    "End your story with a lesson learned."
]

# Session state
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_index" not in st.session_state:
    st.session_state.question_index = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

# Title
st.title("🎮 Composition Quest Adventure")
st.write("Learn composition writing while playing!")

# Score
st.metric("🏆 Score", st.session_state.score)

progress = st.session_state.question_index / len(QUESTIONS)
st.progress(progress)

# Finished game
if st.session_state.question_index >= len(QUESTIONS):

    st.balloons()
    st.success("🎉 Congratulations! You completed the game!")

    if st.session_state.score >= 60:
        badge = "🏆 Composition Master"
    elif st.session_state.score >= 40:
        badge = "🌟 Creative Author"
    elif st.session_state.score >= 20:
        badge = "👍 Junior Writer"
    else:
        badge = "📖 Story Explorer"

    st.header(badge)

    if st.button("🔄 Play Again"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.answered = False
        st.rerun()

else:

    current = QUESTIONS[st.session_state.question_index]

    st.subheader(
        f"Mission {st.session_state.question_index + 1}: {current['skill']}"
    )

    st.info(current["question"])

    selected_answer = st.radio(
        "Choose the best answer:",
        current["options"],
        key=f"q_{st.session_state.question_index}"
    )

    if not st.session_state.answered:

        if st.button("Submit Answer"):

            selected_index = current["options"].index(selected_answer)

            if selected_index == current["answer"]:

                st.success("✅ Correct!")
                st.write(current["explanation"])

                st.session_state.score += 10

            else:

                st.error("❌ Not quite right.")

                st.write(
                    "Correct answer: "
                    + current["options"][current["answer"]]
                )

                st.info(current["explanation"])

            st.session_state.answered = True
            st.rerun()

    else:

        if st.button("Next Mission"):

            st.session_state.question_index += 1
            st.session_state.answered = False
            st.rerun()

# Writing tip
st.divider()

st.subheader("💡 Writing Tip")
st.info(random.choice(TIPS))

# Sidebar
with st.sidebar:

    st.header("📚 Story Structure")

    st.write("1. Character")
    st.write("2. Setting")
    st.write("3. Problem")
    st.write("4. Feelings")
    st.write("5. Action")
    st.write("6. Ending")

    st.divider()

    if st.button("Reset Game"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.session_state.answered = False
        st.rerun()
