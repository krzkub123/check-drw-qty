"""
 -- created by: krzysztof.kubacki ---
"""
# --- PRINTING RESULTS ---
# KRKU modules
from global_vars import *
# Open-source modules

def printResultsAsBoolean(arr) -> print:
    """
    Print list of boolean which files are included

    Parameters
    ----------
    arr : TYPE
        List of object files in package.

    Returns
    -------
    print
        it is printing list of boolean of all files that are included in package.
    """
    print('\n PDF files:\t len: \t', len([o.isPDFfile for o in arr]))
    # print([str(o.name)+ " : " + str(o.isPDFfile) for o in arr])
    print([o.isPDFfile for o in arr])
    print('\n DWG files:\t len: \t', len([o.isDWGfile for o in arr]))  
    # print([str(o.name)+ " : " + str(o.isDWGfile) for o in arr])
    print([o.isDWGfile for o in arr])
    print('\n STEP files:\t len: \t', len([o.isSTEPfile for o in arr]))
    # print([str(o.name)+ " : " + str(o.isSTEPfile) for o in arr])
    print([o.isSTEPfile for o in arr])
    print('\n DXF files:\t len: \t', len([o.isDXFfile for o in arr]))
    # print([str(o.name)+ " : " + str(o.isDXFfile) for o in arr])
    print([o.isDXFfile for o in arr])
    print('\n ?All files?:\t len: \t', len([o.allFilesIncluded for o in arr]))
    # print([str(o.name)+ " : " + str(o.allFilesIncluded) for o in arr])
    print([o.allFilesIncluded for o in arr])

def printFileIncluded(arr: list, n: int) -> int:
    """
    Printing all attribute (.allFilesIncluded) in list arr,
    temp func created for debuggig

    Parameters
    ----------
    arr : list
        list with objects.allFilesIncluded (projectArray)
    n : int
        iteration of loop

    Returns
    -------
    print
        how many times it was done

    """
    print("<"*10, "iteration of loop: ", n, ">"*10)
    print("Are all files included")
    for each in arr:# check
        print(each.allFilesIncluded)
    print("---- loop pause ----")
    print("Are all dwg file included")
    for each in arr:# check
        print(each.isDWGfile)
    print("--------------------after loop--------------------")
    n +=1 
    return n

def printingCreatedObject(arr):
    global typeFilesNotToBeChecked
    for i in range(len(arr)):
        if arr[i].typePrchCustom in typeFilesNotToBeChecked:
            continue
        else:
            print('\n' + '-'*10 + ' ' + str(arr[i].name) +' ' + '-'*10)
            print('Name of component is ' + str(arr[i].description) + '. It has number:',
              str(arr[i].name) + '\nWhich type is ' + str(arr[i].typePrchCustom), 
              '\nIs it metal sheet: ' + str(arr[i].metalSheet) + '\n',
              'Drawing Revision_Version: ' + str(arr[i].drawingRevisionBOM) + '_' + str(arr[i].drawingVersionBOM)+ '\n',
              'Model 3d Revision_Version: ' + str(arr[i].model3dRevisionBOM) + '_' + str(arr[i].model3dVersionBOM)+'\n')
            # filesWhichRequiresBeingCheck(arr[i].typePrchCustom, filesNotToBeChecked)
            if arr[i].allFilesIncluded:
                print('All required files for this component are included.')
            else:
                print('!!! Check package !!!')
            if arr[i].isPDFfile == False:
                print('no PDF file!')
            if arr[i].isDWGfile == False:
                print('no DWG file!')
            if arr[i].isSTEPfile == False:
                print('no STEP file!')
            if arr[i].isDXFfile == False and arr[i].metalSheet == True:
                print('no DXF file!')
            print('_'*100)

def debuggingStepVersions():
    """
    temp function for debugging

    Returns
    -------
    None.

    """
    print("----DEBUGGING VERSIONS OF STEPS----")
    print("\nprinting pdfs...: \n")
    print(packageArray.pdf)
    print(packageArray.pdfRevision)
    print(packageArray.pdfVersion)
    print("\nprinting dwgs...: \n")
    print(packageArray.dwg)
    print(packageArray.dwgRevision)
    print(packageArray.dwgVersion)
    print("\nprinting steps...: \n")
    print(packageArray.step)
    print(packageArray.stepRevision)
    print(packageArray.stepVersion)
    print("\nprinting dxfs...: \n")
    print(packageArray.dxf)
    print(packageArray.dxfRevision)
    print(packageArray.dxfVersion)    

def printFinalResult(arr: list) -> print:
    """
    Parameters
    ----------
    arr : list
        project (BOM) list of components (as object) with included attributes

    Returns
    -------
    print
        Printing all components listed to console with its properties,
        additionally printing if package is complete or not
    """
    global typeFilesNotToBeChecked, typeFilesToBeChecked
    lst1 = []
    lst1missing = []
    lst2 = []
    lst2missing = []
    lst3 = []
    lst3missing = []
    space = 4*'-'
    for each in arr:
        if each.typePrchCustom in typeFilesNotToBeChecked:
            continue
        elif (each.typePrchCustom in typeFilesToBeChecked):
            lst1.append(each.allFilesIncluded)
            lst1missing.append(each)
            lst2.append(each.drawingRevisionBOM)
            lst2missing.append(each)
            lst3.append(each.drawingVersionBOM)
    l1Cond = all(lst1)
    l2Cond = all(isinstance(i, str) for i in lst2)
    l3Cond = all(isinstance(i, str) for i in lst3)
    
    print(4*'\n')
    for i in range(2): print(61*'*')
    print(22*'*' , 'RESULTS SUMMARY', 22*'*')
    for i in range(2): print(61*'*')
    print(2*'\n')
    
    if l1Cond:
        print('\n' + 41*'-' + '\n')
        print(7*'-' , 'Your package is completed'.upper(), 7*'-')
        print('\n' + 41*'-'+ '\n')
    else:
        print('\n' + 41*'-' + '\n')
        print(space, 'Your package is NOT completed;'.upper(), space)
        print('\n' + 41*'-' + '\n')
        print('please check report above for find missing drws'.upper(),
              'following drawing missed:', '\n')

        for i in range(len(lst1)):
            if lst1[i] is False:
                print('\n - ', lst1missing[i].name)
                if lst1missing[i].isPDFfile is not True:
                    print('lack of PDF')
                elif lst1missing[i].isDWGfile is not True:
                    print('lack of DWG')
                elif lst1missing[i].isSTEPfile is not True:
                    print('lack of STEP')
                elif lst1missing[i].isDXFfile is not True:
                    print('lack of DXF')
                else:
                    print("Wrong: isPDFfile, isDWGfile, isSTEPfile, isDXFfile assignment")
    if l2Cond and l3Cond:
        print(space, 'PDF and DWG revision and versions matches', space)
    else: 
        print("\n")
        print('Not all PDF and DWG revisions and versions matches')
        print('Please check visions and revisins for following PDF and DWG files')
        for i in range(len(lst2)):
            if lst2missing[i].drawingRevisionBOM is False:
                print(' - ', lst2missing[i].name)

def PrintExtraFilesNeededToBeChecked(files: dict, format) -> print:
    # does not work fully good for func there is no difference
    # for P-0001030509_A_1.dxf and P-0001030509_A_1_copy.dxf
    if len(files) != 0:
        print(f'\nConsider if you need following {format} files (QTY = {len(files)}) in folder:')
        for item in files:
            print(f' - {item}')
    else:
        print(f'No extra {format} files in directory.')
