from abc import ABC, abstractmethod

class Paginator(ABC):
    @abstractmethod
    def fetch_all(self, client, **kwargs):
        pass

class APIPaginator(Paginator):
    def fetch_all(self, client, **kwargs):
        all_data = []
        page = kwargs.pop('page', 1)
        while True:
            response = client.get_entities(page=page, **kwargs)
            data = response.get("data", [])
            if not data:
                break
            all_data.extend(data)
            page += 1
        return all_data
