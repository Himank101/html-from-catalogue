import pandas as pd
from openpyxl import load_workbook
from openpyxl.drawing.image import Image

def read_excel_file(file_path):
    # Read Excel data using pandas
    excel_data = pd.read_excel(file_path, sheet_name=None)
    # Load workbook using openpyxl to handle images
    workbook = load_workbook(file_path)
    return excel_data, workbook

def process_data_to_html(excel_data, workbook):
    html_data = ''
    # Iterate through each sheet in the Excel file
    for sheet_name, data in excel_data.items():
        html_data += f'<h2>{sheet_name}</h2><table>'
        html_data += data.to_html(index=False, header=True, border=1)
        html_data += '</table>'
        ws = workbook[sheet_name]
        # Process images in the sheet
        for image in ws._images:
            cell = (image.anchor._from.row, image.anchor._from.col)
            img_tag = f'<img src="data:image/png;base64,{image._data}" alt="Embedded Image" />'
            html_data = html_data.replace(f'<td>{cell[0]}</td>', f'<td>{img_tag}</td>')
    return html_data

def generate_html_file(html_data, output_file):
    html_content = f'''
    <html>
    <head>
        <title>Excel to HTML</title>
        <style>
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid black; padding: 8px; text-align: left; }}
        </style>
    </head>
    <body>
        {html_data}
    </body>
    </html>
    '''
    with open(output_file, 'w') as file:
        file.write(html_content)

def main():
    input_file = '/path/to/excel/file.xlsx'
    output_file = 'output.html'
    excel_data, workbook = read_excel_file(input_file)
    html_data = process_data_to_html(excel_data, workbook)
    generate_html_file(html_data, output_file)

if __name__ == "__main__":
    main()
