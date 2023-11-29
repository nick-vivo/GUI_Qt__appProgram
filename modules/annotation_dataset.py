import os
import pandas as pd

def annotation_dataset(source_dir: str, name_annotation: str) -> pd.DataFrame:
    """
    Функция принимает путь к датасету и будущее имя папки с аннотацией

    Создаст аннотацию на оригинальный датасет
    """

    for i in range(1, 6):
        
        if not os.path.exists( os.path.join(source_dir, str(i)) ):
            raise Exception("Is doesn't live")


    fieldnames = ['abs_path', 'rel_path', "class"]
    
    data = pd.DataFrame(columns=fieldnames)

    index = 0
    
    for i in range(1, 6):


        files = os.listdir( os.path.join(source_dir, str(i)) )

        files.sort()


        for file in files:
            

            new_row = { fieldnames[0]:os.path.join( os.getcwd(), source_dir, str(i), file), fieldnames[1]:os.path.join(source_dir, str(i), file), fieldnames[2]:str(i) }

            data.loc[index] = new_row

            index += 1

    data.to_csv(name_annotation, index=False)

    return data


if __name__ == '__main__':
    print("Annotation dataset")

# def dataset_aloin(source_dir: str) -> str:


#     for i in range(1, 6):
        
#         if not os.path.exists( os.path.join(source_dir, str(i)) ):
#             raise Exception("Is doesn't live")
    
#     cataloge = source_dir + ".aloin"

#     os.mkdir(cataloge)

#     for i in range(1, 6):


#         files = os.listdir( os.path.join(source_dir, str(i)) )

#         files.sort()

#         for file in files:


#             source = os.path.join( source_dir, str(i), file )

#             destination = os.path.join( cataloge, str(i) + "_" + file )

#             shutil.copyfile(source, destination)

#     return cataloge


# def annotation_aloin(source_dir: str, name_annotation: str) -> pd.DataFrame:

#     if not os.path.exists( os.path.join(source_dir) ):
#         raise Exception("Is doesn't live")


#     fieldnames = ['abs_path', 'rel_path', "class"]
    
#     data = pd.DataFrame(columns=fieldnames)
    
#     files = os.listdir( os.path.join(source_dir) )

#     files.sort()

#     index = 0

#     for file in files:
            

#         new_row = { fieldnames[0]:os.path.join( os.getcwd(), source_dir, file), fieldnames[1]:os.path.join(source_dir, file), fieldnames[2]:file[0] }

#         data.loc[index] = new_row

#         index += 1

#     data.to_csv(name_annotation, index=False)

#     return data


# def dataset_random_annotation(source_dir: str, name_annotation: str) -> pd.DataFrame:


#     for i in range(1, 6):
        
#         if not os.path.exists( os.path.join(source_dir, str(i)) ):
#             raise Exception("Is doesn't live")
    
#     cataloge = source_dir + ".random"
#     os.mkdir(cataloge)

#     data = annotation_dataset(source_dir, "ARBITRASHIK")
#     os.remove("ARBITRASHIK")


#     fieldnames = ['abs_path', 'rel_path', "class"]    

#     data_2 = pd.DataFrame(columns=fieldnames)


#     random_ls = data[['rel_path', 'class']].values
    
#     indexes = list(range(len(random_ls)))

#     random.shuffle(indexes)

#     randomized_data = [random_ls[i] for i in indexes]

#     index = 0

#     for file in randomized_data:

    
#         source = os.path.join( file[0] )

#         destination = os.path.join( cataloge, str(index).rjust(5, "0") )

#         new_row = [ os.path.join( os.getcwd(), destination), os.path.join(destination),  file[1]]

#         data_2.loc[index] = new_row

#         index += 1

#         shutil.copyfile(source, destination)
    
#     data_2.to_csv(name_annotation, index=False)

#     return data_2
