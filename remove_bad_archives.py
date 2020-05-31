import zipfile
import rarfile
import tarfile
import os


os.getcwd()
os.chdir("C:\\Users\\andom\\архивы")
folder = os.listdir("C:\\Users\\andom\\архивы")
for file in folder:
    ans_zip = zipfile.is_zipfile(file)
    ans_rar = rarfile.is_rarfile(file)
    ans_tar = tarfile.is_tarfile(file)
    if ans_zip is False and ans_rar is False and  ans_tar is False:
        os.remove(file)
