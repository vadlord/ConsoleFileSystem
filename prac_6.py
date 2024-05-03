import os
import shutil
WORKDIR = "C:\\Users\\vadim\\PycharmProjects\\pythonProject5-6"

class CommandParser:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def parse_command(self, user_command):
        try:
            command_parts = user_command.split()
            if command_parts:
                command = command_parts[0]
                args = command_parts[1:]
                if hasattr(self.file_manager, command):
                    func = getattr(self.file_manager, command)
                    func(*args)
                else:
                    print("Неизвестная команда")
        except:

            print('Ошибка во время выполнении команды, читайте документацию (help)')


class FileManager:
    def __init__(self, workdir):
        self.workdir = workdir

    #Навигация по файловой системе внутри рабочей директории
    def cd(self, path):
        if path != '..':
            path_to_go = os.path.join(self.workdir, path)
        else:
            path_to_go = '\\'.join(str(self.workdir).split('\\')[:-1])

        if os.path.exists(path_to_go) and os.path.isdir(path_to_go):
            self.workdir = path_to_go
        else:
            print("Ошибка: директория не существует")

    #Создание новой папки (директории)
    def mkdir(self, dirname):
        path = os.path.join(self.workdir, dirname)
        if not os.path.exists(path):
            os.mkdir(path)
            print(f"Директория {dirname} создана")
        else:
            print("Ошибка: директория уже существует")

    #Удаление папки (директории)
    def rmdir(self, dirname):
        path = os.path.join(self.workdir, dirname)
        if os.path.exists(path) and os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Директория {dirname} удалена")
        else:
            print("Ошибка: директория не существует")

    #Создание нового файла
    def touch(self, filename):
        path = os.path.join(self.workdir, filename)
        if not os.path.exists(path):
            open(path, 'a').close()
            print(f"Файл {filename} создан")
        else:
            print("Ошибка: файл уже существует")

    #Чтение данных из файла
    def cat(self, filename):
        path = os.path.join(self.workdir, filename)
        if os.path.exists(path) and os.path.isfile(path):
            with open(path, 'r') as f:
                print(f.read())
        else:
            print("Ошибка: файл не существует")

    #Удаление файла
    def remove(self, filename):
        path = os.path.join(self.workdir, filename)
        if os.path.exists(path) and os.path.isfile(path):
            os.remove(path)
            print(f"Файл {filename} удален")
        else:
            print("Ошибка: файл не существует")

    #Копирование папки или файла в другую директорию
    def copy(self, src, dst):
        src_path = os.path.join(self.workdir, src)
        dst_path = os.path.join(self.workdir, dst)
        if os.path.exists(src_path):
            if os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path)
            else:
                shutil.copy2(src_path, dst_path)
            print(f"Скопировано из {src} в {dst}")
        else:
            print("Ошибка: источник не существует")

    #Перемещение файла в другую директорию
    def move(self, src, dst):
        src_path = os.path.join(self.workdir, src)
        dst_path = os.path.join(self.workdir, dst)
        if os.path.exists(src_path):
            shutil.move(src_path, dst_path)
            print(f"Перемещено из {src} в {dst}")
        else:
            print("Ошибка: источник не существует")

    #Переименование файла
    def rename(self, src, dst):
        src_path = os.path.join(self.workdir, src)
        dst_path = os.path.join(self.workdir, dst)
        if os.path.exists(src_path):
            os.rename(src_path, dst_path)
            print(f"Переименовано из {src} в {dst}")
        else:
            print("Ошибка: источник не существует")

    #Просмотр внутренности директории
    def ls(self):
        for item in os.listdir(self.workdir):
            print(item)

    #Запись в файл
    def write(self, filename, content):
        path = os.path.join(self.workdir, filename)
        with open(path, 'w') as f:
            f.write(content)
        print(f"Данные записаны в файл {filename}")

    def help(self):
        print('''
cd <path> - Навигация по файловой системе внутри рабочей директории
mkdir <dirname> - Создание новой папки (директории)
rmdir <dirname> - Удаление папки (директории)
touch <filename> - Создание нового файла
cat <filename> - Чтение данных из файла
remove <filename> - Удаление файла
copy <src> <dst> - Копирование папки или файла в другую директорию
move <src> <dst> - Перемещение файла в другую директорию
rename <src> <dst> - Переименование файла
ls - Просмотр внутренности директории
write <filename> <content> - Запись в файл
''')

workdir = WORKDIR
file_manager = FileManager(workdir)
parser = CommandParser(file_manager)
while True:
    command = input(f"{file_manager.workdir}> ")
    parser.parse_command(command)


