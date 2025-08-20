import json

import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from src.core.config import settings
from src.utils.logger import logger

PROMPT = """
以下の質問に対して、適切な回答を生成してください。

{question}
"""


class ResponseModel(BaseModel):
    answer: str = Field(description="日本語で記述された回答")


if __name__ == "__main__":
    st.set_page_config(page_title="Simple Q&A App")
    st.title("Simple Q&A App")

    prompt_template = PromptTemplate.from_template(PROMPT)
    model = ChatOpenAI(model=settings.MODEL_NAME, temperature=0.3)
    chain = prompt_template | model.with_structured_output(ResponseModel)

    question = st.text_area("Input your question", height=100)

    if st.button("Generate response"):
        if question:
            with st.spinner("Generating response..."):
                input_data: dict[str, str] = {"question": question}
                response: ResponseModel = chain.invoke(input_data)  # type: ignore
                st.markdown(response.answer)

                log_info = {
                    "question": question,
                    "answer": response.answer,
                }
                logger.info(json.dumps(log_info))
