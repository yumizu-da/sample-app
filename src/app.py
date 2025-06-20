import json

import streamlit as st

from src.utils.logger import logger


if __name__ == "__main__":
    st.set_page_config(page_title="Sample App")
    st.title("Sample App")
    selected_food = st.radio("Which food do you like?", ["Sushi", "Ramen"])

    if st.button("Submit"):
        st.write(f"You chose {selected_food}")
        st.balloons()

        log_info = {
            "user_id": "12345",
            "food": selected_food,
        }
        logger.info(json.dumps(log_info))