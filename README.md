# Цветовое смещение картинок

Скрипт для цветового смещения RGB картинок, например для создания аватарок.
Программа смещает красный канал влево, синий вправо, а зеленый оставляет как есть.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip3` для установки зависимостей:
```
pip install pillow
```
В main.py необходимо указать путь до исходной картинки, пути или названия для получившейся картинки, полноценной и thumbnail 80x80. 
Для изменения "силы" смещения, необходимо изменить значение переменной CROP_SIZE.

### Как запустить
Скрипт запускается из консоли
```shell
foo@bar ~ % python main.py 
Смещенная картинка сохранена в out.jpg
Превью смещенной картинки сохранено в out_thumbnail.jpg
```
### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).