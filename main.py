import phrase_tools
import wb_tools
import logic_tools
import time
from collections import defaultdict
import  openpyxl

##########output##########

exit = False

while exit == False:
    print("Welcome User")
    length = int(input('Phrase Length:'))
    min = int(input('Minimum Guess Per Letter ratio (1 is perfect): '))
    wbname = str(input('Workbook Name: '))
    trials = int(input('Trials:'))

    for trial in range(0,int(trials)):
        trial = trial + 1
        wb_name = str(wbname)+str(trial)
        logic_tools.solve_logical(length, min, wb_name)

    exitq = str(input('Exit? (y/n): '))

    if exitq == 'y':
        exit = True

