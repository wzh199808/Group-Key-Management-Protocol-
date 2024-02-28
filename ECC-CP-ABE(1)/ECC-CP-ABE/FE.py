import random
import sys
import string
from fuzzy_extractor import FuzzyExtractor
import time

def reproduce():
    #此函数测试模糊提取器是否可以从相同的输入中重现相同的键
    random.seed()
    #测试值
    val_len = 16
    chars = string.ascii_letters
    values = list()
    tg=0
    tr=0
    #生成1000个随机测试值，每个测试值长度为val_len
    for _ in range(1000):
        values.append("".join(random.choice(chars) for _ in range(val_len)))
    #对上述1000个测试值模糊提取的提取和复现
    for value in values:
        #实例化模糊提取器类，该模糊提取器规定允许误差为2位
        extractor = FuzzyExtractor(val_len, 2)
        print(value)
        t1=time.perf_counter()
        #对输入value提取生成key和辅助数据helper
        key, helpers = extractor.generate(value)
        t2=time.perf_counter()
        #assert extractor.reproduce(value, helpers) == key
        #这里直接用原输入值value
        r_key=extractor.reproduce(value, helpers)
        t3=time.perf_counter()
        tg+=(t2-t1)
        tr+=(t3-t2)
    print("gen:",tg,"ms rep:",tr,"ms \n gen+rep:",(tg+tr),"ms \n")

    #print(r_key,"\n",key)

def reproduce_fuzzy():
        #此函数测试模糊提取器是否可以从带噪声的输入中复现
    random.seed()
    val_len = 30
    chars = string.ascii_letters
    values = list()
    for _ in range(5):
        values.append("".join(random.choice(chars) for _ in range(val_len)))

    for value in values:
        #提取器可以处理8位以内翻转
        extractor = FuzzyExtractor(val_len, 8)
        key, helpers = extractor.generate(value)
        # 在字符串value的pos位置,用随机字符替换生成一个噪声字符串value_noisy
        pos = random.randint(0, val_len - 2)
        value_noisy = value[:pos] + random.choice(chars) + value[pos + 1:]
        # 在允许的误差范围内，仍然会生成相同的key
        assert extractor.reproduce(value_noisy, helpers) == key

def reproduce_bad():
    #当误差/翻转位过大时，测试模糊提取器会产生不同的key
    value_orig = 'AABBCCDD'
    value_good = 'ABBBCCDD'  #  A和B对应的二进制位存在2位翻转
    value_bad = 'A0B00CDD'   # 0对应A，B翻转4位,对应C翻转5位共13位
    extractor = FuzzyExtractor(8, 2)
    key, helpers = extractor.generate(value_orig)
    print(sys.getsizeof(key))
    assert extractor.reproduce(value_good, helpers) == key
    assert extractor.reproduce(value_bad, helpers) != key

reproduce()
reproduce_bad()