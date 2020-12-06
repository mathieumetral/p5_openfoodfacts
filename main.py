from src.api.openfoodfacts import OpenFoodFacts

api = OpenFoodFacts()

if __name__ == "__main__":
    categories = api.get_random_categories(5)
    print(categories)
