class NameNotFound(Exception):
    pass


class MustContainAtSymbol(Exception):
    pass


class TooManyAtSymbols(Exception):
    pass


class NameTooShortError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


ALLOWED_DOMAINS = [".com", ".bg", ".net", ".org"]

while True:
    email = input()
    if email == "End":
        break

    if "@" not in email:
        raise MustContainAtSymbol("Email must contain @")

    username, domain, *rest = email.split('@')

    if len(rest) > 0:
        raise TooManyAtSymbols("the whole email must only contain one '@' symbol")

    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "." + domain.split(".")[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: {', '.join(ALLOWED_DOMAINS)}")

    if not MustContainAtSymbol and not TooManyAtSymbols and not NameTooShortError and not InvalidDomainError:
        print('Email is valid')
