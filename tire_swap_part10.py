# === Stage 10: Текстовый поиск ===
# Project: TireSwap
def highlight_match(text: str, pattern: str) -> str:
    if not pattern:
        return text
    lower_text = text.lower()
    lower_pattern = pattern.lower()
    start = 0
    parts = []
    index = lower_text.find(lower_pattern, start)
    while index != -1:
        parts.append(text[start:index])
        parts.append('\033[7m' + text[index:index + len(pattern)] + '\033[0m')
        start = index + len(pattern)
        index = lower_text.find(lower_pattern, start)
    parts.append(text[start:])
    return ''.join(parts)


def search_sets(sets, query: str) -> list:
    query = query.strip()
    if not query:
        return sets
    results = []
    for name, size, season, mileage in sets:
        lower_name = name.lower()
        lower_size = size.lower()
        lower_season = season.lower()
        lower_mileage = str(mileage).lower()
        haystack = ' '.join([lower_name, lower_size, lower_season, lower_mileage])
        if query.lower() in haystack:
            results.append((name, size, season, mileage))
    return results


def render_search_result(name, size, season, mileage) -> str:
    line = f'{name:<24} {size:<8} {season:<10} {mileage:>8}'
    return line


def interactive_search(sets, prompt: str = 'Search:') -> None:
    print(f'{prompt}\n')
    while True:
        query = input().strip()
        if query.lower() in ('quit', 'exit', 'clear'):
            break
        results = search_sets(sets, query)
        if not results:
            print('No matching sets found.\n')
            continue
        for name, size, season, mileage in results:
            print(render_search_result(name, size, season, mileage))
        print()
