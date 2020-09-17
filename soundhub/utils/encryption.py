from Crypto.Cipher import XOR
import base64


def encrypt(key, plain_text):
    """
    :param key: 32 byte 길이의 문자열. 나중에 암호를 푸는데 사용된다.
    :param plain_text: 암호화하고 싶은 평문
    :return: 암호화된 byte 타입 데이터
    """
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plain_text))


def decrypt(key, encrypted_text):
    """
    :param key: 암호화에 사용되었던 32 byte 길이의 문자열
    :param encrypted_text: 암호화된 byte 타입 데이터
    :return: 복호화된 평문
    """
    # 암호문이 "b'1234'" 형태의 문자열로 오는 경우
    if type(encrypted_text) is str:
        encrypted_text = encrypted_text[2:][:-1].encode('utf-8')

    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(encrypted_text)).decode('utf-8')
