import os
import tkinter as tk
from tkinter import filedialog
from TextUnionParser.MessageBox import MessageBox
from TextUnionParser.DocumentAnalyzer import DocumentAnalyzer


def select_file():
    """Открывает диалог выбора файла и возвращает путь к выбранному файлу и его директорию."""
    root = tk.Tk()
    root.withdraw()  # Скрыть главное окно
    file_path = filedialog.askopenfilename(title="Выберите файл", filetypes=[("Word Documents", "*.docx")])
    directory = os.path.dirname(file_path) if file_path else None
    return file_path, directory


class MainProcess:
    def __init__(self, input_file, benefits_file, output_file):
        self.input_file = input_file
        self.benefits_file = benefits_file
        self.output_file = output_file

    def run(self):
        """Запуск основного процесса анализа документа."""
        analyzer = DocumentAnalyzer(self.input_file, self.benefits_file)
        analyzer.analyze_benefits()
        analyzer.create_report(self.output_file)


# Основной процесс
if __name__ == "__main__":
    # Запрос пути к файлу у пользователя
    file_path, directory = select_file()

    if file_path:
        # Запрос файла с льготами
        benefits_file = filedialog.askopenfilename(title="Выберите файл с льготами",
                                                   filetypes=[("JSON Files", "*.json")])

        if benefits_file:
            output_file = os.path.join(directory, "report.docx")  # Сохраняем отчет в той же директории

            # Создание и запуск основного процесса
            main_process = MainProcess(file_path, benefits_file, output_file)
            main_process.run()
        else:
            MessageBox.show_warning("Файл с льготами не был выбран.")
    else:
        MessageBox.show_warning("Файл не был выбран.")
