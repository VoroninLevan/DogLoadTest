import random
from locust import HttpUser, task, between, SequentialTaskSet


class DogLoadUser(HttpUser):
    wait_time = between(5, 15)
    
    @task(3)
    class BreedTasks(SequentialTaskSet):
        # Dict for list of breeds
        breeds = {}

        def get_random_breed(self):
            """
            Returns random key(breed) from the 'breeds' dict
            """
            return random.choice(list(self.breeds.keys()))

        def populate_breed_list(self, json):
            """
            Populates 'breeds' dict with data
            """
            self.breeds = json["message"]
    
        @task
        def perform_listing(self):
            """
            'List all breeds' endpoint test
            """
            response = self.client.get("/api/breeds/list/all")
            # Retrieve and feed json response
            self.populate_breed_list(response.json())

        @task
        def perform_listing_by_breed(self):
            """
            'By breed' endpoint test
            NOTE: relation to 'perform_listing'
            """
            self.client.get("/api/breed/" + self.get_random_breed() + "/images")

    @task(2)
    def random_image(self):
        """
        'Random image' endpoint test
        """
        self.client.get("/api/breeds/image/random")
