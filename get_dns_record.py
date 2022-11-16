import dns.resolver
from dns import reversename, resolver


# 根据域名查询ip地址
domain = 'www.baidu.com'
qtype = 'A'
answer = dns.resolver.resolve(domain,qtype, raise_on_no_answer=False)
if answer.rrset is not None:
    print(answer.rrset)



# 根据ip地址查询域名
ip = '76.248.80.112' #github.com 的ip
domain_address = reversename.from_address(ip)
print(domain_address)
qtype = 'PTR'
domain_name = str(resolver.resolve(domain_address, qtype)[0])
print(domain_name)


#!/usr/local/bin/python38

# import dns.resolver
# import httplib2
#
# iplist = []
# appdomain = "www.baidu.com"
#
# def get_iplist(domain=""):
#     try:
#         A = dns.resolver.resolve(domain,"A")
#     except Exception as e:
#         print("dns resolver error:" + str(e))
#         return
#     for i in A.response.answer:
#         for j in i.items:
#             if j.rdtype == 1:
#                 iplist.append(j.address)
#     return True
#
# def checkip(ip):
#     checkurl = 'http://' + ip + ":80"
#     getcontent = ""
#     httplib2.socket.setdefaulttimeout(5)
#     conn = httplib2.Http()
#
#     try:
#         resp,getcontent=conn.request(checkurl)
#     finally:
#         if  resp['status']== "200":
#             print(ip+"[OK]")
#         else:
#             print(ip+"[Error]")
#
#
# if __name__ == "__main__":
#     if get_iplist(appdomain) and len(iplist) > 0:
#         for ip in iplist:
#             checkip(ip)


