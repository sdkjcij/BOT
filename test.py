from http import server
from re import T
from tkinter import N
import discord
from discord.ext import commands
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

opts = Options()
#opts.add_argument('--headless') # 啟動無頭模式
#opts.add_argument('--disable-gpu') # windowsd必須加入此行

lanes = ["上路TOP","中路AP","打野JG","輔助SUP","下路ADC"]
lanes_play = ["上路","中路","打野","輔助","下路"]
stars = [":star:",":star::star:",":star::star::star:",":star::star::star::star:",":star::star::star::star::star:"]
hearts = [":heart_on_fire:",":heart_on_fire::heart_on_fire:",":heart_on_fire::heart_on_fire::heart_on_fire:",":heart_on_fire::heart_on_fire::heart_on_fire::heart_on_fire:",":heart_on_fire::heart_on_fire::heart_on_fire::heart_on_fire::heart_on_fire:"]
names = ["呂諺","大腸腸","阿熙","韋頡","小智","桀煾"]

TOP = ["厄薩斯","卡蜜兒","古拉格斯","弗力貝爾","伊瑞莉雅","伊羅旖","汎","克雷德","吶兒","犽宿","犽凝","辛吉德","杰西","阿卡莉","科加斯","約瑞科","剛普朗克","悟空","泰達米爾","烏爾加特","納瑟斯","貪啃奇","凱能","凱爾","提摩","斯溫","菲歐拉","鄂爾","慎","葛雷夫","葵恩","賈克斯","達瑞斯","雷尼克頓","雷玟","漢默丁格","蒙多醫生","蓋倫","歐拉夫","墨菲特","賽恩","賽特","藍寶","關","魔鬥凱薩"]
AP = ["加里歐","卡特蓮娜","卡莎碧雅","卡薩丁","弗拉迪米爾","伊瑞莉雅","安妮","艾克","艾妮維亞","劫","犽宿","犽凝","妮可","拉克絲","阿卡莉","阿祈爾","阿璃","星朵拉","柔伊","飛斯","埃可尚","姬亞娜","庫奇","逆命","馬爾札哈","勒布朗","斯溫","塔莉雅","塔隆","奧莉安娜","雷茲","漢默丁格","維克特","維迦","齊勒斯","翱銳龍獸","薇可絲","賽勒斯","麗珊卓"]
JG = ["卡力斯","卡爾瑟斯","史加納","史瓦妮","弗力貝爾","札克","伊芙琳","伊莉絲","艾克","努努和威朗普","劫","希瓦娜","李星","沃維克","貝爾薇斯","夜曲","奈德麗","拉姆斯","易大師","波比","阿姆姆","埃爾文","悟空","烏迪爾","特朗德","莉莉亞","慨影","菲艾","費德提克","塔莉雅","塔隆","葛雷夫","雷珂煞","雷葛爾","嘉文四世","維爾戈","赫克林","趙信","歐拉夫","黛安娜","薩科","鏡爪"]
AD = ["伊澤瑞爾","吉茵珂絲","好運姐","汎","艾希","克黎思妲","希格斯","希維爾","犽宿","亞菲利歐","法洛士","剎雅","婕莉","寇格魔","崔絲塔娜","凱特琳","凱莎","煞蜜拉","路西恩","達瑞文","圖奇","燼"]
SUP = ["巴德","卡瑪","布里茨","布朗姆","布蘭德","艾希","亞歷斯塔","珊娜","拉克斯","威寇茲","枷蘿","派克","珍娜","茂凱","娜米","納帝魯斯","索拉卡","索娜","悠咪","斯溫","塔里克","極靈","瑟菈紛","瑟雷西","雷歐娜","睿娜妲．格萊斯克","齊勒斯","潘森","銳兒","銳空","露璐","魔甘娜"]
Hero = ["厄薩斯","卡蜜兒","古拉格斯","弗力貝爾","伊瑞莉雅","伊羅旖","汎","克雷德","吶兒","犽宿","犽凝","辛吉德","杰西","阿卡莉","科加斯","約瑞科","剛普朗克","悟空","泰達米爾","烏爾加特","納瑟斯","貪啃奇","凱能","凱爾","提摩","斯溫","菲歐拉","鄂爾","慎","葛雷夫","葵恩","賈克斯","達瑞斯","雷尼克頓","雷玟","漢默丁格","蒙多醫生","蓋倫","歐拉夫","墨菲特","賽恩","賽特","藍寶","關","魔鬥凱薩","加里歐","卡特蓮娜","卡莎碧雅","卡薩丁","弗拉迪米爾","安妮","艾克","艾妮維亞","劫","妮可","拉克絲","阿祈爾","阿璃","星朵拉","柔伊","飛斯","剛普郎克","埃可尚","姬亞娜","庫奇","逆命","馬爾札哈","勒布朗","塔莉雅","塔隆","奧莉安娜","雷茲","維克特","維迦","齊勒斯","翱銳龍獸","薇可絲","賽勒斯","麗珊卓","卡力斯","卡爾瑟斯","史加納","史瓦妮","札克","伊芙琳","伊莉絲","艾克","努努和威朗普","劫","希瓦娜","李星","沃維克","貝爾薇斯","夜曲","奈德麗","拉姆斯","易大師","波比","阿姆姆","埃爾文","烏迪爾","特朗德","莉莉亞","慨影","菲艾","費德提克","塔莉雅","塔隆","雷珂煞","雷葛爾","嘉文四世","維爾戈","赫克林","趙信","黛安娜","薩科","鏡爪","伊澤瑞爾","吉茵珂絲","好運姐","艾希","克黎思妲","希格斯","希維爾","亞菲利歐","法洛士","剎雅","婕莉","寇格魔","崔絲塔娜","凱特琳","凱莎","煞蜜拉","路西恩","達瑞文","圖奇","燼","巴德","卡瑪","布里茨","布朗姆","布蘭德","艾希","亞歷斯塔","珊娜","拉克斯","威寇茲","枷蘿","派克","珍娜","茂凱","娜米","納帝魯斯","索拉卡","索娜","悠咪","塔里克","極靈","瑟菈紛","瑟雷西","雷歐娜","睿娜妲•格萊斯克","齊勒斯","潘森","銳兒","銳空","露璐","魔甘娜"]


Path = "C:/Users/user/Desktop/chromedriver.exe"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!')

@bot.event

async def on_ready():
    print(">> 熙掰Bot is Online <<")

    channel_siba = bot.get_channel(971373450281226280)
    await channel_siba.send(">> 熙掰Bot is Online <<")
    
    game = discord.Game('熙掰聯盟')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.idle, activity=game)

@bot.command()
async def ping(ctx):
    await ctx.reply(f'延遲為{round(bot.latency*1000)} 毫秒')

@bot.event

async def on_message(message):
    channel_siba = bot.get_channel(971373450281226280)
    if message.content == '玩哪路':
        random.shuffle(lanes)
        await message.reply("為你選擇" + lanes[0])

    if message.content == '手感':
        random.shuffle(hearts)
        await message.reply(hearts[0])
    
    if message.content == '運氣':
        random.shuffle(stars)
        await message.reply(stars[0])

    if message.content == '3v3隨機分隊':
        random.shuffle(names)
        team1 = "第一組:"+names[0]+" "+names[1]+" "+names[2]
        team2 = "第二組:"+names[3]+" "+names[4]+" "+names[5]
        await message.reply(team1+"\n"+team2)
    
    if message.content == '上路':
        random.shuffle(TOP)
        Text_top = "為你選擇" + TOP[0]
        await message.reply(Text_top)
    
    if message.content == '中路':
        random.shuffle(AP)
        Text_AP = "為你選擇" + AP[0]
        await message.reply(Text_AP)

    if message.content == '下路':
        random.shuffle(AD)
        Text_AD = "為你選擇" + AD[0]
        await message.reply(Text_AD)

    if message.content == '打野':
        random.shuffle(JG)
        Text_JG = "為你選擇" + JG[0]
        await message.reply(Text_JG)

    if message.content == '輔助':
        random.shuffle(SUP)
        Text_SUP = "為你選擇" + SUP[0]
        await message.reply(Text_SUP)

    if message.content == "指令":    
        await message.reply(">> 熙掰Bot指令 <<\n1.玩哪路\n2.手感\n3.運氣\n4.3v3隨機分隊\n5.上路\n6.中路\n7.下路\n8.打野\n9.輔助\n10.搜索符文裝備 打(!+空格+英雄名字)\n11.隨機\n12.多選一選擇器 打(選 物品1 物品2.... or 選擇 英雄1 英雄2....)")

    if message.content == "隨機":
        random.shuffle(Hero)
        random.shuffle(lanes_play)
        Text_play = lanes_play[0]+Hero[0]
        await message.reply(Text_play)

    if message.content.startswith('!'):
        Hero_content =[]
        Hero_content = message.content.split()
        message_content = Hero_content[1]
        if message_content in Hero:

            driver = webdriver.Chrome(Path,chrome_options=opts)
            driver.get("https://www.op.gg/")

            element_search = driver.find_element(By.ID, 'searchSummoner')
            element_search.send_keys(message_content)
            WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH , '/html/body/div[1]/div[2]/div[2]/div/nav/a/div/small/em[1]'))
            )

            element_send = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/nav/a/div/small/em[1]')
            ActionChains(driver).move_to_element(element_send).perform()
            ActionChains(driver).click(element_send).perform()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , '/html/body/div[1]/div[5]/div/main/div[1]/h4/a'))
            )

            currentPageUrl = driver.current_url
            driver.execute_script('window.scrollBy(0,500)')
            time.sleep(1)
            driver.get_screenshot_as_file("D:/Python Project/VScode/image.png")
            driver.close()

            file = discord.File("D:/Python Project/VScode/image.png", filename="image.png")
            embed_hero = discord.Embed(
                title = "符文及裝備",
                description = message_content,
                color = 0x3498db
            )
            embed_hero.add_field(name="網址", value=currentPageUrl)
            embed_hero.set_image(url = "attachment://image.png")

            await message.reply(file=file, embed=embed_hero)

    if message.content.startswith("選"):
        split_hero_choose = []
        text = message.content
        split_hero_choose = text.split()
        del split_hero_choose[0]
        
        #print(split_hero_choose)
        random.shuffle(split_hero_choose)
        #await channel_luyan.send(split_hero_choose[0])

        if split_hero_choose[0] in Hero:
            await channel_siba.send("------------------------------------------符文及裝備搜尋中//請稍後------------------------------------------")

            driver = webdriver.Chrome(Path,chrome_options=opts)
            driver.get("https://www.op.gg/")

            element_search = driver.find_element(By.ID, 'searchSummoner')
            element_search.send_keys(split_hero_choose[0])
            WebDriverWait(driver, 1).until(
                EC.presence_of_element_located((By.XPATH , '/html/body/div[1]/div[2]/div[2]/div/nav/a/div/small/em[1]'))
            )

            element_send = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div/nav/a/div/small/em[1]')
            ActionChains(driver).move_to_element(element_send).perform()
            ActionChains(driver).click(element_send).perform()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH , '/html/body/div[1]/div[5]/div/main/div[1]/h4/a'))
            )

            currentPageUrl = driver.current_url
            driver.execute_script('window.scrollBy(0,500)')
            time.sleep(1)
            driver.get_screenshot_as_file("D:/Python Project/VScode/image.png")
            driver.close()
            
            await channel_siba.send("---------------------------------------------搜尋完成//請等候傳輸--------------------------------------------")

            file = discord.File("D:/Python Project/VScode/image.png", filename="image.png")
            
            embed_hero = discord.Embed(
                title = text,
                description = "為你選擇" + split_hero_choose[0],
                color = 0x3498db
            )
            embed_hero.add_field(name="網址", value=currentPageUrl)
            #pic = discord.File("C:/VScode/Python Project/符文及裝備.png")
            embed_hero.set_image(url = "attachment://image.png")
            
            await message.reply(file=file, embed=embed_hero)
        
        else:
            split_message = []
            text = message.content
            split_message = text.split()
            del split_message[0]
            #print(split_hero_choose)
            random.shuffle(split_message)
            embed_hero = discord.Embed(
                title = text,
                description = "為你選擇" + split_message[0],
                color = 0x3498db
            )
            await message.reply(embed=embed_hero)

bot.run('OTg0OTk2MTAwNzYxMDY3NTcw.G9lmNQ.7m2ein9QzYpXroS_ZF7smJqKK0U4N2hlkQItig')



#OTkyNzU3OTA4MjY3ODY0MDk1.G56B1O.Ji3ztGHC0pxSqLK29RFZCDa0oVI9jJNbmtf1FI