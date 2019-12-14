# tqdk-qebul-pdf-parsing

Datanı hazırlamaq üçün lazım olan addımlar:

1. pdf_to_txt_file.py faylında pdf faylının path-ın vermək.
2. Hansı fayla yazacaq onu qeyd eləmək.
3. txt_to_csv.py fayında txt faylına yığılan faylın adın qeyd eləmək.
4. txt faylını biraz edit eləmək lazım olacaq, 

**sektor üç  [ ] işarə ilə qeyd olunur**

[[[AZ]]]

**qrup nömrəsi iki [ ] işarə ilə qeyd olunur**

[[I]]

**Uni adı bir [ ] işarə ilə qeyd olunur**

[Bakı Dövlət Universiteti]

**İxtisas adı bir sətirdə aşağdakı nümunədəki kimi eləmək lazımdı.**

111114 Fizika müəllimliyi Ə 444 (444)

**Belə yazılan ixtisas adlarıda eyni qalır, script parse edə bilir.**

*148757 Fiziki tərbiyə və çağırışaqədərki hazırlıq (qızlar üçün fiziki tərbiyə) müəllimliyi Ə 57 (80)<br/>
**158452 Dizayn (tədris ingilis dilində) Ə 7/50 ( - )

5. txt_to_csv.py faylında hansı csv faylına yazılacaq onu qeyd edirik, fayla data üzərinə yazılır, əgər yenisin istəyirsizsə köhəni pozun və ya yeni fayl adı qeyd edin.
6. txt_to_csv.py run edin və csv faylını alın.
