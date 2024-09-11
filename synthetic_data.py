import csv
import random
from faker import Faker

fake = Faker()

# Function to generate a more intricate random sentence
def generate_sentence():
    # Create a basic sentence using Faker
    sentence = fake.sentence()
    
    # Introduce random noise (incorrect capitalization, punctuation errors)
    if random.random() < 0.2:
        sentence = sentence.lower() if random.random() < 0.5 else sentence.upper()

    # Introduce a chance for a random typo or character swap
    if random.random() < 0.1:
        sentence = list(sentence)
        if len(sentence) > 2:
            i = random.randint(1, len(sentence) - 2)
            sentence[i], sentence[i+1] = sentence[i+1], sentence[i]
        sentence = ''.join(sentence)
    
    # Add random periods or commas in strange places
    if random.random() < 0.05:
        sentence = sentence.replace(" ", ". ", 1)  # Random period after first word
    
    return sentence

# Function to generate a paragraph with 3-7 intricate sentences
def generate_paragraph():
    return " ".join(generate_sentence() for _ in range(random.randint(3, 7)))

# Function to generate a more detailed conversation (up to 4 lines)
def generate_conversation():
    num_people = random.randint(2, 4)
    conversation = "\n".join(f"Person {i+1}: {generate_sentence()}" for i in range(num_people))
    return conversation

# Function to generate a random sentence with a name, date, or random event
def generate_special_sentence():
    # Randomly choose to insert a name, date, or random event
    special_type = random.choice(['name', 'date', 'event'])
    
    if special_type == 'name':
        return f"{fake.name()} said: {generate_sentence()}"
    elif special_type == 'date':
        return f"On {fake.date()}, {fake.name()} wrote: {generate_sentence()}"
    elif special_type == 'event':
        return f"At the {fake.company()} event, {generate_sentence()}"

# Function to generate one line of synthetic text data with varied complexity
def generate_row():
    text_type = random.choice(['sentence', 'paragraph', 'conversation', 'special'])
    
    if text_type == 'sentence':
        return [generate_sentence()]
    elif text_type == 'paragraph':
        return [generate_paragraph()]
    elif text_type == 'conversation':
        return [generate_conversation()]
    elif text_type == 'special':
        return [generate_special_sentence()]

# Create CSV file with 1 million rows
def generate_csv(file_name, num_rows):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Text"])  # Writing the header

        for _ in range(num_rows):
            writer.writerow(generate_row())

# Generate 1,000,000 rows of synthetic text and save it to a CSV file
generate_csv('intricate_synthetic_text_data.csv', 1000000)

print("CSV file with 1,000,000 rows of intricate synthetic text data has been generated.")
