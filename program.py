import re
from collections import Counter

def read_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


amharic_text = read_text('amharic_text.txt')
tigrigna_text = read_text('tigrigna_text.txt')

# print("Amharic Text:", amharic_text)
# print("Tigrigna Text:", tigrigna_text)

def clean_text(text):
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip()


cleaned_amharic = clean_text(amharic_text)
cleaned_tigrigna = clean_text(tigrigna_text)

# print("Cleaned Amharic Text:", cleaned_amharic)
# print("Cleaned Tigrigna Text:", cleaned_tigrigna)


def count_words(text):
    words = text.split()
    return Counter(words)

amharic_freq = count_words(cleaned_amharic)
tigrigna_freq = count_words(cleaned_tigrigna)

# print("Amharic Word Frequency:", amharic_freq)
# print("Tigrigna Word Frequency:", tigrigna_freq)

def word_overlap(freq1, freq2):
    common_words = set(freq1.keys()).intersection(set(freq2.keys()))
    return len(common_words), common_words

overlap_count, common_words = word_overlap(amharic_freq, tigrigna_freq)

# print("Word Overlap Count:", overlap_count)
# print("Common Words:", common_words)

def g2p(text):
    return text.split() 

amharic_phonemes = g2p(cleaned_amharic)
tigrigna_phonemes = g2p(cleaned_tigrigna)

# print("Amharic Phonemes:", amharic_phonemes)
# print("Tigrigna Phonemes:", tigrigna_phonemes)

def phoneme_distribution(phonemes):
    return Counter(phonemes)

amharic_phoneme_dist = phoneme_distribution(amharic_phonemes)
tigrigna_phoneme_dist = phoneme_distribution(tigrigna_phonemes)

# print("Amharic Phoneme Distribution:", amharic_phoneme_dist)
# print("Tigrigna Phoneme Distribution:", tigrigna_phoneme_dist)

def phoneme_overlap(dist1, dist2):
    common_phonemes = set(dist1.keys()).intersection(set(dist2.keys()))
    return len(common_phonemes), common_phonemes

phoneme_overlap_count, common_phonemes = phoneme_overlap(amharic_phoneme_dist, tigrigna_phoneme_dist)

print("Phoneme Overlap Count:", phoneme_overlap_count)
print("Common Phonemes:", common_phonemes)


