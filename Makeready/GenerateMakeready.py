import os
import shutil

unit = '1633'
bedrooms = 3

def copy_template_files(template_folder, target_folder):
    # Define files to copy and their respective counts
    files_to_copy = {
        'tplMakeReady.md': 1,
        'tplMakeReadyAudit.md': 1,
        'tplMakereadyKitchen.md': 1,
        'tplMakereadyLiving.md': 1,
        'tplMakereadyBath.md': 2,
        'tplMakereadyBed.md': bedrooms
    }
    fileNames = [
        unit,
        'makeready audit',
        'kitchen',
        'living',
        'bath 1',
        'bath 2',
        'bed 1',
        'bed 2',
        'bed 3'
    ]

    # Create the target folder if it doesn't exist
    os.makedirs(target_folder, exist_ok=True)

    # Iterate over files to copy
    iterator = 0
    for filename, count in files_to_copy.items():
        for i in range(1, count + 1):
            new_filename = f"" + fileNames[iterator] + ".md"
            src_file = os.path.join(template_folder, filename)
            dst_file = os.path.join(target_folder, new_filename)
            shutil.copy(src_file, dst_file)
            print(f"Copied {filename} to {new_filename}")
            iterator += 1

if __name__ == "__main__":
    # Specify the template folder relative to the script
    template_folder = os.path.join(os.path.dirname(__file__), "../$templates/makereadyTpl")

    # Specify the target folder (1801) relative to the script
    target_folder = os.path.join(os.path.dirname(__file__), unit)

    # Copy the template files to the target folder
    copy_template_files(template_folder, target_folder)

    print("Files copied successfully.")