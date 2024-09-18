def clean_text(raw_text):
    lines = raw_text.split('\n')
    lines = [line.strip() for line in lines if line.strip()]
    lines = [line for line in lines if len(line) > 2]
    cleaned_text = '\n'.join(lines)
    return cleaned_text
