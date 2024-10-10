from pathlib import Path
import argparse

def copy_and_sort_recursive(copy_from: Path, copy_to: Path) -> None:
    if copy_from.is_dir():
        for child in copy_from.iterdir():
            if child.is_dir():
                # Рекурсивная обработка
                copy_and_sort_recursive(child, copy_to)
            elif child.is_file():
                # Создаем директорию с названием расширения
                ext = child.suffix[1:]
                new_dir = copy_to / ext
                new_dir.mkdir(parents=True, exist_ok=True)

                # Создаем полный путь с именем файла
                new_path = new_dir / child.name
                try:
                    # Копируем
                    new_path.write_bytes(child.read_bytes())
                    print(f"Скопирован: {child} -> {new_path}")
                except Exception as e:
                    print(f"Ошибка при копировании {child}: {e}")

def main():
    ''' Для теста, например python3 task_1.py files NEW '''
    parser = argparse.ArgumentParser()
    parser.add_argument('copy_from', help='Исходная директория')
    parser.add_argument('copy_to', nargs='?', default='dist', help='Целевая директория')
    args = parser.parse_args()

    copy_from = Path(args.copy_from)
    copy_to = Path(args.copy_to)

    try:
        if not copy_from.is_dir():
            print(f"Ошибка: Исходная директория '{copy_from}' не существует.")
            return

        if not copy_to.is_dir():
            print(f"Целевая директория '{copy_to}' не существует. Создаем.")
            copy_to.mkdir(parents=True, exist_ok=True)

        print(f"Исходная директория: {copy_from}")
        print(f"Целевая директория: {copy_to}")

        copy_and_sort_recursive(copy_from, copy_to)

    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()