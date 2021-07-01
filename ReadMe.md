# Алгоритмы поиска на графах на примере игры Pacman
Источник: https://inst.eecs.berkeley.edu/~cs188/fa18/project1.html

В данном проекте агент Pacman с помощью алгноритмов поиска на графах проходит лабиринт и эффективно собирает по пути еду.

### Структура файлов

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
* `testClasses.py`  General autograding test classes
* *test_cases/*   Directory containing the test cases for each question
* `searchTestClasses.py`    Project 1 specific autograding test classes

### Инструкция
Поиграть в Pacman можно, набрав в терминале:

```bash
python3 pacman.py
```
Eсли Pacman застрял, вы можете выйти нажав CTRL-C в вашем терминале.

Проверить корректность работы агента поиска можно, запустив:
```bash
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch
```
Данная команда говорит агенту поиска использовать алгоритм поиска tinyMazeSearch, который реализован а `search.py`. Pacman должен пройти лабиринт успешно.

### Алгоритм поиска в глубину (DFS)  

```bash
python3 pacman.py -l mediumMaze -p SearchAgent
```  
![pacman_dfs](media/pacman_dfs_x2.gif)  


**Примечание.** Опция *-l* задает тип лабиринта:  
* tinyMaze - маленький;
* mediumMaze - средний;
* bigMaze - большой.  
Полный список опций можно увидеть, набрав в терминале:  
```bash
python3 pacman.py -h
```

### Поиск в Ширину (BFS)  

```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```  
![pacman_bfs](media/pacman_bfs_x2.gif)  

### Алгоритм Uninformed cost search (UCS)  

Простой лабиринт:
```bash
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
```  
![pacman_ucs](media/pacman_ucs_x2.gif)  
Лабиринт с едой:
```bash
python3 pacman.py -l mediumDottedMaze -p StayEastSearchAgent
```  
![pacman_ucs_food](media/pacman_ucs_food_x2.gif)  
Лабиринт с призраками:
```bash
python3 pacman.py -l mediumScaryMaze -p StayWestSearchAgent
```  
![pacman_ucs_ghosts](media/pacman_ucs_ghosts_x2.gif)  

### Алгоритм A*  
Запуск реализации алгоритма A*  для решения задачи поиска пути, используя эвристику Манхеттоновское расстояние, осуществляется командой:
```bash
python3 pacman.py -l mediumMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```  
![pacman_astar](media/pacman_astar_x2.gif)  
