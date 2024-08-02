# Ethiopian Language Text Processing

This project involves text processing for two Ethiopian languages, Amharic and Tigrigna. The main tasks include text cleaning, word and phoneme frequency analysis, and comparison of word and phoneme overlaps between the two languages.

## Project Overview

1. **Text Reading**: Load Amharic and Tigrigna text files.
2. **Text Cleaning**: Remove non-phonetic characters from the text.
3. **Word Frequency Analysis**: Count the frequency of unique words in each language.
4. **Word Overlap Analysis**: Compute the overlap of words between the two languages.
5. **Phoneme Transcription**: Transcribe the text into phonemes (currently simulated).
6. **Phoneme Distribution Analysis**: Count the frequency of phonemes in each language.
7. **Phoneme Overlap Analysis**: Compute the overlap of phonemes between the two languages.

## Setup and Installation

**Clone the Repository:**

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

## Usage

1. **Prepare Your Text Files:**

    - Ensure `amharic_text.txt` and `tigrigna_text.txt` are available in the project directory.

2. **Run the Script:**

    Execute the script using Python:

    ```bash
    python program.py
    ```

    This will perform text processing tasks and print the results to the console.

## Script Overview

### `read_text(file_path)`

Reads text from a specified file.

### `clean_text(text)`

Cleans the text by removing non-phonetic characters.

### `count_words(text)`

Counts the frequency of each word in the text.

### `word_overlap(freq1, freq2)`

Calculates the overlap of words between two frequency dictionaries.

### `g2p(text)`

Simulated grapheme-to-phoneme conversion (replace with actual implementation).

### `phoneme_distribution(phonemes)`

Counts the frequency of each phoneme.

### `phoneme_overlap(dist1, dist2)`

Calculates the overlap of phonemes between two distribution dictionaries.

## Example Output

The script will output:

- **Word Overlap Count**: The number of common words between Amharic and Tigrigna texts.
- **Common Words**: A list of words that appear in both texts.
- **Phoneme Overlap Count**: The number of common phonemes between Amharic and Tigrigna texts.
- **Common Phonemes**: A list of phonemes that appear in both texts.

## Contact

For questions or feedback, please contact [tadekaldas1992@gmial.com].
