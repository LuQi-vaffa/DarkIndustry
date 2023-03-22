import OpenSSL
import ssl


def check_cert_valid(domian):
    # 这里还有一些代码，用来获取域名列表，情况不同，不阐述了

    # 这里我直接使用了下述方法来获取证书，并没有将证书写入文件
    cert = ssl.get_server_certificate((domian, 443))  # 一般是443端口,并且这里默认返回
                                                        # 的是PEM证书
    print(cert)
    # 如果有cert文件的话，直接执行这里
    # cert_file_path = ''  # cert证书文件路径
    # cert = open(cert_file_path).read()  # 当然这里也可以使用with来进行上下文管理
    certification = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    # print(certification)
    # valid_start_time = certification.get_notBefore()  # 有效期起始时间
    # valid_end_time = certification.get_notAfter()  # 有效期结束时间
    return cert



check_cert_valid("www.baidu.com")

