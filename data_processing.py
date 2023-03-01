"""
 -- created by: krzysztof.kubacki ---
"""
# --- PROCESSING DATA ---
# KRKU modules
from global_vars import *
from Folder_check import projectComponent
import PDM_check as PDM
# Open-source modules
import warnings
import os
import pathlib
import pandas as pd

def importCsvBOM(stringName: str) -> pd.DataFrame:
    # make sure your csv is utf-8
    df = pd.read_csv(stringName, delimiter=';')
    return df

def createProjectListOfComponentsWithProperties(df):
    lst = []
    for i in range(len(df[fileNameColStr])):
        name = df[fileNameColStr][i]         
        # TODO - import revision and version number
        revision = None
        versionNumber = None
        typePrchCustom = df[customPrtAsmColStr][i]
        metalSheet = df[sheetMetColStr][i]
        description = df[descriptionColStr][i]
        partObj = projectComponent(name, description, revision, versionNumber, typePrchCustom, metalSheet)
        lst.append(partObj)
    return lst

def createPDMListOfComponentsWithProperties(df):
    lst = []
    for i in range(len(df[PDMfileName])):
        #  LOC... stands for local variable
        #  PDM... stands for global PDM variable
        # LOClevel = df[PDMlevel][i] 3 PDM level parts only BOM
        LOCfileName = df[PDMfileName][i]
        LOCnumber = df[PDMnumber][i]
        LOCdescription = df[PDMdescription][i]
        LOCqty = df[PDMqty][i]
        LOCstate = df[PDMstate][i]
        LOCversion = df[PDMversion][i]
        LOCrevision = df[PDMrevision][i]
        LOCrevisionBy = df[PDMrevisionBy][i]
        LOCvendor = df[PDMvendor][i]
        LOCitemID = df[PDMitemID][i]
        LOCprice = df[PDMprice][i]
        LOCdeliveryTime = df[PDMdeliveryTime][i]
        LOCtypeSld = df[PDMtypeSld][i]
        LOCplateThickness = df[PDMplateThickness][i]
        LOCsparePart = df[PDMsparePart][i]
        LOCweight = df[PDMweight][i]
        LOCmaterial = df[PDMmaterial][i]
        LOCmanufacturingMethod = df[PDMmanufacturingMethod][i]
        LOCsurfaceTreatment = df[PDMsurfaceTreatment][i]
        LOCproject = df[PDMproject][i]
        LOCprojectName = df[PDMprojectName][i]
        LOCprojectNumber = df[PDMprojectNumber][i]
        #  define part object
        partObj = PDM.PDMComponent(LOCfileName, LOCnumber, LOCdescription,
                                   LOCqty, LOCstate, LOCversion, LOCrevision,
                                   LOCrevisionBy, LOCvendor, LOCitemID,
                                   LOCprice, LOCdeliveryTime, LOCtypeSld,
                                   LOCplateThickness, LOCsparePart, LOCweight,
                                   LOCmaterial, LOCmanufacturingMethod,
                                   LOCsurfaceTreatment, LOCproject,
                                   LOCprojectName, LOCprojectNumber)
        lst.append(partObj)
    return lst

def compareTwoLists(BOMlist, folderList, atrName: str):
    
    lstA = [o.name for o in BOMlist]  # i iterator stands for list projectArray (from BOM)
    lstB = folderList  # j iterator stands for list packageArray (from folderlist)
    folderList.sort()  # think if it is worth
    
    for i in range(len(lstA)):
        for j in range(len(lstB)):
            if lstA[i] == lstB[j][:len(lstA[i])]:
                if atrName == "PDF":
                    BOMlist[i].isPDFfile = True
                elif atrName == "DWG":
                    BOMlist[i].isDWGfile = True
                elif atrName == "STEP":
                    BOMlist[i].isSTEPfile = True
                elif atrName == "DXF":
                    # for i in range(len(BOMlist)):  # TODO we are working here 
                    #     BOMlist[i].isDXFfile = None
                    if BOMlist[i].metalSheet == True:
                        BOMlist[i].isDXFfile = True
                    else:
                        BOMlist[i].isDXFfile = False
                else:
                    print("something went wrong")
                    return None
                break

def metalSheetBoolean(string: str)-> bool:
    """
    Check if component is metal sheet
    Parameters
    ----------
    string : str
        "Yes" or "No"

    Returns
    -------
    bool
        True -> metal sheet
        False -> not metal sheet
        None -> value in table is not as "Yes" or "No"

    """
    if string == "Yes":
        return True
    elif string == "No":
        return False
    else:
        warnings.warn('One of part has wrong attribute assinged it should be <Yes> or <No>.'
                      '/nPlease validate your data.'
                      'If this warning is set Toolbox library ignore this message.')
        return None

def changeStatusOfAtrFile(obj, fileFormat: str):
    # TODO consider if it is neccessery
    if fileFormat == "PDF":
        return obj.isPDFfile
    elif fileFormat == "DWG":
        return obj.isDWGfile
    elif fileFormat == "STEP":
        return obj.isSTEPfile
    elif fileFormat == "DXF":
        return obj.isDXFfile
    else:
        print("something went wrong")
        return None

def listOfFilesFromSubfolder(subfolder, inputList):
    folderPath = os.path.join(pathlib.Path(__file__).parent.resolve(), folderWithPackage, subfolder)
    outputlist = os.listdir(folderPath)
    return outputlist

def checkForExtraFiles(df: pd.DataFrame, fType: str) -> set:
    global folder
    filesList = os.listdir('./' + folder + '/' + fType)
    folderSet = set()
    for item in filesList:
        pos = item.find("_")
        if pos == -1:
            folderSet.add(item)
        else:
            folderSet.add(item[:pos])


    projectSet = set(df.loc[df['Type'] == "Custom Part / Assembly"])
    df_sel = df.loc[df['Type'] == "Custom Part / Assembly"]
    projectSet = set(df_sel["SW-File Name(File Name)"])
    
    return folderSet.difference(projectSet)