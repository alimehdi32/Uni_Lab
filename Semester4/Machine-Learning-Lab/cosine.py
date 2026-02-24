import pandas as pd

documents = [
    "Machine learning is a powerful field of artificial intelligence where intelligent systems use data driven models and intelligent algorithms to learn from data.",
    
    "Deep learning is a specialized subset of machine learning where deep neural networks use large amounts of data for accurate prediction and intelligent decision making.",
    
    "Data science combines statistical methods, machine learning techniques, and advanced data visualization techniques to extract meaningful insights from complex data.",
    
    "Artificial intelligence includes intelligent applications such as robotics, natural language processing, and computer vision systems that solve complex real world problems.",
    
    "Neural networks are powerful learning models that learn complex patterns from large data sets and are widely used in modern deep learning systems."
]

common_words = [
    # Articles
    "a", "an", "the",
    
    # Be verbs
    "am", "is", "are", "was", "were", "be", "been", "being",
    
    # Helping verbs
    "do", "does", "did", "have", "has", "had",
    "will", "would", "shall", "should", "can", "could",
    "may", "might", "must",
    
    # Conjunctions
    "and", "or", "but", "nor", "so", "yet",
    "either", "neither", "because", "although", "though",
    
    # Prepositions
    "in", "on", "at", "by", "for","of", "with", "about",
    "against", "between", "into", "through", "during",
    "before", "after", "above", "below", "to", "from",
    "up", "down", "out", "over", "under",
    
    # Pronouns
    "i", "you", "he", "she", "it", "we", "they",
    "me", "him", "her", "us", "them",
    "my", "your", "his", "their", "our",
    
    # Other common words
    "this", "that", "these", "those",
    "there", "here",
    "what", "which", "who", "whom",
    "not", "no", "yes"
]

words_in_documents = {}

labels = ["d1", "d2", "d3", "d4", "d5"]
i=1
for doc in documents:
    unique_words={}
    for word in doc.split():
        if word.lower() not in common_words:
            unique_words[word.lower()] = unique_words.get(word.lower(), 0) + 1
    words_in_documents[f'd{i}'] = unique_words
    i += 1

sorted_dict = {}    
# print(words_in_documents)
for key, value in words_in_documents.items():
    sorted_dict[key] = dict(sorted(value.items(), key=lambda x: x[1], reverse=True)[:5])

# print(sorted_dict)

df = pd.DataFrame.from_dict(sorted_dict, orient='index').fillna(0)
# df = df.astype(int)
#df=df.reindex(labels)

# print(df)

# sorted_dict=dict(sorted(words_in_documents.items(), key=lambda item:item[1], reverse=True))
# print(sorted_dict)

most_freq={}
for colm in df.columns:
    df[colm] = df[colm].astype(int)
    counter=0
    for value in df[colm]:
        if value!=0:
            counter+=1
    most_freq[colm]=counter
# print(most_freq)


# sorted_dict=dict(sorted(most_freq.items(), key=lambda item:item[1], reverse=True))
# for word in common_words:
#     if word in sorted_dict:
#         del sorted_dict[word]
        
# print(sorted_dict)


# Get combined words from top 5 of each document

combined_words = set()

for doc in sorted_dict.values():
    for word in doc.keys():
        combined_words.add(word)

combined_words = sorted(list(combined_words))

print("Combined Words:")
print(combined_words)

combined_data = {}

for doc in sorted_dict:
    
    temp_dict = {}
    
    for word in combined_words:
        
        if word in sorted_dict[doc]:
            temp_dict[word] = sorted_dict[doc][word]
        else:
            temp_dict[word] = 0
            
    combined_data[doc] = temp_dict


combined_df = pd.DataFrame.from_dict(combined_data, orient='index')

print("\nCombined DataFrame:\n")
print(combined_df)

import math

def cosine_similarity(v1,v2):

    dot = 0
    norm1 = 0
    norm2 = 0
    
    for i in range(len(v1)):
        
        dot += v1[i]*v2[i]
        norm1 += v1[i]**2
        norm2 += v2[i]**2
        
    return dot/(math.sqrt(norm1)*math.sqrt(norm2))


docs = combined_df.index

cosine_matrix = pd.DataFrame(index=docs, columns=docs)

for d1 in docs:
    for d2 in docs:
        
        v1 = combined_df.loc[d1].values
        v2 = combined_df.loc[d2].values
        
        cosine_matrix.loc[d1,d2] = cosine_similarity(v1,v2)


print("\nCosine Similarity Matrix:\n")
print(cosine_matrix)