Crawler README.md
===========================

########### Used Softwares and Environments
1. Windonws 10 OS
2. Python 3.5
3. Scrapy Crawler Framework
    Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide range of useful applications, 
    like data mining, information processing or historical archival.Even though Scrapy was originally designed for web scraping, 
    it can also be used to extract data using APIs (such as Amazon Associates Web Services) or as a general purpose web crawler.
    (Reference: https://docs.scrapy.org/en/latest/intro/overview.html)

########### Configuration and Installation
1. Install Python 3.5 // Install Python 3 Envrionment
    Downloading Python 3 installer from https://www.python.org/downloads/windows/  

2. Start cmd and confirm python 3 has been installed successfully

3. Enter instruction "python -m pip install --upgrade pip" // Update pip

4. Enter instruction "pip install wheel" // Install wheel
 
5. Enter instruction "pip install lxml" // Install lxml
 
6. Enter instruction "pip install twisted" // Install Twisted

7. Install Win32 for Python 3 // Install Pywin32
    Enter instruction "pip install win32"
    or
    Downloading Pywin32 for Python 3 from https://sourceforge.net/projects/pywin32/files/pywin32/Build%20220/ and install it 

8. Enter instruction "pip install scrapy" // Install Scrapy Framework

########### Structure of Crawler "IR Project" directory
├───Readme.md // Help
├───.idea
│       encodings.xml
│       IR Project.iml
│       misc.xml
│       modules.xml
│       workspace.xml
│
├───irproject
│   │   scrapy.cfg
│   │   term_frequency_matrix_query.py // program for converting intermediate json file crawled by crawler into term-frequency matrix
|   |   query.py // program for query engine
│   │
│   └───irproject
│       │   items.py
│       │   middlewares.py
│       │   pipelines.py
│       │   settings.py  // settings for crawler
│       │   __init__.py
│       │
│       ├───spiders
│       │   │   irproject.py  // main function for crawling
│       │   │   __init__.py
│       │   │
│       │   └───__pycache__
│       │           homework.cpython-37.pyc
│       │           irproject.cpython-37.pyc
│       │           __init__.cpython-37.pyc
│       │
│       └───__pycache__
│               settings.cpython-37.pyc
│               __init__.cpython-37.pyc
│
└───Results  // Directory showing the crawling results
        broken_urls.txt  // txt file containing broken urls 
        duplicated_urls.txt // txt file containing duplicated urls
        graphic_urls.txt // txt file containing graphic urls
        indexed_urls.txt // txt file containing indexed urls
        in_going_pdf_xlsx_urls.txt // txt file containing .pdf and .xlsx urls
        outgoing_urls.txt // txt file containing urls that is outside of domain
        Words_Frequency_Matrix_Porter.txt // txt file containing term-frequency matrix for stemmed scheme
        words_porter.json // json file containing each document with its stemmed words and frequency of its words in each document

########### Execution Instructions
1. Start cmd or terminal

2. Go into the irproject directory inside the IR Project directory // IR Project/irproject
    cd IR Project
    cd irproject

2.5 If you don't want to recrawl the data, you can skip step 3 and step 4.

3. Enter instruction "scrapy crawl irproject" // Starting the web crawler and collecting data

4. Enter instruction "python term_frequency_matrix.py" // Running the term-frequency matrix program to build term-frequency matrix

5. Enter instruction "python query.py". // Running query engine

6. Enter query until you want to shut down the query engine(instructure "stop") // Execute query

7. Repeat step 5 to run restart query engine. If you want to recollect the data, then repeat step 3. 

 