def html_list(items):
    ul = ['<ul>']

    for item in items:
        ul.append('<li>{}</li>'.format(item))
    ul.append('</ul>')

    return '\n'.join(ul)


items = ['first string', 'second string']
print(html_list(items))
