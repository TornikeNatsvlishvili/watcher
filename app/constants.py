from enum import Enum

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1)'
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95'
    'Safari/537.36'
}


class MagazineTypes(Enum):
    ECONOMIST = 'Economist'
    BLOOMBERG = 'Bloomber'
    GQ = 'GQ'
    ESQUIRE = 'Esquire'
    THE_ATLANTIC = 'The Atlantic'
    VANITY_FAIR = 'Vanity Fair'
    FASHION_MAGAZINE = 'Fashion Magazine'
    NATIONAL_GEOGRAPHIC = 'National Geographic'
    US_WEEKLY = 'Us Weekly'
    WIRED = 'Wired'


URLS = [
    ('http://magazinelib.com/?s=economist+usa', MagazineTypes.ECONOMIST),
    ('http://magazinelib.com/?s=bloomberg+businessweek+usa', MagazineTypes.BLOOMBERG),
    ('http://magazinelib.com/?s=the+atlantic', MagazineTypes.THE_ATLANTIC),
    ('http://magazinelib.com/?s=gq+usa', MagazineTypes.GQ),
    ('http://magazinelib.com/?s=esquire+usa', MagazineTypes.ESQUIRE),
    ('http://magazinelib.com/?s=vanity+fair+usa', MagazineTypes.VANITY_FAIR),
    ('http://magazinelib.com/?s=Fashion+Magazine', MagazineTypes.FASHION_MAGAZINE),
    ('http://magazinelib.com/?s=national+geographic+usa', MagazineTypes.NATIONAL_GEOGRAPHIC),
    ('http://magazinelib.com/?s=us+weekly', MagazineTypes.US_WEEKLY),
    ('http://magazinelib.com/?s=wired+usa', MagazineTypes.WIRED),
]
