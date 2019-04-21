class Alipay:
    '''
    支付宝支付
    '''
    def pay(self,money):
        print('支付宝支付了%s元'%money)

class Applepay:
    '''
    apple pay支付
    '''
    def pay(self,money):
        print('apple pay支付了%s元'%money)



# class Wechatpay:
#     def fuqian(self, money):
#         print('微信支付了%s元'%money)
def pay(payment,money):
    '''
    支付函数，总体负责支付
    对应支付的对象和要支付的金额
    '''
    payment.pay(money)

class Payment:
    def pay(self, money):
        raise NotImplementedError


class Wechatpay(Payment):
    def fuqian(self, money):
        print('微信支付了%s元'%money)


p = Wechatpay()
pay(p,200)