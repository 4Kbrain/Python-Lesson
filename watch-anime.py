import requests
from bs4 import BeautifulSoup
import webbrowser

def search_anime(query):
    url = f"https://otakudesu.cloud/?s={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = soup.find_all("div", class_="bsx")
    for i, result in enumerate(results, start=1):
        title = result.find("h3", class_="episodeye").text
        print(f"{i}. {title}")
    return results

def play_anime(anime_url):
    webbrowser.open(anime_url)

def main():
    query = input("Enter anime title: ")
    search_anime(query)
    
    while True:
        try:
            selection = int(input("Select anime: ")) - 1
            if selection < 0 or selection >= len(requests):
                print("Invalid selection. Please try again.")
            else:
                break  
        except ValueError:
            print("Invalid input. Please enter a number.")

    anime_url = "https://otakudesu.cloud" + requests[selection].find("a")["href"]
    play_anime(anime_url)



if __name__ == "__main__":
    main()
