import os

folder = 'pasta/que/voce/deseja/'
texto = 'Teste_'

for index, file_name in enumerate(os.listdir(folder), start=0):
    old_name = os.path.join(folder, file_name)
    new_name = os.path.join(folder, f'{texto}{index}.py')
    os.rename(old_name, new_name)

print(os.listdir(folder))