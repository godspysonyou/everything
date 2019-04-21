from abc import ABCMeta, abstractmethod

# 使用abc模块来实现借口

class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass

class Wechatpay(Payment):
    def fuqian(self, money):
        print('微信支付了%s元'%money)

p = Wechatpay()