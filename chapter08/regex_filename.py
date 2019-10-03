import re
filename = 'mad_lab_01.tmt'
filename_regex = re.compile(r'''
    (\w+)
    (\.\w{3})
''', re.VERBOSE)
mo = filename_regex.search(filename)

new_filename = mo.group(1) + '_output' + mo.group(2)
print(new_filename)
