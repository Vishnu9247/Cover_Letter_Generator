import google.generativeai as genai
import os
from dotenv import load_dotenv
from Prompt_utils import prompt_content


def initiate_model():
    load_dotenv()
    api_key = os.getenv("GOOGLE_GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(model_name="gemini-2.0-flash")
    return model

def letter_body(resume, job_description, n_paras):
    model = initiate_model()
    prompt = prompt_content(resume, job_description, n_paras)
    response = model.generate_content(prompt)
    return response.text






#model_response("Data Science in simple terms")