from creation_functions import copy_content, generate_pages_recursive
import sys
def main():
    try:
        basepath = sys.argv[1]
    except:
        basepath ="/"
    copy_content("static","docs")
    generate_pages_recursive("content","template.html","docs",basepath)
    

main()