import os, shutil
import re
from helper_functions import markdown_to_html_node


def copy_content(src,dist):
    if not os.path.exists(dist):
        os.mkdir(dist)
    for file in os.listdir(dist):
        file_path = os.path.join(dist,file)
        
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
            else:
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason %s" % (file_path, e))
        

    for file in os.listdir(src):
        file_path = os.path.join(src,file)
        
        try:
            if os.path.isfile(file_path):
                shutil.copy(file_path,dist)
                print("File %s has been copied" % file_path)
            else:
                os.mkdir(os.path.join(dist,file))
                print("Copying folder %s." % file_path)
                copy_content(file_path,os.path.join(dist,file))
        except Exception as e:
            print("Failed to copy %s. Reason %s" % (file_path, e))
            
            
def extract_title(markdown):
    with open(markdown) as file:
        content = file.read()
        file.close()
        if re.match(r"# ", content)== None:
            raise Exception("No Main header found")
        else:
            return re.match(r"\# .*",content).group()[2:]
            





def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as from_file:
        content = from_file.read()
        from_file.close()
    
    with open(template_path) as template_file:
        template = template_file.read()
        template_file.close()
    
    html = markdown_to_html_node(content).to_html()
    title = extract_title(from_path)
    template_with_title = template.replace("{{ Title }}", title)
    template_with_title_and_content = template_with_title.replace("{{ Content }}", html)
    template_with_title_and_content_and_basepath = template_with_title_and_content.replace("href=\"/", f"href=\"{basepath}")
    template_with_title_and_content_and_basepath2 = template_with_title_and_content_and_basepath.replace("src=\"/", f"src=\"{basepath}")
    
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    with open(os.path.join(dest_path, "index.html"), "w") as html_file:
        html_file.write(template_with_title_and_content_and_basepath2)
        html_file.close()
        


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dirs = os.listdir(dir_path_content)
    for dir in dirs:
        file_path = os.path.join(dir_path_content,dir)
        # print(file_path)
        if os.path.isfile(file_path):
            generate_page(file_path, template_path, dest_dir_path,basepath)
        else:
            new_dest_dir_path = os.path.join(dest_dir_path,dir)
            print("current dest", new_dest_dir_path)
            generate_pages_recursive(file_path,template_path, new_dest_dir_path,basepath)