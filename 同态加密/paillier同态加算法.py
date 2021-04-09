# -*- encoding: utf-8 -*-
from phe import paillier
import numpy as np

print('第一步,生成公钥私钥')
public_key, private_key = paillier.generate_paillier_keypair(n_length=34)
print('公钥的g：', public_key.g, '公钥的n：',public_key.n)
print('私钥的p：', private_key.p, '私钥的q：', private_key.q)

print('\n第二步,加密原始数据')
A=[3,32]
B=[4,16]
print('原始数据A：', A)
print('原始数据B：', B)
enA=[public_key.encrypt(x) for x in A]
enB=[public_key.encrypt(x) for x in B]
print("加密后的A：",enA[0].ciphertext(False),enA[1].ciphertext(False))
# print(enA[0].ciphertext(True).bit_length())
print("加密后的B：",enB[0].ciphertext(False),enB[1].ciphertext(False))
# print(enB[0].ciphertext(False).bit_length())

print('\n第三步,执行给定的加运算')
en=np.add(enA,enB)
print("加密后的A+B：",en[0].ciphertext(False),en[1].ciphertext(False))
# print(en[0].ciphertext(False).bit_length())

print('\n第四步,解密结果')
print("解密后的结果:", [private_key.decrypt(x) for x in en])

