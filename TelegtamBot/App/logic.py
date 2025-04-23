import openpyxl


#Назавние таблиц 
list_tabels =["Отчет по домашним заданиям.xlsx"
            ,"Отчетпопосещаемостистудентов.xlsx"
              ,"Отчетпостудентам.xlsx"
              ,"Отчет по дз (6 задание) .xlsx"]
list_oret_nuber  =[]
# нахождени процента 
def percentage(number_verified, number_plann):
    number_average_score: float = (number_verified /number_plann)*100

    number_average_score_lod = (number_average_score * 10) % 10

    if int(number_average_score_lod) >= 5.0:

        return int(number_average_score + 1)

    else:

        return int(number_average_score)
# понть какую таблицу окрыть 
def open_tabel(relut:str,list_search)->str:
    if relut in ("mouth spand" ,"day spand" , "week spand"):
        return list_search[0]
    elif relut=="percentage_group_tectecr":
        return list_search[1]
    elif relut =="percentage_of_homework_per_mont":
        return list_search[3]
    elif relut =="student_assessment":
        return list_search[2]
# Нахождени листа кторый пришёл на результат 
def provert_list(list_text:list)->str:
    len_list_seract = len(list_text)
    match len_list_seract:

        case  4:
            for i in range(len_list_seract):
                match list_text[i]:
                    case "Месяц":
                        return "mouth spand"
                    case "Неделя":
                        return "week spand"
                    case "День":
                        return "day spand"            
        case 3: 

            return "percentage_of_homework_per_mont"
        
        case 2:

            return "percentage_group_tectecr"
        
        case 6:

            return "student_assessment"

#Функци поиска по листу  
def search_List_text(file,list_search:list):
        list_text = []

        print(f"{type(list_search)}")
        print(list_search)
        relut =  provert_list(list_search)

        print(relut)

      
        col_arguments = []

        relut_tabel = open_tabel(relut,list_tabels)

        print(relut_tabel)

        
        print(f"{type(relut_tabel)}")

        worbook = openpyxl.open(relut_tabel)

        worksheet = worbook.active
        print(worksheet.max_row)
        
        # Поиск аргументов 
        for row in range(1, worksheet.max_row):

            for col in range(0,worksheet.max_column):

                if relut in("mouth spand " ,"day spand" "week spand"):

                    if worksheet[row][col].value == list_search[0]:

                        col_arguments.insert(0,col)

                            

                    elif worksheet[row][col].value == list_search[3]:
                    

                        col_arguments.append(col)
                   
                    elif (worksheet[row][col].value == list_search[1]
                        or worksheet[row][col].value == list_search[2]) :

                        col_arguments.append(col)
                        

                    elif(len(col_arguments)==4):

                        break
                
                elif relut == "percentage_group_tectecr":

                    if worksheet[row][col].value == list_search[1]:

                        col_arguments.append(col)
                

                    elif worksheet[row][col].value == list_search[0]:

                        col_arguments.append(col)

                    elif len(col_arguments) == 2:

                        break
                       
                elif relut == "student_assessment":

                    if worksheet[row][col].value == list_search[0]:

                        col_arguments.append(col)
                       
                    elif worksheet[row][col].value == list_search[1]:
                       
                       col_arguments.append(col)
                    elif (
                        (worksheet[row][col].value == list_search[2])or
                        (worksheet[row][col].value == list_search[3])or
                        (worksheet[row][col].value == list_search[4])):
                        col_arguments.append(col)
                       
                elif relut =="percentage_of_homework_per_mont":

                    if worksheet[row][col].value == list_search[0]:

                        col_arguments.append(col)

                    elif worksheet[row][col].value == list_search[1]:

                        col_arguments.append(col)

                    elif worksheet[row][col].value == list_search[2]:

                        col_arguments.append(col)

        print(col_arguments)

                        
                

                            
        
       # Вывод сообщени 
        if relut=="mouth spand" or  relut=="day spand" or relut == "week spand" or relut =="percentage_group_tectecr":
            for row in range(3,worksheet.max_row):
                if col_arguments[0] != 0 or col_arguments[1] == 0 and len(col_arguments) == 0:
                    text = "Таких данных нет в документе "

                    list_text.append(text)

                    return list_text
                
                else:
                    
                    if relut=="mouth spand" or  relut=="day spand" or relut == "week spand":
                        worksheet_row_col_fio_teacher = worksheet[row][col_arguments[1]].value
                        worksheet_row_col_relet_1 = int(worksheet[row][col_arguments[2]].value)
                        worksheet_row_col_relet_2 = int(worksheet[row][col_arguments[3]].value)
                        if percentage(worksheet_row_col_relet_1, worksheet_row_col_relet_2) < 75:
                            text = f"""Добрый день - {worksheet_row_col_fio_teacher}. У Вас не выполнена норма по {list_search[1]} ДЗ студентов. Нужно исправить это.У Вас  процент проверки ДЗ: {percentage(worksheet_row_col_relet_1, worksheet_row_col_relet_2)}%."""
                            list_text.append(text)
                        else:
                            text = "ок"
                    elif relut =="percentage_group_tectecr":
                        worksheet_row_col_fio_teacher = worksheet[row][col_arguments[0]].value
                        worksheet_row_col_procent_teacher = int(worksheet[row][col_arguments[1]].value.strip("%"))
                        worksheet_row_col_procent_teacher_finall = int(worksheet[worksheet.max_row][col_arguments[1]].value)
                        if worksheet_row_col_procent_teacher < worksheet_row_col_procent_teacher_finall:
                            text = f"""Добрый день {worksheet_row_col_fio_teacher}! У вас плохая посещаемость предмета на вашей паре.Вот  {worksheet_row_col_procent_teacher}%."""
                            list_text.append(text)
                        else:
                            text = "Ок"
        elif relut == "student_assessment" or  relut=="percentage_of_homework_per_mont":
            for row in range(2, worksheet.max_row):
                if relut == "student_assessment":
                    if col_arguments[0] == 0 and col_arguments[1] != 0  and  len(col_arguments) != 0:
                        worksheet_row_col_name_student = worksheet[row][col_arguments[0] ].value
                        worksheet_row_col_grop = worksheet[row][col_arguments[1]].value
                        worksheet_row_col_homework = int(worksheet[row][col_arguments[2]].value)
                        worksheet_row_col_classroom = int(worksheet[row][col_arguments[3]].value)
                        if (worksheet_row_col_homework < 3 or worksheet_row_col_classroom < 3
                                or percentage(worksheet_row_col_homework, worksheet_row_col_classroom) < 3):
                            text = f"""Cтудент:{worksheet_row_col_name_student} - {worksheet_row_col_grop} Дз- {worksheet_row_col_homework} или КЛ_Р- {worksheet_row_col_classroom}.Как поступить в данной ситуации?"""
                            list_text.append(text)
                        else:
                            continue
                    else:
                        text = "Таких данных нет в документе "
                        list_text.append(text)
                        return list_text
                if relut == "percentage_of_homework_per_mont":
                    if len(col_arguments) != 0:
                        worksheet_row_col_name_student = worksheet[row][col_arguments[0]].value
                        worksheet_row_col_grop = worksheet[row][col_arguments[1]].value
                        worksheet_row_col_homework = int(worksheet[row][col_arguments[2]].value)
                    if worksheet_row_col_homework < 50:
                        text = (
                        f"""Студент:{worksheet_row_col_name_student}-{worksheet_row_col_grop} и процент дз:{worksheet_row_col_homework}%.""")
                        list_text.append(text)
        

        worbook.close()
        return list_text
           
            

def search_average_rating_grop(file):
    text = ""
    list_text = []
    list_procent= []
    list_teacher= []

    worbook = openpyxl.open("Отчетпопосещаемостистудентов.xlsx")
    worksheet = worbook.active

    col_percent = 0
    col_teacher= 0
    for row in range(1, worksheet.max_row):
        for col in range(0, worksheet.max_column):

            if worksheet[row][col].value == "Средняя посещаемость":
                col_percent = col
                print(col_percent)
                break

            elif worksheet[row][col].value == "ФИО преподавателя":
                col_teacher = col
                print(col_teacher)

    for row in range(3,worksheet.max_row+1):
        list_procent.append(worksheet[row][col_percent].value)
        list_teacher.append(worksheet[row][col_teacher].value)

    for len_list in range(len(list_procent)-1):
        if col_percent != 0 and col_teacher == 0:
            worksheet_row_col_fio_teacher = list_teacher[len_list]
            worksheet_row_col_procent_teacher = int(list_procent[len_list].strip("%"))
            worksheet_row_col_procent_teacher_finall = int(list_procent[len(list_procent) - 1])
            if worksheet_row_col_procent_teacher < worksheet_row_col_procent_teacher_finall:
                text = f"""Добрый день {worksheet_row_col_fio_teacher}!У вас плохая посещаемость предмета на вашей паре.Вот  {worksheet_row_col_procent_teacher}%."""
                list_text.append(text)
            else:
                text = "Ок"
        else:
            text = "Таких данных нет в документе "
            list_text.append(text)
            return list_text

    worbook.close()
    print(list_text)
    return list_text



def search_student_assessment(file):
    list_text = []
    list_search = ["FIO","Группа","Classroom","Homework","Average score","Exam"]
    col_fio = 0
    col_group = 0
    col_assessment = []
    worbook = openpyxl.open("Отчетпостудентам.xlsx")
    worksheet = worbook.active
    for row in range(1, worksheet.max_row):
        for col in range(0, worksheet.max_column):

            if worksheet[row][col].value == list_search[0]:
                col_fio = col
                print(col_fio)
            elif worksheet[row][col].value == list_search[1]:
                col_group = col
                print(col_group)
            elif ((worksheet[row][col].value == list_search[2])or
                  (worksheet[row][col].value == list_search[3])or
                  (worksheet[row][col].value == list_search[4])):
                col_assessment.append(col)
                print(col_assessment)

    for row in range(2, worksheet.max_row):
        if col_fio == 0 and col_group != 0  and  len(col_assessment) != 0:
            worksheet_row_col_name_student = worksheet[row][col_fio].value
            worksheet_row_col_grop = worksheet[row][col_group].value
            worksheet_row_col_homework = int(worksheet[row][col_assessment[0]].value)
            worksheet_row_col_classroom = int(worksheet[row][col_assessment[1]].value)
            if (worksheet_row_col_homework < 3 or worksheet_row_col_classroom < 3
                    or (worksheet_row_col_homework, worksheet_row_col_classroom) < 3):
                text = f"""Cтудент:{worksheet_row_col_name_student} - {worksheet_row_col_grop} Дз- {worksheet_row_col_homework} или КЛ_Р- {worksheet_row_col_classroom}.Как поступить в данной ситуации?"""
                list_text.append(text)
            else:
                continue
        else:
            text = "Таких данных нет в документе "
            list_text.append(text)
            return list_text

    worbook.close()
    return list_text

def search_percentage_of_homework_per_month(file):
    list_text = []
    list_search = ["FIO","Группа","Percentage Homework"]
    col_assessment = []
    worbook = openpyxl.open("Отчет по дз (6 задание) .xlsx")
    worksheet = worbook.active
    for row in range(1, worksheet.max_row):
        for col in range(0, worksheet.max_column):
            if worksheet[row][col].value == list_search[0]:
                col_assessment.append(col)
            elif worksheet[row][col].value == list_search[1]:
                col_assessment.append(col)
            elif worksheet[row][col].value == list_search[2]:
                col_assessment.append(col)
                break
    print(col_assessment)

    for row in range(2, worksheet.max_row):
        if len(col_assessment) != 0:
            worksheet_row_col_name_student = worksheet[row][col_assessment[0]].value
            worksheet_row_col_grop = worksheet[row][col_assessment[1]].value
            worksheet_row_col_homework = int(worksheet[row][col_assessment[2]].value)
            print(f"{worksheet_row_col_homework}")
            if worksheet_row_col_homework < 50:
                text = (
                f"""Студент:{worksheet_row_col_name_student}-{worksheet_row_col_grop} и процент дз:{worksheet_row_col_homework}%.""")
                list_text.append(text)
        else:
            text = "Таких данных нет в документе "
            list_text.append(text)
            return list_text

    print(len(list_text))
    worbook.close()
    return list_text