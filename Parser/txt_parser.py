import time
import progress_Bar

from openpyxl import Workbook
wb = Workbook()

f = open("Resources/ocr_data.txt", "r")

# grab the active worksheet
ws = wb.active

tries = 1

#for i in f:
#    key = 'A' + str(tries)
#    ws[key] = i
#    print(tries)
#    tries += 1

# A List of Items
l = 10

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
for i, item in enumerate(f):
    # Do stuff...
    key = 'A' + str(tries)
    ws[key] = item
    tries += 1

    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = 'Complete', length = 50)
    
print("Done!")

# Save the file
wb.save("sorted_data.xlsx")



