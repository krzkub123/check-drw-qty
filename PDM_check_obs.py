"""
 --- created by: krzysztof.kubacki ---

"""

import pandas as pd
import os

class PDMComponent:
    def __init__(self, level: int, fileName: str, number: str, description: str,
                 qty: int, state: str, version: int, revision: str,
                 revisionBy: str, vendor: str, itemID: str, price: float,
                 deliveryTime: float, typeSld: str, plateThickness: float,
                 sparePart: bool, weight: float, material: str, manufacturingMethod: str,
                 surfaceTreatment: str, project: str, projectName: str, projectNumber: str):
        self.level = level
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
