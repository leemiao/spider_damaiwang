import requests


class Spider(object):
    # 构造请求头等
    def __init__(self):
        self.url = "https://search.damai.cn/searchajax.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
            "cookie": "_uab_collina=153898386691021526720657; _umdata=70CF403AFFD707DFEB6BA57C56CA3B13E7BD5DAF561D420C384FF4DA75A62F56B2225CEC1DD4846FCD43AD3E795C914C46F57A339EDEC74F7006D0CE8CD77F14; x5sec=7b226d65632d67756964652d7765623b32223a226639303431366238343735643836656338393965393365656533303433646662434f3669374e3046454b2f666a7476302f7244356a41453d227d; cna=b0mIEx9fXWcCAQ6CznyYZjAe; cookie2=18204ab51d2bd14a7326dab901c58057; t=37103c62b8274bb5769837840f8b71a8; _tb_token_=36ed1e7aee13e; x_hm_tuid=PN4CfOch3fJ1yW4MpI+z3hZhs9u9ODTzpfGE7AtbNvax7kg+GG7r3wFIj/ihN/iG; _hvn_login=18; csg=6be6a003; munb=4199098224; damai.cn_nickName=MeisterLee; damai.cn_user=gz4HkAnuV3BDKOniG3I4tVZ2WybxgALVJu0CZ2Xkbi57+SBwd++X2SrBbVRAeGWUGxb2+Rjuqig=; damai.cn_user_new=gz4HkAnuV3BDKOniG3I4tVZ2WybxgALVJu0CZ2Xkbi57%2BSBwd%2B%2BX2SrBbVRAeGWUGxb2%2BRjuqig%3D; h5token=9ccd095300bc4588a090b771e8418b2b_1_1; damai_cn_user=gz4HkAnuV3BDKOniG3I4tVZ2WybxgALVJu0CZ2Xkbi57%2BSBwd%2B%2BX2SrBbVRAeGWUGxb2%2BRjuqig%3D; loginkey=9ccd095300bc4588a090b771e8418b2b_1_1; user_id=116768239; isg=BNfX8KBwQJVhx8QVBH4OF8nuZksr4qxma9qAKCkEQKYNWPSaMO1Azkg-vr5isIP2",
            "referer": "https://search.damai.cn/search.htm?ctl=%20%20%20&order=1&cty="
        }
        self.data = {
            "cty": "北京",
            "ctl": "演唱会",
            "tsg": "0",
            "order": "1"
        }
        # 构造IP代理(按需求开启)
        # proxies = {
        #     "http": "http://47.93.56.0:3128",
        #     "http": "http://39.135.24.12:80",
        # }

    # 请求url获取响应
    def get(self):
        response = requests.post(url=self.url, headers=self.headers, data=self.data)
        # 测试
        print(response.text)

    # # 解析数据
    # def parse(self):
    #     # 构造字典
    #     data_dict = {}
    #     pass
    #
    # # 保存数据
    # def save(self):
    #     pass
    #
    # def run(self):
    #     # 1.请求url获取响应
    #     self.get()
    #     # 2.解析数据
    #     self.parse()
    #     # 3.保存数据
    #     self.save()


if __name__ == '__main__':
    spider = Spider()
    spider.get()

