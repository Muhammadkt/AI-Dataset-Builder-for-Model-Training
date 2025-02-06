import os

def generate_summary():
    base_dir = "curated_code"
    languages = ["python", "javascript", "c_cpp", "java"]
    summary = {}
    
    for lang in languages:
        lang_dir = os.path.join(base_dir, lang)
        files = [f for f in os.listdir(lang_dir) if f.endswith((".py", ".js", ".cpp", ".java"))]
        summary[lang] = len(files)
    
    print("Dataset Summary:")
    for lang, count in summary.items():
        print(f"{lang.capitalize()}: {count} files")

if __name__ == "__main__":
    generate_summary()
