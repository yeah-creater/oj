from markdown import markdown
EXTENTIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.codehilite',
    'markdown.extensions.toc',
    'markdown.extensions.tables',
    'mdx_math'
]
def md_to_html(code):
    html = markdown(code,extensions = EXTENTIONS, extension_configs={
                        'mdx_math': {
                            'enable_dollar_delimiter': True,  # 是否启用单美元符号（默认只启用双美元）
                            'add_preview': True  # 在公式加载成功前是否启用预览（默认不启用）
                        }
                    })
    return html