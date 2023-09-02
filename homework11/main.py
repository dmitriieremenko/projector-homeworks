import requests


def search_gif(search_term, api_key, num_results):
    url = (
        f'https://api.giphy.com/v1/gifs/search?'
        f'api_key={api_key}&q={search_term}&limit={num_results}'
    )
    response = requests.get(url)
    data = response.json()
    gif_urls = []
    if 'data' in data:
        for gif_data in data['data']:
            gif_url = gif_data['images']['original']['url']
            gif_urls.append(gif_url)
        return gif_urls
    else:
        return ["GIF не знайдено"]


def interface():
    with open('api_key.txt', 'r') as file:
        api_key = file.read()
    category = input("Введіть категорію для пошуку GIF: ")
    num_results = int(input("Введіть кількість посилань"
                            ", яку ви хочете отримати: "))
    gif_urls = search_gif(category, api_key, num_results)
    print("Посилання на GIF-зображення:")
    for i, gif_url in enumerate(gif_urls, start=1):
        print(f"{i}. {gif_url}")
    print(f"Не вдалося знайти GIF у категорії '{category}'")


interface()
