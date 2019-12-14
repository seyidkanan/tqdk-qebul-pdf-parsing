import re
import csv

txt_file_path = 'MyFile.txt'
text_file = open(txt_file_path, "r")

for line in text_file:
    if len(line) > 0:
        print(line)

        ixtisas_id = ""
        ixtisas_eyani_or_qiyabi = ""
        ixtisas_adi = ""
        ixtisas_pullu_kechid_bali = ""
        ixtisas_pulsuz_kechid_bali = ""

        split_lines = line.split()

        ixtisas_adin_elave_elesin = False

        for string in split_lines:
            if len(string) == 1 and (string == "Ə" or string == "Q"):
                ixtisas_eyani_or_qiyabi = string
                ixtisas_adin_elave_elesin = False

            if ixtisas_adin_elave_elesin == True:
                ixtisas_adi = ixtisas_adi + " " + string

            if (len(string) == 6 and re.match(r'^([\s\d]+)$', string)) or \
                    (len(string) == 8 and re.match(r'^([\s\d]+)$', string.replace("*", ""))) or \
                    (len(string) == 7 and re.match(r'^([\s\d]+)$', string.replace("*", ""))):
                ixtisas_id = string
                ixtisas_adin_elave_elesin = True

            if len(string) == 3 and re.match(r'^([\s\d]+)$', string):
                ixtisas_pullu_kechid_bali = string

            if len(string) == 5 and string.startswith("(") and string.endswith(")"):
                ixtisas_pulsuz_kechid_bali = string.replace("(", "").replace(")", "")

            if len(string) == 1 and (string.__eq__("(") or string.__eq__("-") or string.__eq__(")")):
                ixtisas_pulsuz_kechid_bali = " - "

        if len(ixtisas_id) > 0:
            with open('data.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([ixtisas_id, ixtisas_adi, ixtisas_eyani_or_qiyabi, ixtisas_pullu_kechid_bali,
                                 ixtisas_pulsuz_kechid_bali])
