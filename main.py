"""
 -- created by: krzysztof.kubacki ---
definitons:
- package: refers to folder of files (pdf,dwg,dxf,step)
    that will be sent to subsuplier
- project: refers to list of files (from project)
    that are included into machine
-- initial conditions:
 - CSV delimers: ";" make sure your csv is utf-8 format
"""
# --- MAIN.PY ---
# KRKU modules
from global_vars import *
from data_processing import *
from printing_results import *
from Folder_check import *
# Open-source modules
import time
from math import isnan

if __name__ == "__main__":
    it = 0 # check
    # --- INITIALIZE CONDTITION ---
    start_time = time.time()

    # --- PROCESSING DATA ---
    # import dataframes
    dfBOM = importCsvBOM(folder + "/" + strBOMCSV)
    dfPDM  = importCsvBOM(folder + "/" + strBOMDPMCSV)
    # create list of objects project and PDM
    projectArray = createProjectListOfComponentsWithProperties(dfBOM)
    PDMArray = createPDMListOfComponentsWithProperties(dfPDM)
    packageArray = packageFileComponent()
    
    packageArray.pdf = listOfFilesFromSubfolder('PDF', packageArray.pdf)
    packageArray.dwg = listOfFilesFromSubfolder('DWG', packageArray.dwg)
    packageArray.step = listOfFilesFromSubfolder('STEP', packageArray.step)
    packageArray.dxf = listOfFilesFromSubfolder('DXF', packageArray.dxf)

    compareTwoLists(projectArray, packageArray.pdf, "PDF")
    compareTwoLists(projectArray, packageArray.dwg, "DWG")
    compareTwoLists(projectArray, packageArray.step, "STEP")
    compareTwoLists(projectArray, packageArray.dxf, "DXF")

    for each in projectArray: # here something is changing
        each.checkIfDocsAreComplete()

    packageArray.checkWhatVersionAndRevisionIs(packageArray.pdf, "PDF")
    packageArray.checkWhatVersionAndRevisionIs(packageArray.dwg, "DWG")
    packageArray.checkWhatVersionAndRevisionIs(packageArray.pdf, "STEP")
    packageArray.checkWhatVersionAndRevisionIs(packageArray.dwg, "DXF")

    for each in projectArray:
        each.assignVersionAndRevision(packageArray)

    

    # --- DEBUGGING ---
    # it = printFileIncluded(projectArray, it)
    # debuggingStepVersions()   
    # printResultsAsBoolean(projectArray)

    # --- PRINTING RESULTS ---
    # printingCreatedObject(projectArray)
    printFinalResult(projectArray)
    [PrintExtraFilesNeededToBeChecked(checkForExtraFiles(dfBOM, f), f) for f in typesOfFiles]

    # ITS TIME FOR REAL PDM BOM

    print('\n \nTime of execution is:', round(time.time() - start_time, 3), 'seconds')