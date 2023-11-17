from contextlib import contextmanager
from deprecation import deprecated
import streamlit as st
import streamlit.components.v1 as components
import os

path = os.getcwd()

class Container:

    def __init__(self, key):
        self.key = key
        st.session_state[f'{self.key}-opened'] = True

    @contextmanager
    def box(self):
        st.markdown(f"""
                <style>
                div[data-modal-container='true'][key='{self.key}'] {{
                    background-color: #f9fafb;
                    border: 1px solid #f3f4f6;
                    padding: 10px 10px 10px 5px;
                    box-sizing: border-box;
                    display: flex;
                    flex-direction: row;
                    width: 104% !important;
                    
                  }}
                </style>
             """, unsafe_allow_html=True)
        with st.container():
            _container = st.container()

        components.html(
            f"""
            <script>
            // STREAMLIT-MODAL-IFRAME-{self.key} <- Don't remove this comment. It's used to find our iframe
            const iframes = parent.document.body.getElementsByTagName('iframe');
            let container
            for (const iframe of iframes) {{
            if (iframe.srcdoc.indexOf("STREAMLIT-MODAL-IFRAME-{self.key}") !== -1) {{
                container = iframe.parentNode.previousSibling;
                container.setAttribute('data-modal-container', 'true');
                container.setAttribute('key', '{self.key}');
                }}
                }}
            </script>
            """, height=0, width=0
        )

        with _container:
            yield _container

