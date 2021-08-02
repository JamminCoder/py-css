CSS_HEADER = "/*This CSS file was generated using\n" \
             "the PyCSS package written by JamminCoder.*/"

def stringify(lst) -> str:
    output = ""
    for item in lst:
        output += item
    return output


def remove_space(string) -> str:
    chars = list(string)
    len_chars = len(chars)
    while len_chars >= 1 and chars[0] == " ":
        chars.pop(0)
        len_chars -= 1

    while len_chars >= 1 and chars[-1] == " ":
        chars.pop(-1)
        len_chars -= 1
    return stringify(chars)


def replace_underscores(string) -> str:
    output = ""
    for char in string:
        if char == "_":
            output += "-"
        else:
            output += char
    return output


def un_camel(string):
    """
    Separates words in camel-case with dashes.
    :param string:
    :return:
    """
    output = ""
    for i in range(len(string)):
        char = string[i]
        if char.isupper() and i > 0:
            output += f"-{char.lower()}"
        else:
            output += char.lower()
    return output


def cleanse_css_line(css):
    css = remove_space(css)
    un_cameled_css = un_camel(css)
    cleansed_css = replace_underscores(un_cameled_css)
    return cleansed_css


def filter_builtins(_class):
    methods = dir(_class)
    return [m for m in methods if not (m.startswith("__") and m.endswith("__"))]

def write(path, content):
    with open(path, "w") as f:
        f.write(content)
