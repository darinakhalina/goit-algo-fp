def greedy_algorithm(items, budget):
    sorted_items = sorted(
        items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True
    )
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item, properties in sorted_items:
        if total_cost + properties["cost"] <= budget:
            selected_items.append(item)
            total_cost += properties["cost"]
            total_calories += properties["calories"]

    return selected_items, total_calories, total_cost


def dynamic_programming(items, budget):
    num_items = len(items)
    dp_table = [[0] * (budget + 1) for _ in range(num_items + 1)]

    for i in range(1, num_items + 1):
        for j in range(budget + 1):
            current_item = items[list(items.keys())[i - 1]]
            if current_item["cost"] <= j:
                dp_table[i][j] = max(
                    dp_table[i - 1][j],
                    dp_table[i - 1][j - current_item["cost"]]
                    + current_item["calories"],
                )
            else:
                dp_table[i][j] = dp_table[i - 1][j]

    selected_items = []
    i, j = num_items, budget
    while i > 0 and j > 0:
        current_item = items[list(items.keys())[i - 1]]
        if dp_table[i][j] != dp_table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= current_item["cost"]
        i -= 1

    total_cost = sum(items[item]["cost"] for item in selected_items)
    return selected_items[::-1], dp_table[num_items][budget], total_cost


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", greedy_result[0])
print("Калорійність:", greedy_result[1])
print("Фінальна сума:", greedy_result[2])

dp_result = dynamic_programming(items, budget)
print("Алгоритм динамічного програмування:")
print("Обрані страви:", dp_result[0])
print("Калорійність:", dp_result[1])
print("Фінальна сума:", dp_result[2])
