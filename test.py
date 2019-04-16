from sklearn.feature_extraction import DictVectorizer

def dictvec():
    """
    字典数字抽取
    ：return: None
    """
    dict = DictVectorizer()

    data = dict.fit_transform([{'city':'北京','temperature':100},
    {'city':'上海','temperature':80},{'city':'深圳','temperature':60}])

    print(data)

    return None


if __name__=="__main__":
    dictvec()