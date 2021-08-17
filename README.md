# titan_quest_skills_increaser
Automatic way to increase skill cap of skills, with increasing values of that skill

Requirements:
 1. Python 3.9 or higher

How to use:
 1. Run **python main.py**
 2. Write one or more path to the directory with .dbr skill-files (e.g. D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\skills)
 2.1. No single or double quotes!
   2.2. If you want use more than one path, the use ";" as delimiter
   2.2.1. For example:
     D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\skills;D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\xpack\skills;D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\xpack2\skills
 3. Write needed max level of skill, e.g 150
 4. Write needed ultimate level of skill (must be bigger or equal to max level), e.g. 200
 5. Write needed max level of masteries (must be bigger or equal to ultimate level), e.g. 500
 6. Press Enter and wait
 7. View changes in ArtManager
 8. Compile your mod

------------------------------------------------------------------------------------
Автоматическое увеличение максимального и ультимативного уровня всех навыков, с повышением всех тех значений навыка, которые требуются для его прогрессии.

Требования:
 1. Python 3.9 or higher

Как использовать:
1. Запустить скрипт командой **python main.py**
2. Указать один или несколько путей в директории с .dbr файлами навыков (пример: D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\skills)
  2.1. Путь не должен содержать одиночных или двойных кавычек!
  2.2. Если нужно указать несколько путей сразу, то используйте разделитель в виде точки-с-запятой ";"
  2.2.1. Например:
    D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\skills;D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\xpack\skills;D:\Mods\Titan Quest - Immortal Throne\Working\CustomMaps\Adventure_Hard\database\records\xpack2\skills
3. Впишите требуемый максимальный уровень навыка, например, 150
4. Впишите требуемый ультимативный уровень навыка, например, 200 (должен быть больше или равен максимальному уровню)
5. Впишите требуемый уровень мастерства, например, 500 (должен быть больше или равен ультимативному уровню)
6. Нажмите Enter и ждите
7. Просмотрите изменения через ArtManager
8. Скомпилируйте ваш мод
