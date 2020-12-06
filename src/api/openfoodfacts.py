import os
import requests


class OpenFoodFacts:
    API_ENDPOINT = "https://fr.openfoodfacts.org/"

    def get_random_categories(self, num: int):
        r = requests.get(url=self.API_ENDPOINT + "categories.json")

        if r.status_code != 200:
            raise Exception("An error occurred while calling the API.\nAdditional Information :" +
                            requests.exceptions.HTTPError)

        response = r.json()

        if "tags" not in response:
            raise Exception("The API returned a response without the expected elements. This error can occur as a "
                            "result of a major API update that changes the structure of responses.")

        categories = random.sample(response["tags"], num)

        for category in categories:
            category.pop("id", None)
            category.pop("known", None)
            category.pop("products", None)

        return categories

    def get_products_by_category(self):
        for i in range(1, int(os.getenv("IMPORT_NUMBER_OF_PAGES")) + 1):
            print(i)

        # r = requests.get(url=self.API_ENDPOINT + "cgi/search.pl", params={
        #     "action": "process",
        #     "json": 1,
        #     "page_size": 100
        #
        # })

        # if "name" not in category or "url" not in category:
        #     raise Exception("The category passed in parameter is incorrect. It must include the keys: name and url.")
