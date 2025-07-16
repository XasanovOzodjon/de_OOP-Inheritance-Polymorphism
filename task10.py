class Document:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_preview(self):
        print(f"Title: {self.title}\nContent: {self.content}")
        
class PdfDocument(Document):
    def print_preview(self):
        print(f"PDF Title: {self.title}\nPDF Content: {self.content}")
        
        
class WordDocument(Document):
    def print_preview(self):
        print(f"Word Title: {self.title}\nWord Content: {self.content}")
        
        
def main():
    pdf_doc = PdfDocument(title="Python OOP", content="OOP Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    word_doc = WordDocument(title="Python Basics", content="Word Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    pdf_doc.print_preview()
    word_doc.print_preview()
    
if __name__ == "__main__":
    main()