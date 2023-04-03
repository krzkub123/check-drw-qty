# DrawingQtyCheck Application

## Project description

Project is a checker of completeness package for subsupplier. During cooperation with subsupliers there is need to order parts. Program helps to identify if all part in package are inluded and if not it shows which files are missing. It helps to reduce project errors such as parts missing, therefore it reduces total project cost.<br>

### Mechanical engineering background
Assembly of machines contains of components which has to be manufactured. Each compononent has its digital representation in project which has to be sent to subsuplier in separate file.  This script compare output of CAD list with package from Product Data Management (PDM) that is outcome from project
Design -> DrawingQtyCheck Application -> Manufacturing
Application check whether package contains all necessery files.<br>
image-1

### Data input
Design (while using CAD and PDM software) has its output as Bill Of Materials (BOM) that can be represented as .csv file. Appplication compares BOM taken from PDM to package created by designer, which is folder containing files with extensions PDF, DWG, STEP and DXF files. Program checks all files exist.
If part is Custom part it checks if following files: PDF, DWG, STEP has its representation in package.
If prefabricated part is made from 2D sheet then Apps checks if files are in representation of PDF, DWG, STEP and DXF.<br>
image-2

## How to use App
1. Compile "main.py".<br>
2. Program will generate following output:
- if all files are included App prints:
```
YOUR PACKAGE IS COMPLETED
```
then Designer knows that package is ready to be sent.
- if allfiles are not included App prints:
```
YOUR PACKAGE IS NOT COMPLETED
```
and shows which files are missing.
then Designer can add those files which are missing.
- it will show which files are not neccessery (extra files).
then Designer can decide whether those files have to be deleted or can be sent.