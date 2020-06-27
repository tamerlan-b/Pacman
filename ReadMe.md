### Алгоритмы поиска на графах
Источник: https://inst.eecs.berkeley.edu/~cs188/fa18/project1.html

В этом проекте агент Pacman должен найти все пути через лабиринт, чтобы добраться до определенного места и эффективно собрать еду. Задача создать общие алгоритмы поиска и применить их к Pacman.

![Pacman](media/pacman_ghosts.png)

##### Структура файлов

Файлы, которые были изменены мной:
* `search.py`   Файл, где находятся все алгоритмы поиска
* `searchAgents.py` - находятся агенты основанные на поиске

Файлы, на которые стоит посмотреть:
* `pacman.py` Основной файл запускающий игру Pacman. Данный файл описывает Состояние среды  Pacman, которое используется в проекте  
* `game.py` Логика, как работает мир Pacman. Данный файл описывает несколько вспомогательных типов, таких как AgentState, Agent, Direction, и Grid.
* `util.py` Полезные структуры данных для имплементации алгоритма поиска

Вспомогательные файлы, которые можно проигнорировать:
* `graphicsDisplay.py`  Графика Pacman
* `graphicsUtils.py`    Вспомогательный файл для графики Pacman graphics
* `textDisplay.py`  ASCII графика Pacman
* `ghostAgents.py`  Агенты для управления призраками
* `keyboardAgents.py`   Интерфейс клавиатуры для управления Pacman
* `layout.py`   Код для чтения файлов и сохранения их содержимого
* `autograder.py`   Project autograder
* `testParser.py`   Parses autograder test and solution files
* `testParser.py`  General autograding test classes
* *test_cases/*   Directory containing the test cases for each question
* `searchTestClasses.py`    Project 1 specific autograding test classes

##### Инструкция
Поиграть в Pacman можно, набрав в терминале:

```bash
python3 pacman.py
```

Самый простой Агент в `searchAgents.py` называется GoWestAgent, который всегда идет на запад.
```bash
python3 pacman.py --layout testMaze --pacman GoWestAgent
```
```bash
python3 pacman.py --layout tinyMaze --pacman GoWestAgent
```

Eсли Pacman застрял, вы можете выйти нажав CTRL-C в вашем терминале.

Скрипт `pacman.py`  поддерживает ряд опций, которые можно увидеть выполнив команду:

```bash
python3 pacman.py -h
```

Проверить корректность работы агента поиска можно, запустив:
```bash
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```
Данная команда говорит агенту поиска использовать алгоритм поиска tinyMazeSearch, который реализован а `search.py`. Pacman должен пройти лабиринт успешно.

##### Алгоритм поиска в глубину (DFS)

Для маленького лабиринта:
```bash
python3 pacman.py -l tinyMaze -p SearchAgent
```
Для среднего:
```bash
python3 pacman.py -l mediumMaze -p SearchAgent
```
Для большого:
```bash
python3 pacman.py -l bigMaze -z .5 -p SearchAgent
```

##### Поиск в Ширину (BFS)

Для среднего лабиринта:
```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
Для большого:
```bash
python3 pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```

##### Алгоритм Uninformed cost search (UCS)

Простой лабиринт среднего размера:
```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```
Лабиринт с едой:
```bash
python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```
Лабиринт с призраками:
```bash
python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```

##### Алгоритм A*
Запуск реализации алгоритма A*  для решения задачи поиска пути, используя эвристику Манхеттоновское расстояние, осуществляется командой:
```bash
python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
