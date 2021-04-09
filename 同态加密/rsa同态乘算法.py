import rsa.core


print('第一步,生成公钥私钥')
(public_key, private_key) = rsa.newkeys(20)
print('公钥:', public_key)
print('私钥:', private_key)

print('\n第二步,加密原始数据')
A = 2
B = 11
print('原始数据A：', A)
print('原始数据B：', B)
enc1 = rsa.core.encrypt_int(A, public_key.e, public_key.n)
print("加密后的A：", enc1)
enc2 = rsa.core.encrypt_int(B, public_key.e, public_key.n)
print("加密后的B：", enc1)


print('\n第三步,执行给定的乘运算')
result = enc1 * enc2
print("加密后的A*B：",result)


print('\n第四步,解密结果')
decrypt_result = rsa.core.decrypt_int(result, private_key.d, public_key.n)
print("解密后的结果:", decrypt_result)


