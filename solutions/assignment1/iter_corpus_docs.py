"""
Authors:
Alena Zorich (elzorich@uni-koblenz.de)
Igor Maksimovich Fedotov (ifedotov@uni-koblenz.de)
Mariya Chkalova (mchkalova@uni-koblenz.de)
Arsenii Smyrnov (smyrnov@uni-koblenz.de)
"""

def iter_corpus_docs(filename):
    """Iterates over all documents in a corpus.

    Example:
        Use this function like this::

            for doc in iter_corpus_docs("simplewiki-20160501-extracted-1.xml"):
                print(doc['id'], doc['url'], doc['title'], doc['content'])

    Args:
        filename: Path to the corpus file.

    Returns:
        An iterator over all documents in the corpus. Each element of the
        iterator is a dict that represent one document, e.g.::

            {'id': '1',
             'url': 'https://simple.wikipedia.org/wiki?curid=1',
             'title': 'April',
             'content': '...'}
    """
    import re
    doc_pattern = re.compile('^<doc id="(.*)" url="(.*)" title="(.*)">$')

    cur_doc = None
    with open(filename, encoding='utf-8') as file:
        for line_no, line in enumerate(file):
            line = line[:-1]
            if line == '<corpus>' or line == '</corpus>':
                continue
            elif line.startswith('<doc'):
                m = doc_pattern.match(line)
                id, url, title = m.group(1), m.group(2), m.group(3)
                cur_doc = {
                    'id': id,
                    'url': url,
                    'title': title,
                    'content': '',
                }
            elif line == '</doc>':
                assert cur_doc, ('doc-end-tag without corresponding '
                                 'doc-start-tag on line {}.'.format(line_no))
                yield cur_doc
                cur_doc = None
            else:
                cur_doc['content'] += line + '\n'
