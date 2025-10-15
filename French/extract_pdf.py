import fitz  # PyMuPDF
import re

# PDF file path
pdf_path = r"c:\\Users\\muhammadahmad4\\ahmad\\fastapi\\New folder\\1-8th-Semester\\French\\French_till_6_10_2025.pdf"

# Extract text from PDF
text_content = ""
try:
    pdf_document = fitz.open(pdf_path)
    print(f"Total pages: {len(pdf_document)}")
    
    for page_num in range(len(pdf_document)):
        print(f"Extracting page {page_num + 1}...")
        page = pdf_document[page_num]
        page_text = page.get_text()
        
        if page_text.strip():
            text_content += f"\n\n=== PAGE {page_num + 1} ===\n\n"
            text_content += page_text
    
    pdf_document.close()
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()

# Save extracted text
output_file = r"c:\\Users\\muhammadahmad4\\ahmad\\fastapi\\New folder\\1-8th-Semester\\French\\extracted_text.txt"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(text_content)

print(f"\nText extracted successfully!")
print(f"Total characters: {len(text_content)}")
print(f"Output saved to: {output_file}")

# Print first 500 characters as preview
if text_content:
    print("\n=== PREVIEW ===")
    print(text_content[:500])
