# Завдання 1.

* Функція *reverse_list* здатна реверсувати однозв'язний список, змінюючи посилання між вузлами. Після виклику цієї функції елементи списку розташовані у зворотньому порядку.
* Алгоритм *insertion_sort* сортує елементи однозв'язного списку за зростанням значень. Після виклику елементи списку впорядковані.
* Функція *merge_sorted_lists* об'єднує два відсортовані однозв'язні списки в один відсортований список.

# Завдання 2.

Програма візуалізує фрактал *"дерево Піфагора"* за допомогою рекурсії. Користувач може вказати рівень деталізації.

#### Приклад рівня рекурсії 8
![pythagorean_tree](/pythagorean_tree.png "Дерево")

# Завдання 3.

Реалізовано алгоритм Дейкстри для пошуку найкоротших шляхів у графі з використанням бінарної купи. Програма дозволяє знаходити вартість найкоротших реальних маршрутів від заданої вершини(вулиці Танкопія) до всіх інших вулиць міста Харкова у графі. Графічне відображення дозволяє візуалізувати зв'язки між вершинами та їх ваги.

![kh_map](/kh_map.png "Харків")

#### Вартість найкоротших шляхів від вершини Tankopiya:
* Вершина Kharkivskykh Dyvizii: сумарний час - 2
* Вершина Oleksandrivskyj: сумарний час - 5
* Вершина Heroiv Kharkova: сумарний час - 5 
* Вершина 12-ho Kvitnya: сумарний час - 9
* Вершина Pavlivska Square: сумарний час - 19
* Вершина Louis Pasteur: сумарний час - 15
* Вершина Poltavskyi Shliakh: сумарний час - 24
* Вершина Sumska: сумарний час - 26
* Вершина Nauky: сумарний час - 30


# Завдання 4.

Реалізовано функцію для візуалізації бінарної купи. 

![heap](/heap.png "Купа")

# Завдання 5.

Програма візуалізує обходи бінарного дерева у глибину та в ширину.

![dfs](/dfs.png "Dfs")

![bfs](/bfs.png "Bfs")

# Завдання 6.

Програма розв'язує задачу вибору страви з найбільшою сумарною калорійністю в межах обмеженого бюджету, використовуючи два різні підходи — жадібний алгоритм та алгоритм динамічного програмування.

Жадібний алгоритм вибирає страви, максимізуючи співвідношення калорій до вартості, і надає гарний результат за прийнятний час виконання. Цей метод швидкий і ефективний, але може не завжди забезпечити абсолютно оптимальний вибір.

Алгоритм динамічного програмування використовує динамічне програмування для знаходження оптимального набору страв для максимізації калорійності при заданому бюджеті. Цей метод гарантує знаходження оптимального рішення, проте може вимагати більше обчислювальних ресурсів.

#### Результати

`items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}`

Бюджет = 100

*Жадібний алгоритм:*
* Обрані страви: ['cola', 'potato', 'pepsi', 'hot-dog']
* Калорійність: 870
* Фінальні витрати: 80

*Алгоритм динамічного програмування:*
* Обрані страви: ['pizza', 'pepsi', 'cola', 'potato']
* Калорійність: 970
* Фінальні витрати: 100
