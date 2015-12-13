import sys


def file2db(file_path, col_table, row_table, data_table):
    print "importing", file_path
    with open(file_path) as ori_file:
            file_lines = ori_file.readlines()
            len_data_lines = len(file_lines) - 1
            row_items = file_lines[0][:-1].split("\t")[1:]
            row_table.objects.all().delete()
            row_items_entries = []
            for attr in row_items:
                row_table.objects.create(attribute=attr)
                row_items_entries.append(row_table.objects.get(attribute=attr))
            attr_len = len(row_items_entries)
            col_table.objects.all().delete()
            data_entries = [None] * (len_data_lines*attr_len)
            data_idx = 0
            for line_idx in xrange(1, len_data_lines + 1):
                entry = file_lines[line_idx].split("\t")
                col_table.objects.create(entry_id=entry[0])
                rna_entry = col_table.objects.get(entry_id=entry[0])
                for i in xrange(attr_len):
                    data_entries[data_idx] = data_table(
                        entry_id=rna_entry,
                        attribute=row_items_entries[i],
                        value=float(entry[i+1])
                    )
                sys.stdout.write("\r%d%%" % (line_idx*100/len_data_lines))
                sys.stdout.flush()
            data_table.objects.all().delete()
            data_table.objects.bulk_create(data_entries)
