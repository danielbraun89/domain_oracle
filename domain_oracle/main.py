import os

from domain_oracle.suggester import DomainSuggester
from domain_oracle.validator import DomainValidator

if __name__ == "__main__":
    # TODO: accept args
    OPENAPI_TOKEN = os.getenv("OPENAPI_TOKEN", "")
    RAPIDAPI_TOKEN = os.getenv("RAPIDAPI_TOKEN", "")
    NUM_OF_DOMAINS = 10
    CATEGORY = "start up companies"
    EXTENSION = ".com"  # free tier in ninja api only support .com domains

    suggester = DomainSuggester(OPENAPI_TOKEN)
    validator = DomainValidator(RAPIDAPI_TOKEN)

    results = suggester.suggest(NUM_OF_DOMAINS, CATEGORY, EXTENSION)

    valid_domains = []
    for suggestion in results.suggestions:
        full_name = suggestion.to_full_domain()
        if validator.validate(full_name):
            valid_domains.append(full_name)

    print(valid_domains)
