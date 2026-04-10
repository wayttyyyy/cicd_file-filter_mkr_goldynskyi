import pytest
from file_filter import get_filtered_lines, save_lines_to_file

# ФІКСТУРА: створює тимчасовий текстовий файл для тестів
@pytest.fixture
def sample_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    file_path.write_text("Apple\nBanana\nOrange\nGreen Apple\nGrape", encoding="utf-8")
    return str(file_path)

# ПАРАМЕТРИЗАЦІЯ: тестуємо пошук різних слів у файлі
@pytest.mark.parametrize("keyword, expected_count", [
    ("Apple", 2),   # 'Apple' та 'Green Apple'
    ("Banana", 1),
    ("Mango", 0)    # Такого слова немає
])
def test_get_filtered_lines(sample_file, keyword, expected_count):
    lines = get_filtered_lines(sample_file, keyword)
    assert len(lines) == expected_count

def test_save_lines_to_file(tmp_path):
    output_path = tmp_path / "filtered.txt"
    lines_to_save = ["Test line 1\n", "Test line 2\n"]
    
    save_lines_to_file(str(output_path), lines_to_save)
    
    content = output_path.read_text(encoding="utf-8")
    assert content == "Test line 1\nTest line 2\n"