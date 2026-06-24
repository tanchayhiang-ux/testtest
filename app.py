```python
import streamlit as st
import random

# =====================================================
# PAGE SETTINGS
# =====================================================
st.set_page_config(
    page_title="Composition Quest Adventure",
    page_icon="✏️",
    layout="centered"
)

# =====================================================
# GAME DATA
# =====================================================
missions = [
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

tips = [
    "Use adjectives to describe people and places.",
    "Describe what characters see, hear and feel.",
    "Include a problem and solution.",
    "Use exciting action verbs.",
    "Show feelings instead of simply telling.",
    "End your story with a lesson learned."
]

# =====================================================
# SESSION STATE
# =====================================================
if "score" not in st.session_state:
    st.session_state.score = 0

if "mission" not in st.session_state:
    st.session_state.mission = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

# =====================================================
# TITLE
# =====================================================
st.title("🎮 Composition Quest Adventure")
st.write("Complete all missions and become a Composition Master!")

# =====================================================
# SCORE
# =====================================================
st.metric("🏆 Score", st.session_state.score)

progress = st.session_state.mission / len(missions)
st.progress(progress)

# =====================================================
# GAME COMPLETE
# =====================================================
if st.session_state.mission >= len(missions):

    st.balloons()

    st.success("🎉 Congratulations! You completed all missions!")

    if st.session_state.score >= 60:
        badge = "🏆 Composition Master"
    elif st.session_state.score >= 40:
        badge = "🌟 Creative Author"
    elif st.session_state.score >= 20:
        badge = "👍 Junior Writer"
    else:
        badge = "📖 Story Explorer"

    st.header(badge)

    st.write(f"Final Score: **{st.session_state.score}**")

    if st.button("🔄 Play Again"):
        st.session_state.score = 0
        st.session_state.mission = 0
        st.session_state.answered = False
        st.rerun()

else:

    current = missions[st.session_state.mission]

    st.subheader(
        f"Mission {st.session_state.mission + 1}: {current['skill']}"
    )

    st.info(current["question"])

    selected = st.radio(
        "Choose the best answer:",
        current["options"],
        key=f"mission_{st.session_state.mission}"
    )

    if st.button("✅ Submit Answer") and not st.session_state.answered:

        selected_index = current["options"].index(selected)

        if selected_index == current["answer"]:

            st.success("🎉 Correct!")
            st.write(current["explanation"])
            st.session_state.score += 10

        else:

            st.error("❌ Not quite right.")

            st.write(
                f"Correct Answer: **{current['options'][current['answer']]}**"
            )

            st.info(current["explanation"])

        st.session_state.answered = True

    if st.session_state.answered:

        if st.button("➡️ Next Mission"):

            st.session_state.mission += 1
            st.session_state.answered = False
            st.rerun()

# =====================================================
# WRITING TIP
# =====================================================
st.divider()

st.subheader("💡 Writing Tip")

random.seed()
st.success(random.choice(tips))

# =====================================================
# SIDEBAR
# =====================================================
with st.sidebar:

    st.header("📚 Story Structure")

    st.write("1️⃣ Character")
    st.write("2️⃣ Setting")
    st.write("3️⃣ Problem")
    st.write("4️⃣ Feelings")
    st.write("5️⃣ Action")
    st.write("6️⃣ Ending")

    st.divider()

    st.write("Earn 10 points for each correct answer!")

    if st.button("Reset Game"):

        st.session_state.score = 0
        st.session_state.mission = 0
        st.session_state.answered = False

        st.rerun()
```
