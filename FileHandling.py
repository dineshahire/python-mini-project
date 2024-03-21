import csv
import os
import matplotlib.pyplot as plt

# Function to read text from a file
def read_text_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# Function to write text to a file
def write_text_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Function to parse CSV file and return data as a list of dictionaries
def parse_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Function to analyze data and plot a graph
def analyze_data(data):
    categories = []
    values = []
    for row in data:
        categories.append(row['Category'])
        values.append(int(row['Value']))

    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Data Analysis')
    plt.show()

# Main function
def main():
    # File paths
    text_file = 'sample_text.txt'
    csv_file = 'sample_data.csv'

    # Sample text data
    text_data = "This is a sample text file.\nIt contains some text data for demonstration purposes."

    # Sample CSV data
    csv_data = [
        {'Category': 'A', 'Value': '10'},
        {'Category': 'B', 'Value': '20'},
        {'Category': 'C', 'Value': '15'}
    ]

    # Write text to a file
    write_text_file(text_file, text_data)

    # Read text from a file
    read_text = read_text_file(text_file)
    print("Text read from file:")
    print(read_text)

    # Write CSV data to a file
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=['Category', 'Value'])
        csv_writer.writeheader()
        csv_writer.writerows(csv_data)

    # Parse CSV file
    parsed_data = parse_csv_file(csv_file)
    print("\nParsed CSV data:")
    for row in parsed_data:
        print(row)

    # Analyze data and plot graph
    analyze_data(parsed_data)

# Entry point of the application
if __name__ == "__main__":
    main()
