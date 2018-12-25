"""wcount.py: count words from an Internet file.

__author__ = "Yicongwei"
__pkuid__  = "1800011850"
__email__  = "yicw@pku.edu.cn"
"""

import sys
import collections 
from urllib.request import urlopen
import urllib.error

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines = lines.lower()
    for i in lines:
        if not i.isalpha():#判断到非单词部分改成空格
            lines=lines.replace(i,' ')
    vocabulary = lines.split()
    ct = collections.Counter(vocabulary)#利用counter得到计数dict
    for (a,b) in ct.most_common(topn):#利用most_common得到按key的排序
        print(a,'\t',b)
    
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    #anayze whether paras are right or not
    elif len(sys.argv) >= 2:
        try:
            book = urlopen(sys.argv[1])#利用urlopen得到url
            ibook = book.read()
            book.close()
        except ValueError:#各种报错类型
            print('ValueError:unknown url type. please check your website,we got invaild url from it.')
        except urllib.error.URLError :
            print('urllib.error.URLError:Errno 11001. Please check your website or your Internet connection')
        except urllib.error.HTTPError :
            print('urllib.error.URLError:HTTP Error 404: Not Found. Please check your website.')
        else:
            bookstr = ibook.decode()
            if len(sys.argv) >= 3:#寻找topn值
                try:
                    topn = int(sys.argv[2])
                except ValueError:
                    print('please insure the number that you input is vaild.')
                else:
                    topn = int(sys.argv[2])
                    wcount(bookstr,topn)
            else:
                wcount(bookstr)
