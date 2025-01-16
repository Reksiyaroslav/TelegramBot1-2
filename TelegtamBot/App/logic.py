import openpyxl




def search_type_sq(file):
        list_search = ["Тема","Урок"]
        itor_text = []

        worbook = openpyxl.open("File\\Отчетпотемамзанятий.xlsx")
        worksheet = worbook.active
        col_subject = 0
        col_teacher  = 0
        for row in range(1, worksheet.max_row):
            for col in range(0,worksheet.max_column):
               if worksheet[row][col].value == "Тема урока":
                    col_subject = col
                    print(col_subject)

                    break
               elif worksheet[row][col].value == "ФИО преподавателя":
                   col_teacher = col
                   print(col_teacher)
               else:
                    "Темы нет в это файле "
                    continue

        for row in range(2,worksheet.max_row):
            if ((worksheet[row][col_subject].value in (list_search[0].title())
                    or worksheet[row][col_subject].value in (list_search[0].upper()))and 
                    (worksheet[row][col_subject].value in (list_search[1].title())
                    or  worksheet[row][col_subject].value in (list_search[1].upper()))):
                print(f"{worksheet[row][col_subject].value}\n")
                continue
            else:
                text = worksheet[row][col_subject].value

                itor_text.append(text)
                print(f"{itor_text}\t")
        worbook.close()
        return itor_text


def Percentage_of_Dz_Verified(number_verified, number_plann):
    number_average_score: float = (number_verified /number_plann)*100
    number_average_score_lod = (number_average_score * 10) % 10
    if int(number_average_score_lod) >= 5.0:
        return int(number_average_score + 1)
    else:
        return int(number_average_score)
def search_verified_homework(file,search_text_data):
        list_text = []
        list_search =["Проверено","План"]
        worbook = openpyxl.open("File\\Отчет по домашним заданиям.xlsx")
        worksheet = worbook.active
        col_data = 0
        col_teacher= 0
        col_arguments = []
        for row in range(1, worksheet.max_row):
            for col in range(0,worksheet.max_column):
               if worksheet[row][col].value == search_text_data:
                    col_data = col
                    print(col_data)
               elif worksheet[row][col].value == "ФИО преподавателя":
                   col_teacher = col
                   print(col_teacher)

               else:
                    "Темы нет в это файле "
                    continue
        for row in range(1, worksheet.max_row):
            for col in range(col_data, worksheet.max_column):
                if (worksheet[row][col].value == list_search[0]
                    or worksheet[row][col].value == list_search[1]) :
                    col_arguments.append( col)
                    print(col_arguments)
                elif(len(col_arguments)==2):
                    break
        for row in range(3, worksheet.max_row):
            if(Percentage_of_Dz_Verified(int(worksheet[row][col_arguments[0]].value),
                                         int(worksheet[row][col_arguments[1]].value))<75):
                text = f"Добрый время суток {worksheet[row][col_teacher].value} у вас не выполняна норма по проверке дз у студентах нужн что это делать  у вас токой {Percentage_of_Dz_Verified(int(worksheet[row][col_arguments[0]].value),
                                         int(worksheet[row][col_arguments[1]].value))}%"
                list_text.append(text)
            else:
                text = "ок"




        worbook.close()
        return list_text
def search_issued_homework(file,search_text_data):
        list_text = []
        list_search =["Выдано","План"]
        worbook = openpyxl.open("File\\Отчет по домашним заданиям.xlsx")
        worksheet = worbook.active
        col_data = 0
        col_teacher= 0
        col_arguments = []
        for row in range(1, worksheet.max_row):
            for col in range(0,worksheet.max_column):
               if worksheet[row][col].value == search_text_data:
                    col_data = col
                    print(col_data)
               elif worksheet[row][col].value == "ФИО преподавателя":
                   col_teacher = col
                   print(col_teacher)

               else:
                    "Темы нет в это файле "
                    continue
        for row in range(1, worksheet.max_row):
            for col in range(col_data, worksheet.max_column):
                if (worksheet[row][col].value == list_search[0]
                    or worksheet[row][col].value == list_search[1]) :
                    col_arguments.append( col)
                    print(col_arguments)
                elif(len(col_arguments)==2):
                    break
        for row in range(3, worksheet.max_row):
            if(Percentage_of_Dz_Verified(int(worksheet[row][col_arguments[0]].value),
                                         int(worksheet[row][col_arguments[1]].value))<75):
                text = f"Добрый время суток {worksheet[row][col_teacher].value} у вас не выполняна норма по проверке дз у студентах нужн что это делать  у вас токой {Percentage_of_Dz_Verified(int(worksheet[row][col_arguments[0]].value),
                                         int(worksheet[row][col_arguments[1]].value))}%"
                list_text.append(text)
            else:
                text = "ок"




        worbook.close()
        return list_text
def search_average_rating_grop(file ):
    text = ""
    list_text = []
    list_procent= []
    list_teacher= []
    worbook = openpyxl.open("File\\Отчетпопосещаемостистудентов.xlsx")
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
            else:
                inform_text = "Темы нет в это файле "
                continue
    for row in range(3,worksheet.max_row+1):

        list_procent.append(worksheet[row][col_percent].value)
        list_teacher.append(worksheet[row][col_teacher].value)

    for len_list in range(len(list_procent)-1):
        if int(list_procent[len_list].strip("%")) < int(list_procent[len(list_procent)-1]):
            text = (
                f"Добрый день {list_teacher[len_list]}! "
                f"У вас плохая посещаемость предмета на ваши пары. "
                f"Вот такая {list_procent[len_list]}.")
            print(text)
            list_text.append(text)

        else:
            text = "Ок"
    worbook.close()
    print(list_text)
    return list_text

def Average_score(number_homework,number_classwork ):
        number_average_score:float = (number_homework+number_classwork)/2
        number_average_score_lod = (number_average_score * 10)%10
        if int(number_average_score_lod) >= 5.0:
            return int(number_average_score+1)
        else:
            return int(number_average_score)
def search_student_assessment(file):


    list_text = []
    list_search = ["FIO","Группа","Classroom","Homework","Average score","Exam"]
    col_fio = 0
    col_group = 0
    col_assessment = []

    worbook = openpyxl.open("File\\Отчетпостудентам.xlsx")
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
            else:
                inform_text = "ДЗ,Классаня работа или Экзамен нет файле"
                continue

    for row in range(2, worksheet.max_row):
        if (int(worksheet[row][col_assessment[0]].value) < 3 or int(worksheet[row][col_assessment[1]].value < 3)
                or Average_score(int(worksheet[row][col_assessment[0]].value),int(worksheet[row][col_assessment[1]].value)) <3):
            text = f"Cтудент:{worksheet[row][col_fio].value},{worksheet[row][col_group].value} Дз-{worksheet[row][col_assessment[0]].value } или КЛ_Р-{ worksheet[row][col_assessment[1]].value}.Как поступить в данной ситуации?"
            list_text.append(text)
        else:
            continue

    worbook.close()
    print(list_text)
    return list_text