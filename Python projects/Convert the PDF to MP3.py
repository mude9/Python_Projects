import pyttsx3
from PyPDF2 import PdfReader

pdf_path = r'D:\Mude\university application\university application木德\master/csu.pdf'
output_path = r'D:\Mude\university application\university application木德\master/csu.mp3'

pdfreader = PdfReader(open(pdf_path, 'rb')) # PDF reader
speaker = pyttsx3.init() # The text-to-speech engine

# Determine the total number of pages in the PDF
total_pages = len(pdfreader.pages) # Calculates the total number of pages in the PDF file

# Accept user input for the number of pages to be read
num_pages_to_read = int(input(f"Enter the number of pages to read (1-{total_pages}): "))
if num_pages_to_read < 1 or num_pages_to_read > total_pages:
    print(f"Invalid input. Please enter a number between 1 and {total_pages}.")
    exit()

# Set the speed of the TTS engine (adjust the rate as needed)
speaker.setProperty('rate', 170)  # You can experiment with different values to adjust the MP3 speed

full_text = ""
for page_num in range(num_pages_to_read):
    text = pdfreader.pages[page_num].extract_text() # extract the text from each page
    clean_text = text.strip().replace('\n', ' ') # text.strip means clean it by removing extra spaces and newlines
    full_text += clean_text + ' ' # concatenate it into a full_text variable.

speaker.save_to_file(full_text, output_path) # Safe full_text file to output_path and convert it to MP3 file
speaker.runAndWait() # the text-to-speech engine is run to convert the text into speech.

speaker.stop()

print(f"Number of pages in the PDF: {num_pages_to_read}")
print("Text-to-Speech engine speed: 170 words per minute (adjust as needed)")