# Linguistic Fabricator: Synthetic Text Data for NLP

## Summary

The **Linguistic Fabricator** project focuses on generating synthetic text data designed to mimic various linguistic patterns and styles. This dataset serves as a valuable resource for a range of natural language processing (NLP) tasks including model training, sentiment analysis, language generation, and translation models. By creating diverse and intricate text data, the project aims to provide a robust dataset that helps in evaluating and improving NLP models.

The dataset comprises one million lines of synthetic text, with each entry crafted to include various linguistic constructs and styles. This approach helps in testing NLP models under different conditions and simulating real-world text processing scenarios. The dataset is designed to be used for training language models, evaluating text generation algorithms, and developing other NLP applications.

## Dataset

[![Download Dataset](https://img.shields.io/badge/Download%20Dataset-Kaggle-blue)](https://www.kaggle.com/datasets/yajkotak/linguistic-fabricator-synthetic-text-data-for-nlp/data)

The synthetic text dataset used in this project is available for download on Kaggle. You can access it using the link above.

Note: You will need a Kaggle account to download the dataset.

## Working

### Data Generation

The synthetic text data was generated using a combination of linguistic rules and random noise. The process involved the following steps:

1. **Text Generation**: Random sentences and paragraphs were created using a set of predefined linguistic rules to simulate various writing styles. This included varying sentence structures, vocabulary usage, and syntactic patterns.
   
2. **Error Simulation**: To make the dataset more realistic, random linguistic errors were introduced. These errors mimic common typing mistakes, grammatical errors, and syntactical anomalies.

3. **Formatting**: The generated text was structured into columns and saved in a CSV format. Each row in the CSV file represents a line of synthetic text.

4. **Size and Complexity**: The dataset contains one million lines of text, with careful attention to the complexity and variety of the data to ensure its utility for different NLP tasks.

### Example

To use the dataset, simply download it from [Kaggle](https://www.kaggle.com/datasets/yajkotak/linguistic-fabricator-synthetic-text-data-for-nlp/data) and load it into your preferred data analysis or NLP tool. Here's a basic example of how to use the dataset with Python:

```python
import pandas as pd

# Load the synthetic text data
file_path = 'path_to_your_downloaded_file/intricate_synthetic_text_data.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print(data.head())

# Example of text data usage
# Let's perform a simple analysis to count the number of sentences per line
data['sentence_count'] = data['text'].apply(lambda x: len(x.split('.')))
print(data[['text', 'sentence_count']].head())
```
In this example, we load the dataset into a Pandas DataFrame, display the first few rows, and perform a basic analysis to count the number of sentences per line.

## Applications
The dataset can be used for various NLP tasks, including:

1. **Model Training**: Train language models on synthetic data to simulate different text patterns and styles.

2. **Sentiment Analysis**: Evaluate sentiment analysis models by testing them on data with varying linguistic errors and styles.

3. **Language Generation:** Use the data to fine-tune text generation models and assess their ability to produce diverse and coherent text.

4. **Translation Models:** Test translation models on synthetic text to evaluate their performance in handling different linguistic structures.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, you can reach me through the following methods:

  <a href="https://www.linkedin.com/in/yajkotak" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Yaj_Kotak-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
  </a>
