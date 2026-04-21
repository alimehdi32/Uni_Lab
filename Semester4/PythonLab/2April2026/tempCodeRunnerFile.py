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