def get_filtered_lines(file_path: str, keyword: str) -> list:
    """Зчитує файл і повертає список рядків, що містять ключове слово."""
    filtered = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                filtered.append(line)
    return filtered