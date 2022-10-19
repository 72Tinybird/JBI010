



# Programming

* 可迭代对象： string、list、dict、tuple、set() 
* immutable:string、tuple(generator)、int、float、bool……
* mutable:list、dict、set

## string  (immutable)  " "

* 比大小就是字母排列顺序，所以大写都在小写前
* str.upper() ->小写变大写
* str.find()  ->查位置  find('b', 1, 2)  [1, 2)中查
* for element in string:
* string[0:4]  ->取前四位
* str.replace(a,b)  ->a换成b
* str,list,tuple可互转
* string.punctuation

### Tips

* str.capitalize()  ->首字母大写

* str.repalce('python','world')  ->交换str中python变成world

  str.replace('a','e',2)  ->换2次 ex：ababaa->ebebaa

* str.split(x,y)  ->切割符和切割次数

​           ![img](https://images2015.cnblogs.com/blog/979582/201612/979582-20161216172809839-811954751.png) 

## list  (mutable) [ ]

### Reduce, Map, Filter

* 多个列表值整合成一个
* 映射，将一个函数作用到列表中每一个元素
* 筛选

###  Tips

* str.isdigit() ->bool  判断是否只由数字组成

* for b in bikes:  #  遍历列表  new_bike = []

     ​      \#  new_bike.append(b.capitalize())  小写变大写

     ​      print(b)

* 'Sparata' in bikes ->bool

*   \*   +

* word = open('word.txt')

     

* **str=' '.join(list)  ->list转str**

* **list=claim.split()  ->str转list,内部数字还是str的形式**

* **list=list(s)  ->强转string->list**

     

* print("%.1f"%a)  ->保留一位小数

* format(x, "0.1f")

* round(x, 1)

* line.rstrip()  ->删空格(末尾)  strip(头尾)

     

* **list.append()  ->列表加元素**  

* **list1.extend(list2)  ->列表加列表**

* **list.pop(1)  ->列表删元素**

* **list.remove("daskjdas")  ->删除特定元素**

* **del list[x:y]**

     

* list.sort()  ->列表排序(必须同类型)

* try: # 判定是否为浮点数
              float(num)

  ​            return True

  ​        except ValueError:
  ​            pass

* isinstance(element,float)  ->判断是否为某一个类型

### Examples

* **a = [1, 2, 3]**

     **b = [1, 2, 3]**

     **a is b ->False (具有相同的值但不是同一个对象)**

```python
lst1 : list = [1, 2]
lst2 : list = lst1.append(3) # append语句返回值为None
# 返回None的还有sort,remove
print(lst1)
print(lst2)->None
```

## tuple  (immutable) a sequence of values ( )

* 整数索引，和list差不多

* t[len(t)-1]

* t[2:4]

* t = ('Data',) + t[1:]  ->immutable不能换中间的值，只能创建新的

* t1 : tuple = 'programming' ,  ->只有一个元素的tuple要以,为终止符

* **<u>无敌的enumerate</u>** enumerate(x,y) 可迭代对象和从y开始

```python
for index, element in enumerate('abcdef'):
    print(index, element)
"""output
0 a
1 b
2 c
3 d
4 e
5 f
"""
```

### Tips

*  ***Python allows us to have a tuple on the left side of an assignment.  In this way, we can assign more than one variable at a time.*** 
*  t=d.items()  ->dict转List[Tuple] : ([('a', 0), ('b', 1), ('c', 2)])
*  dict_d=dict(lst)  ->a list of tuple(长度为2)转dict
*  **Generator形式就是通过tuple循环载入,可用tuple(generator)变tuple(enumerate好用)**

### Examples (zip)

```python
s = 'abc'
t = [0, 1, 2]

z = zip(s, t) # 打包多个序列
print(z)

for pair in zip(s, t): # 提取
    print(pair)
    
list(zip(s, t))  ->要是s和t长度不同,按短的x来组成列表中x个元组
```

```python
for word in words:
    length_words.append((len(word), word))
    
length_words.sort(reverse=True) # 元组排序先看第一项

sort_words : list = list()

for length, word in length_words: # 按从大到小排序
    sort_words.append(word)
```

```python
from typing import List

def has_perfect_match(t1 : List[any], t2 : List[any]) -> bool:
    """checks whether there is at least one matching element
    """
    
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

has_perfect_match(['Data', 'Science', 'Statistics'], ['Computer', 'Science', "Programming"])
```

* 通过zip整合两个list然后取值操作，不用zip会导致解压值太多报错

## dictionary  (mutable)  { }表字典,[ ]进行操作

* dict[x]=any_thing ->加元素

* Dict=dict( )或Dict={ }  ->空字典

* len(dict)  ->key-value对数量

* word=dict.values()

  'twee' in word  ->查value

* dict[val].append(key)  ->列表key项中添加

* a=sorted(a.items(), key=lambda x: x[1], reverse=True)  

* for key in a.keys():  ->遍历key

* for value in a.values():  ->遍历value

* sum(dict.values())  ->字典中value的所有数字相加

### Tips

*  Lists can be used as values in a dictionary. 
* key 一定是hash型的(immutable->list不行)
* raise LookupError('value does not appear in the dictionary') #报错
* global a  ->函数内声明对全局变量进行赋值等改变操作
* **用zip引入dict,因为dict只接受一个参数**
* dict的key值可以是元组

### Examples



```python
# 计算dict中各字母数量
from typing import Dict
def histogram(word : str) -> Dict:
    """Creates a dictionary for counting the number of letters in a word
    """
    
    dct : Dict = dict()
    for c in word: #不用if
        dct[c] = dct.get(c, 0) + 1
    return dct

letter_hist : Dict = histogram('computerscience')

print(letter_hist)
```

```python
# 计算dict中各字母数量(删特殊符号)
import string

try:
    fhand : str = open('datasets/romeo-full.txt')
except:
    print('File cannot be opened:')
    exit()
    
romeof_dict : Dict = dict()
for line in fhand:
    line = line.translate(line.maketrans('', '', string.punctuation))
    '''图表input->创建图表->被替换，替换，删除
    '''
    line = line.lower()
    words : list = line.split()
    for word in words:
        # romeof_dict[word]=romeof_dict.get(word,0)+1
        if word not in romeof_dict:
            romeof_dict[word] = 1
        else:
            romeof_dict[word] += 1
            
print(romeof_dict)
```

```python
# 反转字典
def invert_dict(dct: Dict) -> Dict:
    inv_dct : Dict = dict()
    for key in dct:
        val = dct[key]
        if val not in inv_dct:
            inv_dct[val] = [key]
        else:
            inv_dct[val].append(key)
    return inv_dct
```

## Set (mutable) 无序不重复元素集 { }

* fruits: set = {'apple', 'pear', 'papaya'}
* fruits.add()  ->set加元素
* set_1.union(set_2)  ->两个set并集   set_1 | set_2
* set_1.intersection(set_2)  ->两个set交集  set_1 & set_2
* set_1.difference(set_2)  ->set_1 - set_2
* len(set(lst)) < len(lst)  ->判断是否有重复元素

### Examples

```python
words1 : dict = {'because': 3, 'you': 5, 'are': 2, 'mine': 2, 'not': 3,
    'I': 2, 'look': 1, 'die': 1, 'love': 1}

words2 : dict = {'you': 5, 'look': 1, 'die': 1, 'looking': 2}

set(words1) - set(words2)

{'I', 'are', 'because', 'love', 'mine', 'not'}
```

```python
from typing import List, Dict

def split_text(text_arg : str) -> List[str]:
    """Splits a text into words which is returned as a list.变小写，删特殊符号
    The words are decapitalized (lower) and punctuation is stripped."""
    
    body : str = text_arg.read()
    
    stripped_words : list = []
    words : List[str] = body.split()
    for w in words:
        lower_w : str = w.lower()
        stripped_w : str = lower_w.strip(string.punctuation)
        stripped_words.append(stripped_w)
        
    return stripped_words

def histogram(words : List[str]) -> Dict:
    """transforms the list of words into dictionary
    list->dict
    """
    
    word_hist : dict = dict()
    for word in words:
        if word not in word_hist:
            word_hist[word] = 1
        else:
            word_hist[word] += 1
    return word_hist
 
text = open('text.txt') 

words = split_text(text)
print(len(words))

word_histo = histogram(words)
print(word_histo)
```

```python
def process_file(filename : str) -> Dict:
    """transforms the content of the given file into a dictionary of words 
    where the frequencies is counted
    """
    
    word_histo : dict = dict()
    fp  : TextIO = open(filename)
    
    for line in fp:
        process_line(line, word_histo)
        
    return word_histo

def process_line(line : str, histo : Dict) -> Dict:
    """add the words of a single line, after preprocessing, to the dictionary
    """
    
    line = line.replace('-', ' ')
    
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        histo[word] = histo.get(word, 0) + 1

hist = process_file('emma.txt')
print(hist)
```

```python
from typing import Tuple

def most_common(hist : Dict) -> List[Tuple]:
    """transforms the dictionary in a list and sorts the list on most values
    """
    frequencies = []
    
    for key, value in hist.items():
        frequencies.append((value, key))
        
    frequencies.sort(reverse=True)
    #frequencies.sort()
    #反向排序
    return frequencies

frequencies = most_common(hist)
print('The most common words are:')

for freq, word in frequencies[:10]:
    print(word, freq, sep='\t')
```

```python
import random # 随机数就对列表进行随机取

def random_word(hist : Dict) -> str:
    """chooses a random word from a dictionary
    """
    word_lst : List[str] = []
    
    for word, freq in hist.items():
        word_lst.extend([word] * freq) # the word is added to the list as often as the frequency
    
    print(len(word_lst))
    return random.choice(word_lst)

print(random_word(hist))
```



## File

* a=open('wenjianming.txt','w')  ->打开文件(w是“写入”模式），可用for循环全部读取

* a.close()  ->结束写入

* call : **str** = a.read()  ->读取所有文件，且**一次性**(a无法再次调用)

* line.startwith('letter')  ->bool

* line.rstrip()  ->print自带两倍间距，删末尾空格

* line.find('letter')  ->如果存在返回位置，不存在返回-1

* import os

  cwd:str=os.getcwd()  ->获取地址

* os.path.abspath()  ->绝对地址

* os.path.exists()  ->文件是否存在  # os.path.isdir  判断是否为文件夹

* os.walk()  ->遍历所有子目录

* file.write(str)  ->写入(别忘了\n)

  

* with open(path,'r') as f:  ->json module引入文件的方法,'r'只读,'w'写
  infos = json.load(f)
  
* next(f) ->跳过一行

## matplotlib.pylot

* %matplotlib inline  ->适用就无需plt.show()
* import matplotlib
* import matplotlib.pyplot as plt
* plt.figure()  ->初始化plt图表
* plt.title("Temperature Conversion")  ->图表名
* plt.ylabel("Celsius")  ->y轴名
* plt.xlabel("Fahrenheit")  ->x轴名
* plt.scatter(convert_valid,valid)  ->x,y轴值
* plt.show()  ->生成图表

## build-in functions

* min()

* max()

* abs()

* len()

* divmod(x,y)  ->x//y  x%y

* pow(x,y)  ->x^y

  pow(x,y,z)  ->(x^y)%z

* round(num, y(保留位数))  ->一个参数默认保留一位

* isinstance(x,y)  ->判断x是不是y的type

* cmp(x,y)  ->x=y返回0,x>y返回1,x<y返回-1

* range() and xrange()  ->type不一样,list和xrange

* filter(f,range(10))  ->返回使函数为True的结果集

​            ![img](https://images2015.cnblogs.com/blog/979582/201612/979582-20161216174215761-1607633930.png) 

* \* 加在参数前可表任何形式 *args：any

* zip(a,b,c) 

* map(None,a,b,c)  ->会以None补全缺值

  ex：>>> map(None,a,b)

  ​        [(1,4), (2,5),(3,6)]

  ​        \>\>\> map(add,a,b)  # zip不行

  ​        [5, 7, 9]
  
* map(function,iterable,...)

   \>>> map(square, [1,2,3,4,5])  # 计算列表各个元素的平方
  [1, 4, 9, 16, 25] 

*  a = datetime.date.today()   ->a=datetime.date(2017,3,22)

  year=a.year

## re module

* patten = re.compile(r'限制条件[A-Z] [a-z]2到4次{2,4}加.任意字符*')
* line=re.sub("[!@#$]","",line)  ->后换前
* a=patten.search("sadasdasd")
* a.group(a,b)
* re.match("www","www.runoob.com".span())  ->(0,3)

  





## class  (every class is an object)  mutable

* class Point:

  ​    """what is point"""

  pnt=Point()

  pnt.x, pnt.y = 3, 4

  def print_point(p: Point):

  ​    print('(%g, %g)' % **(p.x,p.y)**) ->%**要加括号**

  print_point(pnt)

```python
class Point:
    """Represents a point in 2-D space."""
    
    def __init__(self, x=0, y=0):
        """ creates a new Point object and initializes it
        """
        self.x : int = x
        self.y : int = y
            
class Rectangle:
    """Represents a rectangle.
    
    attributes: width, height, corner.
    """
 
    def __init__(self, w=0, h=0, x=0, y=0):
        """ creates a new Point object and initializes it
        """
        self.width : float = w
        self.height : float = h
        self.corner : Point(x,y)
            
box : Rectangle = Rectangle(100.0, 100.0, 0, 0)
box.width : float = 100.0
box.height : float = 200.0
box.corner : Point = Point() ->这步不能省
box.corner.x : float = 0.0
box.corner.y : float = 0.0
```

* copy

  p1 = Point()

  p1.x=1, p1.y=2

  p2 ：Point =  copy.copy(p1)

  p1 is p2 -> False

* 测试docstring

```python
doctest.testmod(verbose=True)  # with details
```

### classes and methods 

  *<u>a **method** is a function that is associated with a particular class</u>* 

* Time.print_time(start)  ->function syntax 
* start.print_time()  ->method syntax (common one)

```python
def print_event_time(time : Time, event="None"):
    print('{:02d}:{:02d}:{:02d} {}'.format(time.hour, time.minute, time.second, event))
          
print_event_time(start, event="Log in")
print_event_time(start)

21:45:00 Log in
21:45:00 None
```

*  In this case, `time` is a positional argument, while `event` is a keyword argument. 
* \__init__ method  -> 初始化
* \__str__ method  -> return的值即class的输出值(可print)
* \__add__ method -> 可以把object进行+操作(可print(a+b))
* \__radd__ method -> 右侧加法 return self.\_\_add__(other)
* isinstance(other, class) -> 是否为class类型返回True/False
* \__repr__ method ->类str,return



## Searching  

* counts = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]

  counts.index(max(counts)) ->3 最大值索引

```python
from typing import List, Tuple

def find_two_highest_remove(amounts : List[int]) -> Tuple[int, int]:
    # Find the index of the maximum in seals
    highest : int = max(amounts)
    high_index1 : int = amounts.index(highest)
    # Remove that item form the list
    amounts.remove(highest)
    
    # Find the index of the new maximum in the list
    next_highest : int = max(amounts)
    high_index2 : int = amounts.index(next_highest)
    
    # Put the highest item back in the list
    amounts.insert(high_index1, highest)
    
    # If necessary, adjust the second index
    if high_index1 <= high_index2:
        high_index2 += 1
        
    # Return the two indices
    return (high_index1, high_index2)

find_two_highest_remove([334, 468, 549, 836, 660, 389, 308, 392, 520, 271]) -> (3, 4)
```

* 1、Find,  Remove, Find

```python
from typing import List, Tuple

def find_two_highest_sort(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the two highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_sort(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """
    # Sort a copy of amounts
    temp_amounts : List[int] = sorted(amounts, reverse = True)

    # Get the two highest values
    highest : int = temp_amounts[0]
    next_highest : int = temp_amounts[1]
    
    # Find their indices in the original list
    high_index1 : int = amounts.index(highest)
    high_index2 : int = amounts.index(next_highest)
    
    # Return the two indices
    return (high_index1, high_index2)

find_two_highest_sort([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])
```

* 2、Sort

```python
from typing import List, Tuple

def find_two_highest_walk(amounts : List[int]) -> Tuple[int, int]:
    """Return a tuple of the indices of the tow highest values in list amounts.
    >>> seals = [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    >>> find_two_highest_walk(seals)
    (3, 4)
    >>> seals == [334, 468, 549, 836, 660, 389, 308, 392, 520, 271]
    True
    """

    # Keep track of the indices of the two highest values found so far
    if amounts[0] > amounts[1]:
        high_index1, high_index2 = 0, 1
    else:
        high_index1, high_index2 = 1, 0
        
    # Examine each value in the list in order
    for i in range(2, len(amounts)):
    #     Update the indices when a new higher value is found
        if amounts[i] > amounts[high_index1]:
            high_index2 = high_index1
            high_index1 = i
        elif amounts[i] > amounts[high_index2]:
            high_index2 = i
        
    # Return the two indices 
    return (high_index1, high_index2)

find_two_highest_walk([334, 468, 549, 836, 660, 389, 308, 392, 520, 271])
```

* 3、Walk through the list

* 速度1>2>3

```python
from typing import Any

def linear_search(lst : list, value : Any) -> int:
    """Return the index of the first occurrence of value in lst,
    return -1 if value is not in lst.
    
    >>> linear_search([2, 5, 1, -3], 5)
    1
    >>> linear_search([2, 4, 2], 2)
    0
    >>> linear_search([2, 5, 1, -3], 4)
    -1
    >>> linear_search([], 5)
    -1
    """
    
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1
```

* 线性搜索

```python
from typing import Any

def binary_search(lst : list, value : Any) -> int:
    """ Return the index of the first occurrence of the value in lst, 
    or return -1 if the value is not found in lst.
    
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 1)
    0
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 4)
    2
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 5)
    4
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 10)
    7
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], -3)
    -1
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 11)
    -1
    >>> binary_search([1, 2, 4, 4, 5, 7, 9, 10], 3)
    -1
    >>> binary_search([], -3)
    -1
    >>> binary_search([1], 1)
    0
    """
    
    # Mark the left and right indices of the part of the list to be searched
    i : int = 0
    j : int = len(lst) - 1
    
    while i != j + 1:
        m = (i + j) // 2
        if lst[m] < value:
            i = m + 1
        else:
            j = m - 1
    
    if 0 <= i < len(lst) and lst[i] == value:
        return i
    else:
        return -1

    
binary_search([1, 2, 4, 4, 5, 7, 9, 10, 12, 15, 
               20, 20, 25, 33, 33, 44, 55, 60, 
               61, 62, 64, 67, 70, 73, 76, 78], 55)
```

* 二分法搜索(排序好的列表)

## Sorting

* 冒泡排序(for(for))
* 插入排序(比较，替换(for(while)))
* 合并排序
* 快排

## Pandas

* import pands as pd

### Series Object

* 类字典

```python
vowels: pd.Series = pd.Series(['a', 'e', 'i', 'o', 'u'])
vowels

0    a
1    e
2    i
3    o
4    u
dtype: object
    
vowel.values
vowel.index

linear: pd.Series = pd.Series(np.linspace(0, 1, 5), index=['a', 'b', 'c', 'd', 'e'])
    
a    0.00
b    0.25
c    0.50
d    0.75
e    1.00
dtype: float64
```

### DataFrame Object

* 一系列Series类型的对象

```python
pd.DataFrame(municipalities_series, columns=['municipalities'])
```

<img src="C:\Users\Sean\AppData\Roaming\Typora\typora-user-images\1666017901884.png" alt="1666017901884" style="zoom: 33%;" />

```python
import random as rd

dict1: dict = {'a': rd.randint(0, 100), 'b': rd.randint(0, 100), 'c': rd.randint(0, 100)}
dict2: dict = {'b': rd.randint(0, 100), 'c': rd.randint(0, 100)}
dict3: dict = {'a': rd.randint(0, 100), 'b': rd.randint(0, 100)}
    
pd.DataFrame([dict1, dict2, dict3])
```

![1666018017051](C:\Users\Sean\AppData\Roaming\Typora\typora-user-images\1666018017051.png)

```python
pd.DataFrame(np.random.randint(0, 100, (4, 3)),
            columns=['apples', 'bananas', 'pears'],
            index=['A', 'B', 'C', 'D'])
```

![1666018161094](C:\Users\Sean\AppData\Roaming\Typora\typora-user-images\1666018161094.png)

### Index Object

* Pandas内置的index类型，***immutable***

```python
ind: pd.Index = pd.Index([1, 3, 5, 7, 9])
ind
Int64Index([1, 3, 5, 7, 9], dtype='int64')

ind[1::2]

rand: pd.Series = pd.Series(np.random.random(8))
rand

0    0.901432
1    0.979631
2    0.670806
3    0.532514
4    0.334909
5    0.997718
6    0.863905
7    0.581134
dtype: float64
    
rand[(rand > 0.25) & (rand < 0.75)]

2    0.670806
3    0.532514
4    0.334909
7    0.581134
dtype: float64

linear: pd.Series = pd.Series(np.linspace(0, 1, 5), index=[1, 3, 5, 7, 9])
linear

1    0.00
3    0.25
5    0.50
7    0.75
9    1.00
dtype: float64

# 显式是闭区间，隐式是左闭右开
linear.loc[1:3] ->显式索引 explicit index
1    0.00
3    0.25
dtype: float64
    
linear.iloc[1:3] ->隐式索引 implicit index
3    0.25
5    0.50
dtype: float64

```













* wines: Dict[str, list] = pd.DataFrame(data) ->pd中转DataFrame格式
* wines.loc[2] ->表格第二行

![1665433443748](C:\Users\Sean\AppData\Roaming\Typora\typora-user-images\1665433443748.png)

* mean = wines['points'].mean() ->pd求平均数
* 同样的, median和mode(众数)也一样
* var()方差 std()标准差 

```python
q1 = wines['points'].quantile(0.25, interpolation='lower')
q3 = wines['points'].quantile(0.75, interpolation='lower')
iqr = q3 - q1
iqr
```

* 四分位间距 ↑

* boxplot = wines.boxplot(column=['points'])  ->箱形图

* hist = wines.hist(column='price', rwidth=0.9, gird=False, bins=100)

  rwidth(每个bar占一个bin的多少)

  grid(有无网格)

  bins(把x轴分成多少块)

## Numpy

```python
import numpy as np
primes: list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
scale: list = [1, 2, 3, 4, 5]
    
np_primes: np.ndarray = np.array(primes) ->numpy的列表
np_scale: np.ndarray = np.array(scale, dtype='float_')
                                      ->int 转float 例如1. 2.
ones: np.ndarray = np.ones(8, dtype='int_') ->默认是float
    # array([1, 1, 1, 1, 1, 1, 1, 1])
pi_numbers: np.ndarray = np.full(8, 3.1418)
    # array([3.1418, 3.1418, 3.1418, 3.1418, 3.1418, 3.1418, 3.1418, 3.1418])
    
nested_lists = [list(range(i, i + 3)) for i in [1, 4, 7]]
    # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(nested_lists)
    # array([[1, 2, 3],
    #        [4, 5, 6],
    #        [7, 8, 9]])
np.arange(0, 10, 2) ->线性序列
    # array([0, 2, 4, 6, 8])
np.linspace(0, 1, 5) ->均匀间隔
    # array([0., 0.25, 0.5, 0.75, 1.])
np.random.random((3, 4)) ->0到1中随机生成一个3×4的矩阵
np.random.randint(0, 100, (4, 4)) ->0到100中随机生成一个4×4矩阵
    # array([[12, 87, 24,  8],
    #        [89, 77, 74, 71],
    #        [69, 71, 74, 79],
    #        [ 6, 23, 45, 21]])
np.random.normal(0, 1, (4, 4)) -> 平均值为0，标准差为1
np.random.randint(10, size=(2, 3, 6))

One-dimensional array: ndim=1, shape=(6,), size=6
Two-dimensional array: ndim=2, shape=(2, 6), size=12
Three-dimensional array: ndim=3, shape=(2, 3, 6), size=36
    
rows, columns = integers.shape ->获得shape的行数与列数
```

### Slice

* x[start:stop:step]

* first_five: np.ndarray = prime[:5]

  array([ 2, 3, 5, 7, 11])

* every_two_half = primes[::2] ->间隔为2的切片

* sub_integers: np.ndarray = integers[:2, :2].copy()

### Masking

```python
integers >= 5 ->转bool值mask
array([[False, False, False],
       [False,  True,  True],
       [ True,  True,  True]])
```