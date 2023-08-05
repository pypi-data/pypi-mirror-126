import pandas
from re import match
from loguru import logger

class UtilsProperty():
    def getDataTypes(properties:dict) -> dict:
        """
        Sorts the property types and returns a dictionary of those properties 
        that are not of type STRING.
        """ 
        propertyTypes = {'Boolean': [], 'Numeric': [], 'DateTime': [], 'String': [], 'Unknown': []}
        for property in properties:
            if property['dataType'] in ['DATETIME, DATETIMEOFFSET']:
                propertyTypes['DateTime'].append(property['name'])
            elif property['dataType'] == 'BOOLEAN':
                propertyTypes['Boolean'].append(property['name'])
            elif property['dataType'] in ['INT', 'LONG', 'DECIMAL']:
                propertyTypes['Numeric'].append(property['name'])
                
            elif property['dataType'] == 'STRING':
                propertyTypes['String'].append(property['name'])
            else: 
                propertyTypes['Unknown'].append(property['name'])
        return propertyTypes

    def getArrays(properties:dict) -> list:
        """ Lists properties that are arrays (isArray) """

        p = [property['name'] for property in properties if property['isArray'] == True]
        return p

    def getNullables(properties:dict) -> list:
        """ Lists properties that are nullable """

        p = [property['name'] for property in properties if property['nullable'] == True]
        return p

    def _transformBool(value:str):
        trueValues = ['ja', 'Ja', 'yes', 'Yes', 'True', 'true', 1]
        falseValues = ['nein', 'Nein', 'no', 'No', 'false','False',0]
        if value in trueValues:
            return True
        elif value in falseValues:
            return False
        return None

    def _isInt(n:str):
        return bool(match(r'-?\d+$', n))

    def _isFloat(n:str) -> bool:
        return bool(match(r'-?\d+(\.\d+)$', n))

    def _transformNumeric(value:str):
        if UtilsProperty._isInt(value):
            return int(value)
        elif UtilsProperty._isFloat(value):
            return float(value)
        else:
            logger.warning(f"'{value}' is not of numeric data type!")

    def _checkIsList(pythonList:str) -> bool:
        if pythonList[0] != '[':
            return False
        elif pythonList[-1] != ']':
            return False
        else:
            return True

    def _transformList(pythonList:str, propertyType:str) -> list:
        """ Transforms a String into a Python list"""
        if not UtilsProperty._checkIsList(pythonList):
            logger.warning(f"Value '{pythonList}' is not array type!")

        pythonList = pythonList[1:-1].split(',')
        pythonList = [element.strip() for element in pythonList]

        _pythonList = []
        for element in pythonList:
            if propertyType == 'Numeric':
                _pythonList.append(UtilsProperty._transformNumeric(element))
            elif propertyType == 'Boolean':
                _pythonList.append(UtilsProperty._transformBool(element))
            else:
                _pythonList.append(str(element))

        return _pythonList

class FileUtils(UtilsProperty):

    def _createBasicItems(content:list, dataType:dict, isArray:list, nullable:list):
        itemList = []
        header = content[0]
        for i, row in enumerate(content):
            itemOkay = True # is changed to false, if certain criteria are not met -> warning message, next item
            if i == 0: continue
            if len(row) < 1: continue
            else:
                item = {}
                for j, field in enumerate(row):
                    if not field:
                        if header[j] in nullable:
                            continue
                        elif header[j] not in nullable and len(field) > 0:
                            logger.warning(f"Value missing for non nullable {header[j]}. Item from line {i} not imported.")
                            itemOkay = False
                            break
                        else:
                            pass
                    else:
                        if header[j] in dataType['Boolean']:
                            if header[j] in isArray:
                                item.setdefault(header[j], UtilsProperty._transformList(field, 'Boolean'))
                            else: 
                                item.setdefault(header[j], UtilsProperty._transformBool(field))
                        elif header[j] in dataType['Numeric']:
                            if header[j] in isArray:
                                item.setdefault(header[j], UtilsProperty._transformList(field,'Numeric'))
                            else:
                                item.setdefault(header[j], UtilsProperty._transformNumeric(field))
                        elif header[j] in dataType['DateTime']:
                            if header[j] in isArray:
                                item.setdefault(header[j], UtilsProperty._transformList(field, 'DateTime'))
                            else:
                                item.setdefault(header[j], UtilsProperty._convertTimestamp(field, timeZone))
                        else:
                            if header[j] in isArray:
                                item.setdefault(header[j], UtilsProperty._transformList(field, 'String'))
                            else:
                                item.setdefault(header[j], field)
                if itemOkay and len(item) > 0:
                    itemList.append(item)

        return itemList

    def _comparePropertiesBasic(properties:pandas.DataFrame, header:list) -> None:
        """ Compares header with requested properties from a basic inventory. """

        #properties = [i for i in properties.index if i[0] != '_'] # get rid of fields beginning with underscores
        properties = set(properties['name'])
        header = set(header)
        return header.difference(properties)

    def _analyzeProperties(inventoryName:str, properties:pandas.DataFrame) -> tuple:
        """ Analyzes inventory properties and returns dictionaries to each property attribute """

        properties = properties[['name', 'dataType', 'isArray', 'nullable']].to_dict('records')
        dataType = UtilsProperty.getDataTypes(properties)
        isArray = UtilsProperty.getArrays(properties)
        nullable = UtilsProperty.getNullables(properties)

        return dataType, isArray, nullable

