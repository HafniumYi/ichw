"""wcount.py: count words from an Internet file.

__author__ = "Yicongwei"
__pkuid__  = "1800011850"
__email__  = "yicw@pku.edu.cn"
"""

import sys
import collections 
from urllib.request import urlopen

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    lines=lines.lower()
    for i in lines:
        if not i.isalpha():#处理非单词部分（包括将I'm一类抽得到I）
            lines=lines.replace(i,' ')
    vocabulary=lines.split()
    ct = collections.Counter(vocabulary)
    for (a,b) in ct.most_common(topn):
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
        try:#将txt网页的url读作字符串。
            book = urlopen(sys.argv[1])
            ibook = book.read()
            book.close()
        except ValueError:# 各类报错
            print('unknown url type. please check your website,we got invaild url from it.')
        except urllib.error.URLError:
            print('Errno 11001. Please check your website or your Internet connection')
        except urllib.error.HTTPError:
            print('HTTP Error 404: Not Found. Please check your website.')
        else:
            bookstr=ibook.decode()
            if len(sys.argv) >= 3:
                try:
                    topn=int(sys.argv[2])
                except ValueError:
                    print('please insure the number that you input is vaild.')
                else:
                    topn=int(sys.argv[2])
                    wcount(bookstr,topn)
                
            else:
                wcount(bookstr)
            
