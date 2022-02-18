import pyttsx3
import PyPDF2

with open("sample.pdf", "rb") as f:
    pdf_reader = PyPDF2.PdfFileReader(f)
    pages = pdf_reader.numPages
    engine = pyttsx3.init()
    for i in range(pages):
        # your custom text
        msg = f"I am reading the page number {i} for you"
        engine.say(msg)
        engine.runAndWait()
        # text from the book
        page = pdf_reader.getPage(i)
        text = page.extractText()
        engine.save_to_file(text, f"page_{i:03d}.mp3")
        engine.runAndWait()
