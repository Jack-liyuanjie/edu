import hashlib


def pwd(txt):
    # 将明文的txt转成md5格式的密文
    md5_ = hashlib.md5()
    md5_.update(txt.encode('utf-8'))
    md5_.update('@liyuanjie@666#$%*'.encode('utf-8'))  # 自己添加规则原md5无法破解
    return md5_.hexdigest()


if __name__ == '__main__':
    print(pwd('000000'))
