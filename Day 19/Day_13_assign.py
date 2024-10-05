import re

def replace_dates(text):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'

    def replace_match(match):
        year, month, day = match.groups()
        return f'{day}/{month}/{year}'
    
    updated_text = re.sub(pattern, replace_match, text)
    
    return updated_text

if __name__ == "__main__":
    sample_text = """My birth date is 2002/02/16    """

    result = replace_dates(sample_text)
    print("Original Text:")
    print(sample_text)
    print("\nUpdated Text:")
    print(result)

 