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
    BAZAAR = 'Bazaar'
    YACHTS_INTERNATIONAL = 'Yachts International'
    BOAT_INTERNATIONAL = 'Boat International'
    FINWEEK = 'Finweek'
    FORBES = 'Forbes'
    HACKERCOOL = 'Hackercool'
    MATHEMATICS_TODAY = 'Mathematics Today'
    MAXIMUM_PC = 'Maximum PC'
    NYLON = 'Nylon'
    ARCHITECTURAL_DIGEST = 'Architectural Digest'
    DWELL = 'Dwell'
    HARVARD_BUSINESS_REVIEW = 'Harvard Business Review'
    THE_SPECTATOR = 'The Spectator'
    THE_NEW_YORKER = 'The New Yorker'


URLS = [
    ('http://magazinelib.com/?s=economist+usa', MagazineTypes.ECONOMIST),
    ('http://magazinelib.com/?s=bloomberg+businessweek+usa', MagazineTypes.BLOOMBERG),
    ('http://magazinelib.com/?s=the+atlantic', MagazineTypes.THE_ATLANTIC),
    ('http://magazinelib.com/?s=gq+usa', MagazineTypes.GQ),
    ('http://magazinelib.com/?s=esquire+usa', MagazineTypes.ESQUIRE),
    ('http://magazinelib.com/?s=vanity+fair+usa', MagazineTypes.VANITY_FAIR),
    ('http://magazinelib.com/?s=Fashion+Magazine', MagazineTypes.FASHION_MAGAZINE),
    ('http://magazinelib.com/?s=national+geographic+usa',
     MagazineTypes.NATIONAL_GEOGRAPHIC),
    ('http://magazinelib.com/?s=us+weekly', MagazineTypes.US_WEEKLY),
    ('http://magazinelib.com/?s=wired+usa', MagazineTypes.WIRED),
    ('http://magazinelib.com/?s=bazaar+usa', MagazineTypes.BAZAAR),
    ('http://magazinelib.com/?s=Yachts+International',
     MagazineTypes.YACHTS_INTERNATIONAL),
    ('http://magazinelib.com/?s=Boat+International',
     MagazineTypes.BOAT_INTERNATIONAL),
    ('http://magazinelib.com/?s=Finweek', MagazineTypes.FINWEEK),
    ('http://magazinelib.com/?s=Forbes+USA', MagazineTypes.FORBES),
    ('http://magazinelib.com/?s=Hackercool', MagazineTypes.HACKERCOOL),
    ('http://magazinelib.com/?s=Mathematics+Today', MagazineTypes.MATHEMATICS_TODAY),
    ('http://magazinelib.com/?s=Maximum+PC', MagazineTypes.MAXIMUM_PC),
    ('http://magazinelib.com/?s=Nylon', MagazineTypes.NYLON),
    ('http://magazinelib.com/?s=Architectural+Digest+USA',
     MagazineTypes.ARCHITECTURAL_DIGEST),
    ('http://magazinelib.com/?s=Dwell', MagazineTypes.DWELL),
    ('http://magazinelib.com/?s=Harvard+Business+Review+USA',
     MagazineTypes.HARVARD_BUSINESS_REVIEW),
    ('http://magazinelib.com/?s=The+Spectator', MagazineTypes.THE_SPECTATOR),
    ('http://magazinelib.com/?s=The+New+Yorker', MagazineTypes.THE_NEW_YORKER),
]
