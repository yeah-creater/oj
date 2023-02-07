import markdown
EXTENTIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.tables'
]
def md_to_html(code):
    return markdown.markdown(code,extensions = EXTENTIONS)