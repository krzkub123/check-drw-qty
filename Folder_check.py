"""
 -- created by: krzysztof.kubacki ---
"""
# --- FOLDER CHECK ---
# KRKU modules
from global_vars import *

# Open-source modules
import warnings

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

class projectComponent:
    """

    A class used to represent project components,
    attributes taken from BOM SolidWorks or PDM
    At later stage of program additional attr.
    are taken from files (e.g. Version/ Revision)

    Attributes
    ----------
    name: str
        Name of part (L-XXXXXXXXXX: eg. P-0001036611);
        taken from BOM SolidWorks column "SW-File Name(File Name)"
    typePrchCustom: str
        Type of part ('Purchasing', 'Standard', 'Custom Part / Assembly')
        taken from BOM SolidWorks column "Type"
    description: str
        Description of part (eg. "Roll spacer");
        taken from BOM SolidWorks column "Description"
    metalSheet: bool
        Check whether component is manufactured from metal sheet or not;
        taken from BOM SolidWorks column "Sheet Metal"
    nameLen: int
        Number length of name (P-0001036611 -> 12)
    revision: str
        Revision of file (taken from PDM) ("A")
        # TODO: import pdm properties: C++/ PDM API
    versionNumber: str
        Version of file (taken from PDM) ("12")
        # TODO: import pdm properties: C++
    isPDFfile: bool
        check if component has correspond package pdf file
        (e.g. P-0001036611 is there P-0001036611_X_1.pdf file)
    isDWGfile: bool
        check if component has correspond package dwg file
        (e.g. P-0001036611 is there P-0001036611_X_1.dwg file)
    isSTEPfile: bool
        check if component has correspond package dwg file
        (e.g. P-0001036611 is there P-0001036611_X_1.step file)
    isDXFfile: bool
        check if component (metal sheet) has correspond package dxf file
        (e.g. P-0001036611 is there P-0001036611_X_1.dxf file)
    allFilesIncluded: bool
        check if component has all neccessery file
    drawingRevisionBOM: str
        represent 2d revision (e.g. B)
    drawingVersionBOM: int
        represent 2d version (e.g. 12)
    model3dRevisionBOM: str
        represent 3d revision (e.g. C)
    model3dVersionBOM: int
        represent 3d version (e.g. 5)

    Methods
    ----------
    checkIfDocsAreComplete()
        Checks if all required files for type of component
        are included in package.
    """

    def __init__(self, name: str, description: str, revision: str,
                 versionNumber: str, typePrchCustom: str, metalSheet: str):
        
        self.name = name
        self.typePrchCustom = typePrchCustom
        self.description = description
        self.metalSheet = metalSheetBoolean(metalSheet)
        self.nameLen = len(name)
        self.revision = revision
        self.versionNumber = versionNumber
        initialCondition = None # condition to initialize following bool status
        self.isPDFfile = initialCondition
        self.isDWGfile = initialCondition
        self.isSTEPfile = initialCondition
        self.isDXFfile = initialCondition
        self.allFilesIncluded = initialCondition
        initialVerAndRev = -1
        self.drawingRevisionBOM = initialVerAndRev
        self.drawingVersionBOM = initialVerAndRev
        self.model3dRevisionBOM = initialVerAndRev
        self.model3dVersionBOM = initialVerAndRev


    def checkIfDocsAreComplete(self) -> bool:
        """
        Checks if all required files for type of component are included in package.

        Returns
        -------
        bool
            None -> not applied for this part (eg. Purchasing parts -pdf, dwg, step, dxf; custom not metal sheet)
            True -> all files are included
            False -> some of file is missing
        """
        global typeFilesToBeChecked, typeFilesNotToBeChecked
        if self.typePrchCustom in typeFilesNotToBeChecked:
            self.allFilesIncluded = None
        elif type(self.typePrchCustom) == float:
            self.typePrchCustom = None
            self.allFilesIncluded = None
        elif self.typePrchCustom in typeFilesToBeChecked:
            if self.metalSheet == True:
                if all([self.isPDFfile, self.isDWGfile, self.isSTEPfile, self.isDXFfile]):
                    self.allFilesIncluded = True
                else:
                    self.allFilesIncluded = False
            elif self.metalSheet == False:
                if all([self.isPDFfile, self.isDWGfile, self.isSTEPfile]):
                    self.allFilesIncluded = True
                else:
                    self.allFilesIncluded = False

    def assignVersionAndRevision(self, o) -> str:
        """
        Assign 2d/ 3d- revision and version. Its based of name file
        (e.g. P-0001009720_C_1.dwg -> Revision: C; Version: 1)

        Parameters
        ----------
        o : TYPE
            Component object

        Returns
        -------
        str
            self object 2d/3d revision and version
        """
        nameArr = o.pdf
        drwRevArr = o.drawingRevision
        drwVerArr = o.drawingVersion
        model3dRevArr = o.model3dRevision
        model3dVerArr = o.model3dVersion

        for i in range(len(nameArr)):
            # TODO            
            if self.name == nameArr[i][:len(self.name)]:
                # print('iteration num: ', i) # debugging
                try:
                    self.drawingRevisionBOM = drwRevArr[i]
                    self.drawingVersionBOM = drwVerArr[i]
                    self.model3dRevisionBOM = model3dRevArr[i]
                    self.model3dVersionBOM = model3dVerArr[i]
                    continue
                except:
                    continue  # do nothing

class packageFileComponent:
    """
    Short class description
    
    ...
 
    Attributes
    ----------
        pdf: list
	list of all files that are in "PDF" folder
        dwg: list
	list of all files that are in "DWG" folder
        step: list
	list of all files that are in "STEP" folder
        dxf: list
	list of all files that are in "DXF" folder
        pdfVersion: list
    list of all PDFs versions included in PDF package folder
        pdfRevision: list
    list of all PDFs revisions included in PDF package folder
        dwgVersion: list
    list of all DWGs versions included in DWG package folder
        dwgRevision: list
    list of all DWGs revisions included in DWG package folder
        stepVersion: list
    list of all STEPs versions included in STEP package folder
        stepRevision: list
    list of all STEPs revisions included in STEP package folder
        dxfVersion: list
    list of all DXFs versions included in DXF package folder
        dxfRevision: list
    list of all DXFs revisions included in DXF package folder
        model3dVersion: list
    list of all 3d Models version included in package folder
        model3dRevision: list
    list of all 3d Models revision included in package folder
        drawingVersion: list
    list of all drawings version included in package folder
        drawingRevision: list
    list of all drawings revision included in package folder
    Methos
    ----------
		method1(param)
	what it does and param to this ... etc
    """
    
    def __init__(self):
        self.pdf = []
        self.dwg = []
        self.step = []
        self.dxf = []
        self.pdfVersion = []
        self.pdfRevision = []
        self.dwgVersion = []
        self.dwgRevision = []
        self.stepVersion = []
        self.stepRevision = []
        self.dxfVersion = []
        self.dxfRevision = []
        self.model3dVersion = []
        self.model3dRevision = []
        self.drawingVersion = []
        self.drawingRevision = []
        
    def checkWhatVersionAndRevisionIs(self, listOfFiles: list, typeOfFile: str) -> list:
        """
        

        Parameters
        ----------
        typeOfFile : str
            Type of file from tuple: ("PDF", "DWG", "STEP", "DXF")

        Returns
        -------
        list
            DESCRIPTION.

        """
        
        def revisionCharacter(o: object, p: int)->str:
            """
            Check what revision of file is.
            Parameters
            ----------
            o : object
                Component from package
            p : int
                Position of character where version is encoded    
            Returns
            -------
            str
                Version which given file represents (P-0001009709_B_2.pdf -> "B")
            """
            return o[p+1:p+2]
        
        def versionCharacter(o: object, p: int)->str: 
            """
            Check what version of file is.
            
            Parameters
            ----------
            o : object
                Component from package
            p : int
                Position of character where version is encoded
                
            Returns
            -------
            str
                Revision which given file represents (P-0001009709_B_2.pdf -> "2")
            """
            return o[p+3:-4]
        
        def versionCharacterStep(o: object, p: int)->str: 
            """
            Check what version of step file is).
            
            Parameters
            ----------
            o : object
                Component from package
            p : int
                Position of character where version is encoded
                
            Returns
            -------
            str
                Revision which given file represents (P-0001009709_B_2.step -> "2")
            """
            return o[p+3:-5]
        
        def changeAttributiesEachTypeOfFile(self, fType: str, fileName: str) -> list:   
            """       
            Creates list of version and revision of files
            
            Parameters
            ----------
            fType : str
                type of file from tuple ("PDF", "DWG", "STEP", "DXF")
            fileName : string
                name of file from list

            Returns
            -------
            list
                Version and revision as List of \all file

            """
            pos = fileName.find('_')
            
            if fType == 'PDF':
                self.pdfRevision.append(revisionCharacter(fileName, pos)) # ea stands for P-0001009721_A_11.DXF
                self.pdfVersion.append(versionCharacter(fileName, pos))
            elif typeOfFile == "DWG":
                self.dwgRevision.append(revisionCharacter(fileName, pos))
                self.dwgVersion.append(versionCharacter(fileName, pos))
            elif typeOfFile == "STEP":
                self.stepRevision.append(revisionCharacter(fileName, pos))
                self.stepVersion.append(versionCharacterStep(fileName, pos)) # "STEP has 4 len of char"
            elif typeOfFile == "DXF":          
                self.dxfRevision.append(revisionCharacter(fileName, pos))
                self.dxfVersion.append(versionCharacter(fileName, pos))
        
        def SetRevAndVerOfFile(self, drwOr3d: str):# ('drawing', 'model')): # TODO check if model is metal sheet and then compare it with model step
            for i in range(len(self.pdf)):
                if drwOr3d == 'drawing':
                    a = self.pdfRevision[i]
                    b = self.dwgRevision[i]
                    c = self.pdfVersion[i]
                    d = self.dwgVersion[i]
                    if a == b:
                        Rev = a
                        self.drawingRevision.append(Rev)
                    else:
                        self.drawingRevision.append(False)
                    if c == d:
                        Ver = c
                        self.drawingVersion.append(Ver)
                    else:
                        self.drawingRevision.append(False)
                elif drwOr3d == 'model':
                    name = self.step[i][:-5]
                    metalSheetListTemp = [i[:-4] for i in self.dxf]
                    if name in metalSheetListTemp:      
                        a = self.stepRevision[i]
                        b = self.dxfRevision[i]
                        c = self.stepVersion[i]
                        d = self.dxfVersion[i]
                        if a == b:
                            Rev = a
                            self.model3dRevision.append(Rev)
                        else:
                            self.model3dRevision.append(False)
                        if c == d:
                            Ver = c
                            self.model3dVersion.append(Ver)
                        else:
                            self.model3dVersion.append(False)
                    else:
                        self.model3dRevision.append(self.stepRevision[i])
                        
        global typesOfFiles
        fType = typeOfFile        
        if fType == "PDF":
            lst = self.pdf
        elif fType == "DWG":
            lst = self.dwg
        elif fType == "STEP":
            lst = self.step
        elif fType == "DXF":
            lst = self.dxf
        else:
            warnings.warn('Given wrong file format')
            print('list in this scope: \n', lst)
        
        
        for i in range(len(lst)):
            changeAttributiesEachTypeOfFile(self, fType, lst[i])
              
        if len(self.pdfRevision) != 0 and len(self.dwgRevision) != 0 and (fType == "PDF" or fType == "DWG"):
            try:
                SetRevAndVerOfFile(self, 'drawing')
            except:
                print('There is an error and i dont know why, len of self.pdfRevision',
                      'is equal to zero in first loop, at second its correct')
                print("first loop dwg len: ", len(self.dwgRevision))
                print("first loop pdf len: ", len(self.pdfRevision))
        elif len(self.stepRevision) != 0 and len(self.dxfRevision) != 0 and (fType in ("STEP", "DXF")):
            try:
                SetRevAndVerOfFile(self, 'model')
            except:
                # fixed
                """
                print('There is an error and i dont know why, len of self.pdfRevision',
                      'is equal to zero in first loop, at second its correct')
                print("first loop dwg len: ", len(self.stepRevision))
                print("first loop pdf len: ", len(self.dxfRevision))
                """
