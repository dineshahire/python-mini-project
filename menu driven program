import os
import requests
import PyPDF2

def file_handling():
    print("File Handling Menu:")
    print("1. Create a new file")
    print("2. Read a file")
    print("3. Write to a file")
    choice = input("Enter your choice: ")

    if choice == "1":
        filename = input("Enter the name of the file to create: ")
        with open(filename, 'w') as f:
            pass  # Just creating an empty file
        print(f"File '{filename}' created successfully.")
    elif choice == "2":
        filename = input("Enter the name of the file to read: ")
        try:
            with open(filename, 'r') as f:
                print("File content:")
                print(f.read())
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
    elif choice == "3":
        filename = input("Enter the name of the file to write to: ")
        data = input("Enter data to write to the file: ")
        with open(filename, 'w') as f:
            f.write(data)
        print("Data written to the file successfully.")
    else:
        print("Invalid choice")

def web_scanning():
    url = input("Enter the URL to scan: ")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Website is accessible.")
        else:
            print("Website is not accessible.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

def pdf_reader():
    filename = input("Enter the name of the PDF file to read: ")
    try:
        with open(filename, 'rb') as f:
            pdf_reader = PyPDF2.PdfFileReader(f)
            num_pages = pdf_reader.numPages
            print(f"Number of pages in PDF: {num_pages}")
            for page_num in range(num_pages):
                page = pdf_reader.getPage(page_num)
                text = page.extractText()
                print(f"Page {page_num + 1}:")
                print(text)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except PyPDF2.utils.PdfReadError:
        print(f"File '{filename}' is not a valid PDF.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. File Handling")
        print("2. Web Scanning")
        print("3. PDF Reader")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            file_handling()
        elif choice == "2":
            web_scanning()
        elif choice == "3":
            pdf_reader()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
