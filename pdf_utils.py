import pypdf
from Prompt_utils import salutation_from, salutation_to, current_date, closing_saluation, greeting
from LLM_utils import letter_body



def pdf_extract(file_path):
    file = str(file_path)
    reader = pypdf.PdfReader(file)
    for page in reader.pages:
        text = page.extract_text()
        if text:
            return text
        else:
            print("No text found on this page.")


#resume = pdf_extract("resume_vishnu_vardhan_reddy_alla (5).pdf")
#print(resume)

def format_cover_letter(resume, job_description, name, address11, address12, address13, name2, designation, company, address21, address22, address23, n_paras):
    from_address = salutation_from(name, address11, address12, address13)
    to_address = salutation_to(name2, designation, company, address21, address22, address23)
    date = current_date()
    body = letter_body(resume, job_description, n_paras)
    closing = closing_saluation(name)
    greetings = greeting(name2)
    cover_letter = f"""{from_address}
    
{date}

{to_address}

{greetings}
{body}

{closing}"""

    return cover_letter


