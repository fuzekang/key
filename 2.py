import os
libs = {"Seaborn","Scrapy","pyspider","MyQR","sciPy",\
        "Mayavi","NLTK"}
try:
    for lib in libs:
        os.system("pip3 install "+lib)
    print("Successful")        
except:
    print("Failed Somehow")
