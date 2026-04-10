def get_filtered_lines(file_path: str, keyword: str) -> list:
    """Зчитує файл і повертає список рядків, що містять ключове слово."""
    filtered = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                filtered.append(line)
    return filtered

def save_lines_to_file(file_path: str, lines: list):
    """Записує список рядків у вказаний файл."""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)