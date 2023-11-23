import streamlit_authenticator as stauth
import streamlit as st


class Authenticate(stauth.Authenticate):
    """Хак для русского языка"""

    def login(self, form_name: str, location: str = 'main') -> tuple:
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")
        if not st.session_state['authentication_status']:
            self._check_cookie()
            if not st.session_state['authentication_status']:
                if location == 'main':
                    login_form = st.form('Login')
                elif location == 'sidebar':
                    login_form = st.sidebar.form('Login')

                login_form.subheader(form_name)
                self.username = login_form.text_input('Логин').lower()
                st.session_state['username'] = self.username
                self.password = login_form.text_input('Пароль', type='password')
                cols = login_form.columns(3)
                if cols[1].form_submit_button('Войти', use_container_width=True):
                    self._check_credentials()

        return st.session_state['name'], st.session_state['authentication_status'], st.session_state['username']

    def logout(self, place, button_name: str, location: str = 'main', key: str = None):
        if location not in ['main', 'sidebar']:
            raise ValueError("Location must be one of 'main' or 'sidebar'")
        if place.button(button_name, key, use_container_width=True):
            self.cookie_manager.delete(self.cookie_name)
            st.session_state['logout'] = True
            st.session_state['name'] = None
            st.session_state['username'] = None
            st.session_state['authentication_status'] = None
