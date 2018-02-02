#https://seleniumhq.github.io/selenium/docs/api/py/api.html

import AI2048ME
import math
import copy
TotalNum = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#TotalNumLog = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#print(TotalNum)
haha = AI2048ME.AI2048ME()

haha.Test();

def WhichOneIsRightToDo(TotalHAHA):
    TotalNumLog = copy.deepcopy(TotalHAHA)
    AIToDecide = AI2048ME.AI2048ME()
    ShowMe = Log2Handle(TotalNumLog)
    ResultFour = [0,0,0,0]
    ResultFourMove = [0, 0, 0, 0]
    ResultFour[0],ResultFourMove[0] = AI2048ME.UPHandle(TotalNumLog)
    ResultFour[1],ResultFourMove[1] = AI2048ME.DownHandle(TotalNumLog)
    ResultFour[2],ResultFourMove[2] = AI2048ME.RightHandle(TotalNumLog)
    ResultFour[3],ResultFourMove[3] = AI2048ME.LeftHandle(TotalNumLog)
    ResultDecide = [0, 0, 0, 0]
    for indexi in range(4):
        print("ResultFour" , indexi ,ResultFourMove[indexi] ,ResultFour[indexi])
    for indexi in range(4):
        if(ResultFourMove[indexi] != 0):
            ResultDecide[indexi] = AIToDecide.monoWeightCount(ResultFour[indexi])
        else:
            ResultDecide[indexi] = 0xFFFFFFF
        print("ResultDecide" , indexi , ResultDecide[indexi])

    return ResultDecide.index(min(ResultDecide))

def Log2Handle(TotalHAHA):
    TotalNumLog = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(4):
        pass
        for j in range(4):
            pass
            if(TotalHAHA[i][j] != 0):
                TotalNumLog[i][j] = int(math.log2(TotalHAHA[i][j]))

    return  TotalNumLog



def play2048():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import time
    # 打开firefox，并访问2048游戏界面
    bs = webdriver.Firefox()
    #bs.get('https://gabrielecirulli.github.io/2048/')
    bs.get('file:///D:/doc/webailiyun/htdocs/gameme/2048.htm')
    #file:///C:/Users/chenzhuo/Downloads/2048.htm
    #file:///D:/doc/webailiyun/htdocs/gameme/2048.htm
    html = bs.find_element_by_tag_name('html')
    while True:
        print('send up,right,down,left')
        #ShowData = bs.find_element_by_class_name('tile-container')

        for i in range(4):
            pass
            for j in range(4):
                pass
                strFindId = str(i) + "-" + str(j) + "-Grid"
                #print(strFindId)
                ShowData = bs.find_element_by_id(strFindId)
                ShowME = ShowData.get_attribute('innerHTML')
                #print("Showdata--", ShowME)
                TotalNum[i][j] = int(ShowME)

        print("TotalNum",TotalNum)
        '''
        Log2Over = AI2048ME.Log2Handle(TotalNum)
        print("Log2Over", Log2Over)

        monotemp = haha.monoWeightCount(Log2Over)

        print("monotemp",monotemp)
        '''
        #ShowData = bs.find_element_by_xpath("//div[@class='le-container']")
        #print("Showdata",str(ShowData.text))
        #print("Showdata--",ShowData.get_attribute('innerHTML'))

        ShowPPP= bs.find_element_by_id('TESTIDme').text

        #ShowData = bs.find_element_by_xpath("//div[@class='le-container']")
        print("ShowPPP__________________________________________",str(ShowPPP))
        AIdecideOut = WhichOneIsRightToDo(TotalNum)
        print("AIdecideOut",AIdecideOut)
        if AIdecideOut == 0:
            pass
            html.send_keys(Keys.UP)
            time.sleep(0.3)
        elif(AIdecideOut == 1):
            html.send_keys(Keys.DOWN)
            time.sleep(0.3)
            pass
        elif(AIdecideOut == 2):
            pass
            html.send_keys(Keys.RIGHT)
            time.sleep(0.3)
        elif(AIdecideOut == 3):
            pass
            html.send_keys(Keys.LEFT)
            time.sleep(0.3)
        '''
        html.send_keys(Keys.UP)
        time.sleep(0.3)
        time.sleep(3.3)
        html.send_keys(Keys.RIGHT)
        time.sleep(0.3)
        time.sleep(3.3)
        html.send_keys(Keys.DOWN)
        time.sleep(0.3)
        time.sleep(3.3)
        html.send_keys(Keys.LEFT)
        time.sleep(0.3)
    '''
        time.sleep(1.3)

        # 每四个方向操作后判断游戏是否结束
        game_over = bs.find_element_by_css_selector('.game-message>p')

        #print("game_over", game_over.text)
        if game_over.text == 'Game over!':
            score = bs.find_element_by_class_name('score-container')  # 当前得分
            print('game over, score is %s' % score.text)
            print('wait 3 seconds, try again')
            time.sleep(3)
            # 游戏结束后，等待3秒，自动点击try again重新开始
            try_again = bs.find_element_by_class_name('retry-button')
            try_again.click()
play2048();