# 9. Stwórz program który przyjmie w parametrze dowolną listę np ['col1', 'col2', 'col3'] i wyświetli:
#    +------+------+------+
#    | col1 | col2 | col3 |
#    +------+------+------+
#    Dodatkowym atutem będzie gdy szerokość kolumn będzie zawsze równa bez względów na zawartość, tekst wyrównany do lewej.
#    Maksymalna szerokość kolumny np 30znaków jesli tekst będzie za długi niech zawartość przycina się i kończy trzema kropkami.
#    A jeszcze większym atutem będzie gdy będzie można podać liste zagnieżdżoną i narysuje się tabela z odpowiednią ilością wierszy i kolumn

def nested_depth_level(lst) -> int:
    """Checks if a list is nested and returns values:
    0 - not a list
    1 - a non-nested list
    2 - a nested list
    :param lst: list to check
    :type lst: list
    :return: nesting depth"""
    for item in lst:
        if isinstance(item, list):
            if any(isinstance(subitem, list) for subitem in item):
                return 2  # więcej niż jeden poziom
            else:
                return 1  # tylko jeden poziom
    return 0  # brak zagnieżdżenia


def longest_sublist_length(lst) -> int:
    """Returns length of longest sublist or 0 if list is not nested.
    :param lst: list to check
    :type lst: list
    :return: length of the longest sublist"""
    sublists = [item for item in lst if isinstance(item, list)]
    if not sublists:
        return 0
    return max(len(sublist) for sublist in sublists)


def format_string(cell_content: str) -> str:
    """Formats a string according to requirements
    :param cell_content: cell content to be formatted
    :type cell_content: str
    :return: formatted cell content"""
    if len(cell_content) > 30:
        return cell_content[:27] + "..."
    else:
        return cell_content.ljust(30)


def draw_horizontal_line(n_columns: int) -> None:
    """Draws a horizontal line
    :param n_columns: number of columns in the table
    :type n_columns: int
    :return: None"""
    HORIZONTAL_LINE = "+" + "-" * 34
    print(HORIZONTAL_LINE * n_columns + "+")


def draw_row(content: list) -> None:
    """Draws a row with contents
    :param content: content to be put into cells, each item is printed in a separate cell
    :type content: list
    :return: None"""
    VERTICAL_LINE = "|  "
    row = ""
    for cell in content:
        cell = format_string(str(cell))
        row += VERTICAL_LINE + cell + "  "
    row += "|"
    print(row)


def draw_table(content: list) -> None:
    """
    Prints list's content as a table.
    :param content: A list containing the table's content.
                    In case of a nested list, each sub-list is treated as a row.
    :return: None
    """
    # print("~~Narysuj sobie tabelę~~")
    nesting_level = nested_depth_level(content)

    if nesting_level == 0:
        # Jednowierszowa tabela
        columns_number = len(content)
        draw_horizontal_line(columns_number)
        draw_row(content)
        draw_horizontal_line(columns_number)

    elif nesting_level == 1:
        # Tabela wielowierszowa
        rows_number = len(content)
        columns_number = longest_sublist_length(content)

        draw_horizontal_line(columns_number)
        for row_index in range(rows_number):
            row = content[row_index]
            padded_row = row + [""] * (columns_number - len(row))
            draw_row(padded_row)
            draw_horizontal_line(columns_number)

    else:
        print("Uwaga! Twoja lista ma zbyt wiele poziomów zagnieżdżenia. Sprawdź poprawność swoich danych.")


# draw_table([[1, 2, 3], [4, ''], [7, "Dłuuuuuuuuuuuuugi tekst", "Jeszcze dłuuuuuuuuuuuuższy tekst"]])
