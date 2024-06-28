# XFolder by 1nfer.exe

XFolder позволяет отсортировать файлы ***согласно их расширению***. 

Что может ***XFolder***:
1. Сортировать файлы по расширению
	1. Рекурсивно (вместе с поддиректориями)
	2. Итеративно (только в конкретной папке)
2. Настраивать названия директорий, куда будут перемещены отсортированные файлы
3. Указывать какие файлы в какие папки сортировать
4. Настраивать расширения для сортировки, а также игнорирование определенных расширений

## ▶ Установка
Для установки клонируем репозиторий:
```
git clone https://github.com/InferKing/XFolder.git
```
создаем виртаульное окружение в папке, где находится проект:
```
python -m venv .venv
```
активируем виртуальное окружение:
```
source .venv/scripts/activate
```
устанавливаем необходимые зависимости:
```
pip install -r requirements.txt
```
готово!
## 🔸 Как использовать
### Основы
Используй команду <code>python main.py -h</code> в терминале для получения справки.

Для обычного запуска рекурсивной сортировки (вместе с поддиректориями) с заготовленной конфигурацией используется команда:
```
python main.py --path <ваш путь>
```
где <code><ваш путь></code> может быть совершенно любой: относительный или абсолютный.
Флаг <code>--path</code> необходим для указания пути до папки, где будет происходить сортировка. 

#### Пример использования разных путей

Сортировка по относительному пути
```
python main.py --path testfolder
```
Сортировка по абсолютному пути
```
python main.py --path C:\Users\user\Documents\folder
```
Если нужна текущая директория
```
python main.py --path .
```
Или более простой вариант
```
python main.py
```
### Настройка конфигурации

По умолчанию используется конфигурация из файла config.json. При желании можно изменить этот файл, либо использовать собственный. Для того, чтобы подключить собственный конфиг, необходимо использовать флаг <code>-c</code> или <code>--config</code>. 

Пример использования:
```
python main.py -c my_config.json
```
Обязательно указывайте в файле конфигурации поле **matches**. В нем содержится информация о расширениях, а также название папки, куда файлы с таким расширением попадут.
### Игнорирование расширений
По умолчанию игнорируются все файлы с расширением **.py**. Если необходимо указать большее количество расширений, которые нужно игнорировать, вы можете указать флаг <code>-i</code> или <code>--ignore</code>,  а затем указываете какие расширения необходимо игнорировать. 

К примеру, я хочу игнорировать все файлы с расширением **.pdf** и **.png**:
```
python main.py -i .pdf -i .png
```
P.S. В дальнейшем будет добавлена возможность указания игнорируемых расширений в файл конфигурации. Но а пока так :-)

Еще вы можете указать, что никакие расширения игнорировать не нужно, в таком случае необходимо указать флаг <code>--no-ignore</code>:
```
python main.py --path testfolder --no-ignore
```
В примере выше программа не будет игнорировать никакие файлы (кроме не указанных в конфигурационном файле). 
### Не трогаем поддиректории
Можно указать параметр <code>--no-recursive</code>, чтобы программа не проходила по поддиректориям целевой папки:
```
python main.py --path testfolder --no-recursive
```
Актуальные флаги всегда находятся в <code>--help</code>, помните это!
