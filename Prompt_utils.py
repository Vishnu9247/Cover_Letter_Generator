from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import ChatPromptTemplate
import datetime


def salutation_from(name, address1, address2, address3):
    # name = input("Please Enter Your Name to display:")
    # print("Enter your address in max 3 lines")
    # address1 = input("Please Enter your 1st line of address:")
    # address2 = input("Please Enter your 2nd line of address:")
    # address3 = input("Please Enter your 3rd line of address:")

    lines = [name, address1, address2, address3]
    return "\n".join(line for line in lines if line.strip())

# temp = salutation_from()
# print(temp)

def salutation_to(name, designation, company, address1, address2, address3):
    # name = input("Please enter the recipient's name (e.g., Hiring Manager or specific name): ")
    # designation = input("Please enter the recipient's designation (e.g., HR Manager, Team Lead): ")
    # company = input("Please enter the company name: ")
    # print("Enter the company address in max 3 lines")
    # address1 = input("Enter 1st line of company address: ")
    # address2 = input("Enter 2nd line of company address: ")
    # address3 = input("Enter 3rd line of company address: ")

    header = ", ".join(part for part in [designation, company] if part.strip())
    lines = [name, header, address1, address2, address3]
    return "\n".join(line for line in lines if line.strip())

# temp2 = salutation_to()
# print(temp2)

def current_date():
    today = datetime.datetime.now().date()
    formatted_date = f"{today.strftime('%B')} {today.day}, {today.year}"
    return formatted_date

# print(current_date())

def prompt_content(resume, job_description, n_paras):
    prompt = f"""
    You are an expert cover letter writer.

    Your task is to write **only the body paragraphs** of a professional cover letter — **do NOT include** any greeting (like "Dear...") or closing (like "Sincerely," or a name).

    ONLY return the content **between** the greeting and the sign-off. Do NOT include any salutation or sign-off line at all.

    Here is the resume:
    {resume}

    Here is the job description:
    {job_description}

    Write the body paragraphs that clearly align the candidate's skills and experience with the job.
    Do not include any extra lines. Only output the main paragraph content.
    Write it in {n_paras} paragraphs.
    """

    # prompt_template = ChatPromptTemplate.from_messages(messages)
    # prompt = prompt_template.invoke({"resume": resume, "job_description": job_description})
    return prompt

# print(prompt_content("Vishnu Alla's resume", "data Scientist"))

def closing_saluation(name):
    # name = input("Enter your name:")
    salutation = f"Sincerely,\n{name}"
    return salutation

# print(closing_saluation())

def greeting(name):
    return f"Dear {name if name.strip() else 'Hiring Manager'},"


