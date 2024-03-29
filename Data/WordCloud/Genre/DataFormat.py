import os
import re
from nltk.corpus import stopwords

# Ensure NLTK stopwords are downloaded
import nltk

nltk.download("stopwords")

# Define the directory where your files are located
directory = "."

# Define the directory where you want to save the processed files
output_directory = "./output"

# Load stopwords
stop_words = set(stopwords.words("english"))


# Function to remove stopwords and replace commas with spaces
def process_file(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        # Remove stopwords
        processed_text = " ".join(
            [word for word in text.split() if word.lower() not in stop_words]
        )
        # Replace commas with spaces
        processed_text = re.sub(r",", " ", processed_text)
        return processed_text


# Loop through each year from 2011 to 2020
for year in range(2011, 2021):
    filename = str(year) + ".txt"
    file_path = os.path.join(directory, filename)

    # Check if the file exists
    if os.path.exists(file_path):
        # Process the file
        processed_text = process_file(file_path)

        # Save processed text to a new file
        output_filename = str(year) + ".txt"
        output_file_path = os.path.join(output_directory, output_filename)

        with open(output_file_path, "w") as output_file:
            output_file.write(processed_text)

        print(f"Processed {filename}. Saved as {output_filename}")
    else:
        print(f"File {filename} does not exist.")
