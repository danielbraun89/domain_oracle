from langchain_openai import ChatOpenAI
from pydantic import BaseModel


class DomainNameSuggestion(BaseModel):
    domain_name: str
    extension: str

    def to_full_domain(self) -> str:
        return f"{self.domain_name}{self.extension}"


class DomainNameSuggestions(BaseModel):
    suggestions: list[DomainNameSuggestion]


class DomainSuggester:
    MODEL = "gpt-4o"

    def __init__(self, openapi_token: str) -> None:
        self.openapi_token = openapi_token
        self.structured_llm = ChatOpenAI(
            model=DomainSuggester.MODEL, api_key=self.openapi_token
        ).with_structured_output(DomainNameSuggestions)

    def suggest(self, num: int, category: str, extension: str) -> DomainNameSuggestions:
        results = self.structured_llm.invoke(f"""
        suggest a domain name for {category},
        the domain should be with the {extension} extension,
        give me {num} options,
        no repetitions,
        be creative
        """)

        return results
