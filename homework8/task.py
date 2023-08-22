def range_cats_with_hats(num_cats):
    cats_with_hats = set()
    for round_num in range(1, num_cats + 1):
        for cat_num in range(1, num_cats + 1):
            if cat_num % round_num == 0:
                if cat_num in cats_with_hats:
                    cats_with_hats.remove(cat_num)
                else:
                    cats_with_hats.add(cat_num)
    return cats_with_hats


def interface():
    num_cats = 100
    cats_with_hats = range_cats_with_hats(num_cats)
    print("Коти, які мають капелюшки:")
    for cat_num in cats_with_hats:
        print(f"Кіт - Номер {cat_num}")


interface()
