# DrawingQtyCheck Application

## Project description

Project is a checker of completeness package for subsupplier. During cooperation with subsupliers there is need to order parts. Program helps to identify if all part in package is inluded and if not it shows which files are missing. It helps to reduce project errors such as parts missing, therefore it reduces total project cost.<br>

### Mechanical engineering background
Assembly of machines contains of components which has to be manufactured. Each compononent has its digital representation in project which has to be sent to subsuplier in separate file.  This script compare output of CAD list with package that will be sent.
Application check whether package contains all necessery files.<br>
image-1

### Data input
Design (using CAD software) has its output (Bill Of Materials- BOM) that can be represented as .csv file (BOM). Appplication compare BOM to package created by designer, which is folder of PDF, DWG, STEP and DXF files. Program checks all files and sort it.
If part is Custom part it checks if files are in representation of PDF, DWG, STEP
If prefabricated part is made from 2D stock then apps checks if files are in representation of PDF, DWG, STEP and DXF.<br>
image-2

## How to use App
1. Compile "main.py".<br>
2. Program will generate following output:
- if all files are included App prints:
```
YOUR PACKAGE IS COMPLETED
```

- if allfiles are not included App prints:
```
YOUR PACKAGE IS NOT COMPLETED
```
and shows which files are missing
- it will show which files are not neccessery (extra files)