__author__ = 'Jian Yang'
__date__ = '12/13/15'

fn = 'transcripts.filtered.fa'
res = 'stat.res'

g4 = 'ATCG'

def write_head(rf):
    fields = ['name', 'gene', 'gc']
    print >> rf, '\t'.join(fields)

def write_line(rf, name, gene):
    assert isinstance(gene, str)
    l = len(gene)
    cnt_a = gene.count('A')
    cnt_t = gene.count('T')
    cnt_c = gene.count('C')
    cnt_g = gene.count('G')
    cnt_gc = cnt_c + cnt_g
    gc_content = cnt_gc * 1.0 / l

    a_content = cnt_a * 1.0 / l
    t_content = cnt_t * 1.0 / l
    c_content = cnt_c * 1.0 / l
    g_content = cnt_g * 1.0 / l

    contents = []
    for i in g4:
        for j in g4:
            contents.append(gene.count(i+j) * 1.0 / l)

    elements = [name, len(gene), gc_content, a_content, t_content, c_content, g_content]

    print >> rf, '\t'.join([str(x) for x in elements])

with open(fn, 'r') as f:
    with open(res, 'w') as rf:
        write_head(rf)
        name = None
        gene = ""

        for l in f:
            if l.startswith('>'):
                if name is not None:
                    write_line(rf, name, gene)

                name = l.strip()[1:]
                gene = ""
            else:
                gene += l.strip()

        if name is not None:
            write_line(rf, name, gene)



