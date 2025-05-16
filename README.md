# 📄 AI-Powered Cover Letter Generator

This project is an AI-based **Cover Letter Generator** built using **Streamlit** and **Gemini (Google Generative AI)**. It automatically crafts a personalized cover letter based on your resume and a job description using LLMs.

Users can preview, edit, and export the generated cover letter in **PDF** or **Word** format — all within an intuitive interface.

---

## 🚀 Features

✅ Upload your **Resume (PDF)**  
✅ Paste the **Job Description**  
✅ Enter your personal and recruiter’s details  
✅ Choose number of paragraphs in the cover letter  
✅ Generate a high-quality, professional cover letter using **Gemini AI**  
✅ **Editable preview** for fine-tuning tone or grammar  
✅ Export your final letter as a **PDF or Word document**

---

## 🧠 How It Works

1. **Resume Parsing** – Extracts text from your uploaded resume.
3. **Gemini LLM** – Uses Google’s Gemini model to intelligently craft a tailored cover letter.  
3. **Prompt Utilities** – Dynamically generate sender/receiver salutation, date, greetings, and a closing signature.  
4. **Live Editor** – Allows you to review and fine-tune the cover letter before downloading.  
5. **Export Engine** – Save the letter in DOCX or PDF (with proper formatting and spacing).

---

## 📥 Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Vishnu9247/Cover_Letter_Generator
cd cover-letter-generator
```

### 2. Get Gemini API Key
Visit Google Gemini API Key Page

Generate your API Key

⚠️ Use a personal Gmail account — some organizational emails may not work

### 3. Create a .env file
Inside the root directory of your project:

Add the following line to your .env file:

``` bash
GOOGLE_GEMINI_API_KEY=your_api_key_here
```
### 4. Install Dependencies
``` bash
pip install -r requirements.txt
 ```
### 5. Run the Application
```bash
streamlit run main.py
```
The app will open in your browser at: http://localhost:8501

---

## 🖊️ How to Use

Input Fields:
Your Name & Address (Appears in the “From” section)

Recruiter Details (Name, Designation, Company, and Address)

Resume (PDF) – Upload your updated resume

Job Description – Paste the full job description

Number of Paragraphs – Choose how detailed you want the letter to be

Editable Preview:
After clicking “Generate Cover Letter”, the generated letter appears in a text area.

Make any custom edits (fix wording, add content, remove white spaces).

This edited version is what will be exported.

Export Options:
Choose between:

✅ Word (.docx) – Good for further editing in Microsoft Word

✅ PDF (.pdf) – Properly formatted for printing and submissions

PDFs are exported in A4 size, Times New Roman 11pt, and standard margins for a clean, professional look.

---

## 📎 Tech Stack

Python 3.9+

Streamlit

Google Generative AI (Gemini)

PyPDF

FPDF

python-docx

---

## 🛠 Troubleshooting
If Gemini API key isn’t working, try logging in with a personal Gmail account instead of a work/school email.

Make sure your resume PDF is readable (not scanned image-only).

On PDF export issues, ensure your system supports the Times New Roman font.

