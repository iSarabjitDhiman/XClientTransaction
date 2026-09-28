import re

ADDITIONAL_RANDOM_NUMBER: int = 3
DEFAULT_KEYWORD: str = "obfiowerehiring"

# Logged-out x.com/home now redirects to the new x-web app, whose page lacks the ondemand.s chunk map.
# /i/jf/ still serves the responsive-web page with the chunk map, site key, and loading animation.
HOME_PAGE_URL: str = "https://x.com/i/jf/"
ON_DEMAND_FILE_URL: str = "https://abs.twimg.com/responsive-web/client-web/ondemand.s.{filename}a.js"
ON_DEMAND_FILE_REGEX: re.Pattern = re.compile(
    r""",(\d+):["']ondemand\.s["']""", flags=(re.VERBOSE | re.MULTILINE))
ON_DEMAND_HASH_PATTERN: str = r',{}:\"([0-9a-f]+)\"'

INDICES_REGEX: re.Pattern = re.compile(
    r"""(\(\w{1}\[(\d{1,2})\],\s*16\))+""", flags=(re.VERBOSE | re.MULTILINE))

MIGRATION_REDIRECTION_REGEX: re.Pattern = re.compile(
    r"""(http(?:s)?://(?:www\.)?(twitter|x){1}\.com(/x)?/migrate([/?])?tok=[a-zA-Z0-9%\-_]+)+""", re.VERBOSE)


if __name__ == "__main__":
    pass
