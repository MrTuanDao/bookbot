def get_book_text(filepath) -> str:
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents 


def count_word(string: str) -> int:
    return len(string.split())


def count_character(string: str) -> dict:
    count_c = {}
    for c in string:
        c_lower = c.lower()
        if c_lower not in count_c:
            count_c[c_lower] = 0

        count_c[c_lower] += 1

    return count_c


def sort_c_dict(c_dict: dict) -> list[dict]:
    c_dict_list = []

    for c in c_dict:
        c_dict_list.append({
            "char": c, 
            "num": c_dict[c], 
        })

    def sort_on(items):
        return items["num"]
    
    c_dict_list.sort(reverse=True, key=sort_on)
    
    return c_dict_list