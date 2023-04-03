"""
 -- created by: krzysztof.kubacki ---
"""
# --- INITIALIZE GLOBAL VARIABLES ---
# KRKU modules

# Open-source modules

# path properties
global folder, strBOMCSV, strBOMDPMCSV
folder = "./data"
strBOMCSV = "input_BOM.csv"
strBOMDPMCSV = "input_BOM_PDM.csv"


# declare global value
# name of columns from SolidWorks
global fileNameColStr, customPrtAsmColStr, sheetMetColStr
global descriptionColStr, typePartColStr, folderWithPackage
global typeFilesToBeChecked, typeFilesNotToBeChecked, typesOfFiles
fileNameColStr = "SW-File Name(File Name)"

customPrtAsmColStr = "Type"
typeFilesNotToBeChecked = ('Purchasing', 'Standard', 'Other', None)
typeFilesToBeChecked = ('Custom Part / Assembly')

sheetMetColStr = "Sheet Metal"
descriptionColStr = "Description"
typePartColStr = "Type"
folderWithPackage = "data"

typesOfFiles = ("PDF", "DWG", "STEP", "DXF")

# --- PDM properties ---
global PDMfileName, PDMnumber, PDMdescription, PDMqty  # , PDM level parts only BOM
global PDMstate, PDMversion, PDMrevision, PDMrevisionBy, PDMvendor
global PDMitemID, PDMprice, PDMdeliveryTime, PDMtypeSld, PDMplateThickness
global PDMsparePart, PDMweight, PDMmaterial, PDMmanufacturingMethod
global PDMsurfaceTreatment, PDMproject, PDMprojectName, PDMprojectNumber
global csvColumns
# PDMlevel = "Level" # PDM level parts only BOM
PDMfileName = "File Name"
PDMnumber = "Number"
PDMdescription = "Description"
PDMqty = "Qty"
PDMstate = "State"
PDMversion = "Version"
PDMrevision = "Revision"
PDMrevisionBy = "Revision By"
PDMvendor = "Vendor"
PDMitemID = "Item ID"
PDMprice = "Price"
PDMdeliveryTime = "Delivery time"
PDMtypeSld = "Type"
PDMplateThickness = "PlateThickness"
PDMsparePart = "Spare part"
PDMweight = "Weight"
PDMmaterial = "Material"
PDMmanufacturingMethod = "Manufaturing Method"
PDMsurfaceTreatment = "Surface Treatment"
PDMproject = "Project"
PDMprojectName = "Project Name"
PDMprojectNumber = "Project number"
csvColumns = ["File Name", "Number", "Description", "Qty",
            "State", "Version", "Revision", "Revision By", "Vendor",
            "Item ID", "Price", "Delivery time", "Type",
            "PlateThickness", "Spare part", "Weight", "Material",
            "Manufaturing Method", "Surface Treatment", "Project",
            "Project Name", "Project number"]
