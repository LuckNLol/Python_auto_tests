import os

current_dir = os.path.abspath(os.path.dirname("Lesson2_step7_add_file"))
file_path = os.path.join(current_dir, 'file.txt')
# print(current_dir)
print(file_path)