import os
def make_folder(dealername):
    os.getcwd()
    #'C:\\Users\\corcoras\\Desktop\\FY14 INSTALLS'
    install_dir = 'C:\\Users\\corcoras\\Desktop\\FY14 INSTALLS'
    os.chdir(install_dir)
    #dealername = "Rene motors"
    dealername_no_space = dealername.replace(" ", "_")
    dealername_no_space
    #'Don_Ayres_Honda'
    dealer_folder = dealername_no_space[:1]
    dealer_folder
    #'D'
    os.chdir(dealer_folder)
    os.getcwd()
    #'C:\\Users\\corcoras\\Desktop\\FY14 INSTALLS\\D'
    dealername_spaces = dealername_no_space.replace("_", " ")
    dealername_spaces
    #'Don Ayres Honda'
    os.mkdir(dealername_spaces)
    os.chdir(dealername_spaces)
    os.getcwd()
    #'C:\\Users\\corcoras\\Desktop\\FY14 INSTALLS\\D\\Don Ayres Honda'
    os.mkdir("config")
    os.mkdir("original")
    os.mkdir("final")
    print(f"\nFolder was created : {install_dir}\{dealer_folder}\{dealername_spaces}")
