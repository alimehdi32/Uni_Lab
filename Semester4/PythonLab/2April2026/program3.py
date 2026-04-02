'''
Write a program in python to create dict where key is programing language
and value is its popularity. Then perform
1. Ask the user to enter a language name and display its rank
2. List all the languages in alphabetical order
3. Print all the languages sorted by popularity
4. Print top 5 languages
'''


languages = {
    "Python": 1,
    "JavaScript": 2,
    "Java": 3,
    "C#": 4,
    "C++": 5,
    "Go": 6,
    "Rust": 7,
    "Kotlin": 8,
    "Swift": 9,
    "PHP": 10
}

lang = input("Enter a programming language: ")
if lang in languages:
    print("Rank:", languages[lang])
else:
    print("Language not found")

print(sorted(languages.keys()))

sorted_by_popularity = sorted(languages.items(), key=lambda x: x[1])
print(sorted_by_popularity)

top_5 = sorted_by_popularity[:5]
print(top_5)