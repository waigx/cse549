

def get_col_in_db(attr, col_table, row_table, data_table):
    attr_entry = row_table.objects.get(attribute=attr)
    result = data_table.objects.filter(attribute=attr_entry)
    return result


def get_cols_in_db(attrs, col_table, row_table, data_table):
    for attr in attrs:
        get_col_in_db(attr, col_table, row_table, data_table)

