import tabula
# Read pdf into a list of DataFrame
#dfs = tabula.read_pdf("tab2.pdf", pages='all')
# convert PDF into CSV
print('Enter your inputfile path:')
inputfile = input()
print('The file name is  ' + inputfile)

print('Enter your output file path:')
outputfile = input()
print('The file name is  ' + outputfile)

print("Extraction started")
tabula.convert_into(inputfile, outputfile +".csv", output_format="csv", pages='all')

# convert all PDFs in a directory
#tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')

print("Tables extracted and saved as Excel successfully.")

