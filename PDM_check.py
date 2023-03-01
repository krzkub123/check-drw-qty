"""
 --- created by: krzysztof.kubacki ---
"""
# KRKU modules
from global_vars import *
# Open-source modules
from ast import Compare
from csv import reader
import pandas as pd
import os
import PyPDF2
from math import isnan

class PDMComponent:
    def __init__(self, fileName: str, number: str, description: str,
                 qty: int, state: str, version: int, revision: str,
                 revisionBy: str, vendor: str, itemID: str, price: float,
                 deliveryTime: float, typeSld: str, plateThickness: float,
                 sparePart: bool, weight: float, material: str, manufacturingMethod: str,
                 surfaceTreatment: str, project: str, projectName: str, projectNumber: str):
        # self.level = level  # We want to use parts only BOM (option in SolidWorks)
        self.fileName = fileName
        self.number = number
        self.description = description
        self.qty = qty
        self.state = state
        self.version = version
        self.revision = revision
        self.revisionBy = revisionBy
        self.vendor = vendor
        self.itemID = itemID
        self.price = price
        self.deliveryTime = deliveryTime
        self.typeSld = typeSld
        self.plateThickness = plateThickness
        self.sparePart = sparePart
        self.weight = weight
        self.material = material
        self.manufacturingMethod = manufacturingMethod
        self.surfaceTreatment = surfaceTreatment
        self.project = project
        self.projectName = projectName
        self.projectNumber = projectNumber

    def extractPDFsText(self):
        global typeFilesToBeChecked
        PDFFileName = compareFilesPDF(self.number)
        if (type(self.typeSld) == str) and isnan(self.version) == False:
            if (self.typeSld in typeFilesToBeChecked) and (type(self.typeSld) == str):
                filePath = './data/PDF/' + PDFFileName
                # try:
                reader = PyPDF2.PdfReader(filePath)
                num_of_pages = len(reader.pages)
                print('number of pages: ', num_of_pages)
                for pageID in range(num_of_pages):
                    page = reader.pages[0]
                    text = page.extract_text()
                    print(text)
                # except:
                print('-- No file: ', filePath)


def compareFilesPDF(number):
    l = len(str(number))
    global folderWithPackage
    lst = os.listdir('./' + folderWithPackage + '/PDF')
    shortLst = [i[:l] for i in lst]
    if number in shortLst:
        index = shortLst.index(number)
        return lst[index]



