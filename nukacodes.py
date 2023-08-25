import pdfkit

input_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=2in, height=1in">
    <title>Custom Page Size</title>
</head>
<body>
    <div style="width: 2in; height: 1in; background-color: lightgray;">
        <p>This is a custom-sized page.</p>
    </div>
</body>
</html>
'''
output_pdf = 'custom_page.pdf'

# Specify options, including the custom page size
options = {
    'page-width': '2in',
    'page-height': '1in'
}

pdfkit.from_string(input_html, output_pdf, options=options)

print(f"PDF generated: {output_pdf}")
