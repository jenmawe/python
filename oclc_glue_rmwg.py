import pymarc

marcFileIn = pymarc.MARCReader(open('rec_merge_export.mrc', 'rb'))

with open('rec_merge_export_oclcglued.mrc', 'wb') as f:
    for record in marcFileIn:
        if record['035'] is not None:
            for fd in record.get_fields('035'):
                if fd['a'].startswith('(OCoLC)'):
                    oclcNum = ''.join(x for x in fd['a'] if x.isdigit())
                    newfield959 = pymarc.Field(
                        tag='959',
                        indicators=[' ', ' '],
                        subfields=['a', oclcNum]
                    )
                    record.add_ordered_field(newfield959)
        if record['019'] is not None:
            for fd019 in record.get_fields('019'):
                fd019as = fd019.get_subfields('a')
                for fd019a in fd019as:
                    newfield959 = pymarc.Field(
                        tag='959',
                        indicators=[' ', ' '],
                        subfields=['a', fd019a]
                    )
                    record.add_ordered_field(newfield959)
        f.write(record.as_marc21())
