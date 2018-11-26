"""currency.py: To tell you how much your money is worth in another currency .
__author__ = "Yicongwei"
__pkuid__  = "1800011850"
__email__  = "yicw@pku.edu.cn"
"""
# exchange functions

from urllib.request import urlopen

def before_space(s):
    '''处理字符串，返回得到第一个空格以前的子串'''
    i=s.partition(' ')
    result=i[0]
    return result

def get_to(json):
    '''处理访问URL转化得到的字符串，返回得到to的货币值'''
    a=json.index('to')
    b=json.index(':',a+1)
    start=json.index('"',b+1)
    end=json.index('"',start+1)
    return json[start+1:end]
    
def has_error(json):
    '''处理访问URL的得到的信息，检查货币查询是否有效'''
    if 'false' not in json:
        return ('false'  in json)
    else:
        return ('false'  in json)
    
def currency_response(currency_from,currency_to,amount_from):
    '''根据所提供的原货币符号及金额，目标货币符号（三字母代码），得到对应的json字符串'''
    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+str(currency_from)+'&to='+str(currency_to)+'&amt='+str(amount_from))
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr

def iscurrency(currency):
    '''分析所提供货币符号是否有效'''
    jstr=currency_response(currency,'CNY',227)
    return has_error(jstr)==False

def exchange(currency_from,currency_to,amount_from):
    '''根据所提供的原货币符号及金额，目标货币符号（三字母代码），返回目标货币金额'''
    if iscurrency(currency_from)==False or iscurrency(currency_to)==False:
        return 'incalculable, please check the currency code you input.'
    else: 
        a=currency_response(currency_from,currency_to,amount_from)
        b=get_to(a)
        answer=float(before_space(b))
        return answer

# test functions   
def test_A():
    '''测试用来切割字符串的函数before_space'''
    assert('0.8963'==before_space('0.8963 Euro'))
    
    
def test_B():
    '''测试用来处理json字符串的函数get_from，get_to和has_error'''
    assert('2.1589225 Euros'==get_to('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'))
    assert(False==has_error('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'))
    
def test_C():
    '''测试用来得到json字符串（货币查询）的函数currency_response'''
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'==currency_response('USD','EUR',2.5))

def test_D():
    '''测试判断货币有效性及货币兑换的函数iscurrency和exchange'''
    assert(True==iscurrency('CNY'))
    assert(2.1589225==exchange('USD','EUR',2.5))
    
def test_All():
    '''打包测试'''
    """test all cases"""
    test_A()
    test_B()
    test_C()
    test_D()
    print("All tests passed")

def main():
    test_All()

    # 获得访问关键字
    print("If you don't know the code of the currency, you can visit this website in your own browser——https://www.xe.com/iso4217.php")
    currency_from=str(input('the currency code that you now have:'))
    currency_to=str(input('the currency code that you want to get:'))
    amount_from=float(input('the amount of the currency that you want to exchange:'))
    # 输出结果
    print('The amount of the targeted currency is '+str(exchange(currency_from,currency_to,amount_from)))    
    
if __name__ == '__main__':
    main()
