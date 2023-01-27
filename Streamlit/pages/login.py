import streamlit as st
import app

if 'id' not in st.session_state:
    st.sidebar.header("Login")

    st.title("Login")

    id=st.text_input("아이디")
    password=st.text_input("비밀번호", type="password")

    col1, col2 = st.columns([0.5,0.5])
    register = col1.button("회원가입")
    login = col2.button("로그인")
    st.session_state['id'] = id
else:
    st.info("이미 로그인 하였습니다.")
    st.write(f'''
        <a target="_self" href="http://localhost:8501">
            <button>
                돌아가기
            </button>
        </a>
    ''',
    unsafe_allow_html=True
    )