import os, shutil


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