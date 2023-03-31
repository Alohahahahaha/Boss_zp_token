# -*- encoding: utf-8 -*-
"""
@Author: Aloha
@Time: 2023/3/19 23:22
@ProjectName: Practice
@FileName: video.py
@Software: PyCharm
"""
import threading
import os, xlwt, xlrd
from xlutils.copy import copy
import time
import requests


class BiLiBiLiVideo(object):
    def __init__(self):
        self.headers = {
            'authority': 'api.bilibili.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7',
            'cookie': 'LIVE_BUVID=AUTO1516404285352815; buvid4=044E554A-19AF-EEF8-CBA5-FBCF5191718E25566-022040715-Lefi4Vcg048bj6SyfCRJMg%3D%3D; buvid_fp_plain=undefined; blackside_state=0; CURRENT_BLACKGAP=0; i-wanna-go-back=-1; nostalgia_conf=-1; DedeUserID=455183647; DedeUserID__ckMd5=4cdccb7211472cb7; b_ut=5; hit-dyn-v2=1; is-2022-channel=1; b_nut=100; CURRENT_QUALITY=80; rpdid=|(k||l~luuRk0J\'uYYm|k~mlm; buvid3=2E2FEDB4-4A0E-3453-67EC-74C1E843C0AD45873infoc; _uuid=966810BC10-641010-CB1010-8B9A-FAA5B1F433C547093infoc; header_theme_version=CLOSE; fingerprint=126bb84f1f4222ff23b886317d43e771; SESSDATA=4b62b174%2C1693745734%2Ca7623%2A31; bili_jct=7489ec7f04b617376b4b6c053ea9de3b; sid=6uh838n0; bp_video_offset_455183647=770130749262135300; PVID=1; buvid_fp=126bb84f1f4222ff23b886317d43e771; home_feed_column=5; CURRENT_FNVAL=4048; b_lsid=DFD53222_186C0C23CA8; bsource=search_baidu; innersign=1',
            'origin': 'https://www.bilibili.com',
            'referer': 'https://www.bilibili.com/video/BV1j24y1a7FK/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=15eb2628ca2ad486c0f6b3cb81be2738',
            'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
        }

    def videoInfo(self, aid):
        try:
            url = f"https://api.bilibili.com/x/web-interface/view?aid={aid}"
            response = requests.get(url, headers=self.headers).json()
            res = response['data']
            nickname = res['owner']['name']  # 视频作者
            uid = res['owner']['mid']  # 作者id
            address = 'https://api.bilibili.com/x/space/wbi/acc/info?mid=' + str(uid)  # 作者主页地址
            face = res['owner']['face']  # 作者头像
            bvid = res['bvid']
            aid = res['aid']  # 视频id
            """ 格式化时间戳 """
            c = res['pubdate']  # 发布时间
            n = time.localtime(c)  # 将时间戳转换成时间元祖tuple
            pubdate = time.strftime("%Y-%m-%d %H:%M:%S", n)  # 格式化输出时间
            title = res['title']  # 视频标题
            """ 视频数据 """
            coins = res['stat']['coin']  # 获得硬币数
            favorite = res['stat']['favorite']  # 视频收藏数
            danmaku = res['stat']['danmaku']  # 视频弹幕数
            like = res['stat']['like']  # 视频点赞数
            reply = res['stat']['reply']  # 视频评论数
            share = res['stat']['share']  # 视频分享数
            view = res['stat']['view']  # 视频播放量
            data = {
                '视频数据': [nickname, address, face, bvid, aid, pubdate, title, url, coins, favorite, danmaku, like, reply,
                         share, view]
            }
            # self.SaveExcels(data)
            print(f'视频 {title} 采集完毕----------------------')
        except Exception as e:
            print(f'-------------------------视频id {aid} 不存在---------------------------')

    def run(self):
        start = time.time()
        thread = []
        aid = 1
        while True:
            t = threading.Thread(target=self.videoInfo, args=(aid,))
            t.start()
            thread.append(t)
            for i in thread:
                i.join()
            aid += 1
            if aid == 90:
                end = time.time()
                print('所需时间', end - start)  # 14.637601852416992  线程
                break


if __name__ == '__main__':
    b = BiLiBiLiVideo()
    b.run()