'''
    Requirement:
                pip install pikepdf
'''
import pikepdf
import os

'''
    For the given path, get the List of all PDF files in the directory tree
                                    and
                                unlock them
'''
dirName = input('please input the path to the directory of the PDFs:\n')
Password = input('please input the password:\n')
pdf = '.pdf'

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


def main():
    global dirName
    global Password
    # Get the list of all files in directory tree at given path
    listOfFiles = getListOfFiles(dirName)
    # Print the files
    for elem in listOfFiles:
        if elem.endswith(pdf)
            p = pikepdf.open(elem, password=Password, allow_overwriting_input=True)
            p.save(elem)
            print('"' + elem + '"' + ' has been decrypted successfully.')
        else:
            print(elem + ' is not a PDF file.')
    print("****************")


if __name__ == '__main__':
    main()
