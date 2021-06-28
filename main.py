import csv

""" Make sure the exported HSU Report from GW Vistas is opened in excel and saved as this eliminates the
 file error. This top down scrip simply deletes out unwanted rows that are in the first row row[0] of the
 exported HSU report from a retirement or transfer analysis. It is built off of J. Reedy script in VBA but is
 much faster. """

# Make sure to update this file path to the location of the exported HSU (currently in the external 1tb ssd drive)
filepath = "H:/clean_harbors_inj/2010_TOOL_140923_CLEAN_HARBORS_INJ_210616.csv"

# Any words we want deleted out of the first row
del_words = ['cln', 'qrt', 'hsu']

# Opens the csv as inp, creates new csv file in same folder with _processed added on
with open(filepath, newline='') as inp, open(f'{filepath[:-4]}' + "_processed.csv", 'w', newline='') as out:
    reader = csv.reader(inp)
    writer = csv.writer(out)
    # Flow control top down
    for row in reader:
        if 'summary' in row[0].lower().strip():  # Keeps header row that contains hsu (don't want deleted)
            writer.writerow(row)  # Writes out the row that contains summary in row[0]
        else:
            counter = 0  # Makes a counter to work with del_words
            for word in del_words:
                if word not in row[0].lower().strip():
                    counter += 1
                    if counter == len(del_words):  # Row ONLY gets printed if no words in del_words are present
                        writer.writerow(row)  # Print row to new csv
