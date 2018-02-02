#https://seleniumhq.github.io/selenium/docs/api/py/api.html



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
        ShowData = bs.find_element_by_id('0-0-Grid')

        #ShowData = bs.find_element_by_xpath("//div[@class='le-container']")
        print("Showdata",ShowData)
        html.send_keys(Keys.UP)
        time.sleep(0.3)
        html.send_keys(Keys.RIGHT)
        time.sleep(0.3)
        html.send_keys(Keys.DOWN)
        time.sleep(0.3)
        html.send_keys(Keys.LEFT)
        time.sleep(0.3)
        time.sleep(3.3)

        # 每四个方向操作后判断游戏是否结束
        game_over = bs.find_element_by_css_selector('.game-message>p')
        if game_over.text == 'Game over!':
            score = bs.find_element_by_class_name('score-container')  # 当前得分
            print('game over, score is %s' % score.text)
            print('wait 3 seconds, try again')
            time.sleep(3)
            # 游戏结束后，等待3秒，自动点击try again重新开始
            try_again = bs.find_element_by_class_name('retry-button')
            try_again.click()
play2048();