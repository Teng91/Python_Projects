# 讀檔案
file_list = [] # 新增一個list儲存所有檔案的名稱
def list_name():
    for n in range(141): # for迴圈依序讀取每一年的file
        year = 1880+n
        file_list.append('yob%d.txt'%(year)) # 每讀完一年就加入list
list_name()

# 載入所需套件
import math
import matplotlib.pyplot as plt

# 主程式
def male_count(): # 計算男新生兒總數
    """counting the total number of males in each year, and output a list"""
    total_male_count_list = [] # 新增一個list依序裝入每一年的男新生兒總數
    for file_name in file_list: # 依序讀取每一年的檔案
        male_count_of_a_year = 0 # 新增變數用來累計該年男新生兒總數
        fin = open(file_name)
        fobj = fin.readlines()
        for line in fobj:
            string = line.split(',') # 用split切出list裡面的資料轉成str
            if string[-2] == 'M': # 判斷是否為男性
                male_count_of_a_year += int(string[-1]) # 是男性的話加入男新生兒的總數
        total_male_count_list.append(male_count_of_a_year) # 加入男新生兒總數的list
    return total_male_count_list # 回傳每年男新生兒總數形成的list
            
def female_count(): # 計算女新生兒總數
    """counting the total number of females in each year, and output a list"""
    total_female_count_list = [] # 新增一個list裝file內的女新生兒總數
    for file_name in file_list: # 依序讀取每一年的檔案
        female_count_of_a_year = 0 # 新增變數用來累計該年女新生兒總數
        fin = open(file_name)
        fobj = fin.readlines()
        for line in fobj:
            string = line.split(',') # 用split切出list裡面的資料轉成str
            if string[-2] == 'F': # 判斷是否為女性
                female_count_of_a_year += int(string[-1]) # 是女性的話加入女新生兒的總數
        total_female_count_list.append(female_count_of_a_year) # 加入女新生兒總數的list
    return total_female_count_list # 回傳每年女新生兒總數形成的list

def both_count(): # 計算新生兒總數
    """counting the total number of babies in each year, and output a list"""
    total_both_count_list = [] # 新增一個list裝file內的新生兒總數
    for file_name in file_list: # 依序讀取每一年的檔案
        both_count_of_a_year = 0 # 新增變數用來累計該年新生兒總數
        fin = open(file_name)
        fobj = fin.readlines()
        for line in fobj:
            string = line.split(',') # 用split切出list裡面的資料轉成str
            both_count_of_a_year += int(string[-1]) # 儲存所有新生兒姓名的總數
        total_both_count_list.append(both_count_of_a_year) # 加入新生兒總數的list
    return total_both_count_list # 回傳每年新生兒總數形成的list

def male_diversity(): # 計算男新生兒姓名多樣性
    """calculate the Shannon index of males in each year, and output a list"""
    total_male_count_list = male_count()
    male_diversity = [] # 新增一個list裝每一年的男新生兒姓名多樣性指數
    for i in file_list:
        fin = open(i)
        fobj = fin.readlines()
        shannon_index = 0
        
        for line in fobj:
            string = line.split(',') # 用split切出list裡面的資料轉成str
            if string[-2] == 'M': # 判斷是否為男性
                factor = int(string[-1])/total_male_count_list[file_list.index(i)] # 每一年男新生兒姓名佔該年度男新生兒總數的比例
                shannon_index += (-1)*factor*math.log(factor) # 根據公式計算shannon_index
        male_diversity.append(shannon_index) # 加入男新生兒姓名多樣性指數
    return male_diversity

def female_diversity(): # 計算女新生兒姓名多樣性
    """calculate the Shannon index of females in each year, and output a list"""
    total_female_count_list = female_count()
    female_diversity = [] # 新增一個list裝每一年的女新生兒姓名多樣性指數
    for i in file_list:
        fin = open(i)
        fobj = fin.readlines()
        shannon_index = 0
        
        for line in fobj:
            string = line.split(',') # 用split切出list裡面的資料轉成str
            if string[-2] == 'F': # 判斷是否為女性
                factor = int(string[-1])/total_female_count_list[file_list.index(i)] # 每一年女新生兒姓名佔該年度女新生兒總數的比例
                shannon_index += (-1)*factor*math.log(factor) # 根據公式計算shannon_index
        female_diversity.append(shannon_index) # 加入女新生兒姓名多樣性指數
    return female_diversity

def both_diversity(): # 計算新生兒姓名多樣性
    """calculate the Shannon index of babies in each year, and output a list"""
    total_both_count_list = both_count()
    both_diversity = [] # 新增一個list裝每一年的新生兒姓名多樣性指數
    for i in file_list:
        fin = open(i)
        fobj = fin.readlines()
        shannon_index = 0
        
        for line in fobj:
            string = line.split(',') # 用split切出list裡面的資料轉成str
            factor = int(string[-1])/total_both_count_list[file_list.index(i)] # 每一年新生兒姓名佔該年度新生兒總數的比例
            shannon_index += (-1)*factor*math.log(factor) # 根據公式計算shannon_index
        both_diversity.append(shannon_index) # 加入新生兒姓名多樣性指數
    return both_diversity

# 作圖(x軸-年份,y軸-Shannon index)
x = range(1880,2021,1)
y1 = male_diversity()
y2 = female_diversity()
y3 = both_diversity()
# 圖表資訊
plt.plot(x,y1,label = 'male')
plt.plot(x,y2,label = 'female')
plt.plot(x,y3,label = 'both')
plt.legend()
plt.title('Shannon index of male/female/both')
plt.xlabel('years')
plt.ylabel('index')
# 匯出圖表
plt.show()
