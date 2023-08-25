def range_cats_with_hats(num_cats):
    cat_hats = {}
    for cat in range(1, num_cats + 1):
        cat_hats[cat] = False
    for round_num in range(1, num_cats + 1):
        for cat_num in range(round_num - 1, num_cats, round_num):
            cat_hats[cat_num + 1] = not cat_hats[cat_num + 1]
    cats_with_hats = [cat_num for cat_num, has_hat in cat_hats.items()
                      if has_hat]
    return cats_with_hats


def interface():
    num_cats = 100
    cats_with_hats = range_cats_with_hats(num_cats)
    print("Коти, які мають капелюшки:")
    for cat_num in cats_with_hats:
        print(f"Кіт - Номер {cat_num}")


interface()
