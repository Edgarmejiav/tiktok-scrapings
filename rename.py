import os

folder_path = 'url'

mp4_files = [f for f in os.listdir(folder_path) if f.endswith('.mp4')]

for index, file_name in enumerate(mp4_files, start=1):
    new_name = f'family_guy_{index}.mp4'
    old_file = os.path.join(folder_path, file_name)
    new_file = os.path.join(folder_path, new_name)

    os.rename(old_file, new_file)
    print(f'Renamed: {file_name} -> {new_name}')
