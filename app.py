import streamlit as st
from utils import login, signup

# ✅ MUST be the first Streamlit command
st.set_page_config(page_title="Medicinal Plant ID", layout="centered")

# ✅ Apply custom styles
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ✅ Session management
if "user" not in st.session_state:
    st.session_state.user = None
if "visited" not in st.session_state:
    st.session_state.visited = False

# # ✅ First-time redirect to Welcome screen
# if not st.session_state.visited:
#     st.session_state.visited = True
#     # st.switch_page("pages/Welcome.py")

# ✅ Login / Signup screen
if st.session_state.user is None:
    st.title("Login")
    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pwd")
        if st.button("Login"):
            if login(email, password):
                st.session_state.user = email
                st.success("Login successful!")
                st.switch_page("pages/Home.py")
            else:
                st.error("Invalid credentials.")

    with tab2:
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pwd")
        if st.button("Signup"):
            if signup(email, password):
                st.success("Signup successful! Please log in.")
            else:
                st.error("Email already exists.")

# # ✅ Sidebar for logged-in users
# else:
#     st.sidebar.success(f"Welcome, {st.session_state.user}")
#     st.sidebar.page_link("pages/Home.py", label="🏠 Home")
#     st.sidebar.page_link("pages/Predict.py", label="🔍 Predict")
#     st.sidebar.page_link("pages/History.py", label="🕓 History")
#     st.sidebar.page_link("pages/Logout.py", label="🚪 Logout")

# --------
# import streamlit as st
# from utils import login, signup

# st.set_page_config(page_title="Medicinal Plant ID", layout="centered")

# if "user" not in st.session_state:
#     st.session_state.user = None

# # Login / Signup screen
# if st.session_state.user is None:
#     st.title("🌿 Medicinal Plant Identifier - Login")
#     tab1, tab2 = st.tabs(["Login", "Signup"])

#     with tab1:
#         email = st.text_input("Email", key="login_email")
#         password = st.text_input("Password", type="password", key="login_pwd")
#         if st.button("Login"):
#             if login(email, password):
#                 st.session_state.user = email
#                 st.success("Login successful!")
#                 st.rerun()
#             else:
#                 st.error("Invalid credentials.")

#     with tab2:
#         email = st.text_input("Email", key="signup_email")
#         password = st.text_input("Password", type="password", key="signup_pwd")
#         if st.button("Signup"):
#             if signup(email, password):
#                 st.success("Signup successful! Please log in.")
#             else:
#                 st.error("Email already exists.")
# else:
#     st.sidebar.success(f"Welcome, {st.session_state.user}")
#     st.sidebar.page_link("pages/Home.py", label="🏠 Home")
#     st.sidebar.page_link("pages/Predict.py", label="🔍 Predict")
#     st.sidebar.page_link("pages/History.py", label="🕓 History")
#     st.sidebar.page_link("pages/Logout.py", label="🚪 Logout")



# import streamlit as st
# from utils import login, signup

# st.set_page_config(page_title="Medicinal Plant Identifier", layout="centered")

# if "user" not in st.session_state:
#     st.session_state.user = None

# if st.session_state.user is None:
#     st.title("🔐 Login / Signup")
#     tab1, tab2 = st.tabs(["Login", "Signup"])

#     with tab1:
#         email = st.text_input("Email", key="login_email")
#         password = st.text_input("Password", type="password", key="login_pwd")
#         if st.button("Login"):
#             if login(email, password):
#                 st.session_state.user = email
#                 st.success("Login successful!")
#                 st.rerun()
#             else:
#                 st.error("Invalid credentials.")

#     with tab2:
#         email = st.text_input("Email", key="signup_email")
#         password = st.text_input("Password", type="password", key="signup_pwd")
#         if st.button("Signup"):
#             if signup(email, password):
#                 st.success("Signup successful! Please log in.")
#             else:
#                 st.error("Email already exists.")
# else:
#     st.sidebar.success(f"Logged in as {st.session_state.user}")
#     st.sidebar.page_link("pages/1_Home.py", label="🏠 Home")
#     st.sidebar.page_link("pages/2_Predict.py", label="🔍 Predict")
#     st.sidebar.page_link("pages/3_History.py", label="🕓 History")
#     st.sidebar.page_link("pages/4_Logout.py", label="🚪 Logout")
