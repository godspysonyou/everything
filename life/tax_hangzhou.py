'''
杭州个人所得税
'''

yanglao_rate = 0.08
company_yanglao_rate = 0.14
yilao_rate = 0.02  # 忽略+3大病统筹
company_yilao_rate = 0.105
shiye_rate = 0.005
company_shiye_rate = 0.005
shebao_rate = yanglao_rate + yilao_rate + shiye_rate
company_shebao_rate = company_yanglao_rate + company_yilao_rate + company_shiye_rate

shebao_basic = (3054.95, 15274.74)  # 社保缴纳范围
gongjijin_basic = (2010, 24311)  # 公积金缴纳范围

tax_dict = {(0, 3000): [0.03, 0],  # 小于3000
            (3000, 12000): [0.10, 210],  # 大于3000小于12000
            (12000, 25000): [0.20, 1410],  # 大于12000小于25000
            (25000, 35000): [0.25, 2600],  # 大于25000小于35000的部分
            (35000, 55000): [0.30, 4410],  # 大于35000小于55000
            (55000, 80000): [0.35, 7160],  # 大于55000小于80000
            (80000, 10000000): [0.45, 15160]}  # 大于80000的部分

qizhengdian = 5000

gongjijin_rate = 0.12

def cal_company_shebao(gongzi):
    pass


def cal_shebao(gongzi):
    low = shebao_basic[0]
    high = shebao_basic[1]
    if gongzi >= low and gongzi < high:
        return gongzi * float(shebao_rate)
    elif gongzi >= 0 and gongzi < low:
        return low * float(shebao_rate)
    elif gongzi >= high:
        return high * float(shebao_rate)
    else:
        raise Exception('数值不在范围内')


def cal_gongjijin(gongzi):
    low = gongjijin_basic[0]
    high = gongjijin_basic[1]
    if gongzi >= low and gongzi < high:
        return gongzi * float(gongjijin_rate)
    elif gongzi >= 0 and gongzi < low:
        return low * float(gongjijin_rate)
    elif gongzi >= high:
        return high * float(gongjijin_rate)
    else:
        raise Exception('数值不在范围内')


def cal_tax_basic(gongzi):
    if gongzi>=qizhengdian:
        return gongzi - qizhengdian - cal_gongjijin(gongzi) - cal_shebao(gongzi)
    else:
        return 0


def cal_tax(tax_basic):
    for key, value in tax_dict.items():
        low = key[0]
        high = key[1]
        if tax_basic >= low and tax_basic < high:
            tax_rate = value[0]
            tax_quick = value[1]
            return tax_basic * tax_rate - tax_quick
    return -1


class Tax:
    def __init__(self, gongzi):
        if isinstance(gongzi, (float, int)):
            self.gongzi = gongzi
        else:
            raise Exception('不是数值类型')

        if gongzi<=1800:
            raise Exception('工资小于国家基本工资')

    def cal_shebao(self):
        return cal_shebao(self.gongzi)

    def cal_gongjijin(self):
        return cal_gongjijin(self.gongzi)

    def cal_tax(self):
        tax_basic = cal_tax_basic(self.gongzi)
        tax = cal_tax(tax_basic)
        if tax != -1:
            return tax
        else:
            raise Exception('数值不在范围内')

    def cal_shijigongzi(self):
        tax = self.cal_tax()
        shebao = self.cal_shebao()
        gongjijin = self.cal_gongjijin()
        return self.gongzi - tax - shebao - gongjijin


if __name__ == '__main__':
    t = Tax(9920)
    shijigongzi = t.cal_shijigongzi()
    print(shijigongzi)
