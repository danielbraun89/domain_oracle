import requests


class DomainValidator:
    WHOIS_API_DOMAIN = "https://whois-by-api-ninjas.p.rapidapi.com/v1/whois"

    def __init__(self, rapidapi_token: str) -> None:
        self.rapidapi_token = rapidapi_token

    def validate(self, domain: str) -> bool:
        response = requests.get(
            DomainValidator.WHOIS_API_DOMAIN,
            headers={"x-rapidapi-key": self.rapidapi_token, "x-rapidapi-host": "whois-by-api-ninjas.p.rapidapi.com"},
            params={"domain": domain},
            timeout=1,
        )

        if response.status_code != 200:
            raise ValueError(str(response))

        return len(response.json()) == 0  # if whois information is empty the domain is available
