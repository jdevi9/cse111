from ciphers import caeserCipherEncrypt, \
    caeserCipherDecrypt, vingereCipherDecrypt, vingereCipherEncrypt 
import pytest

def test_caeserCipherEncrypt():
    message = "meet me behind the tables"
    encryptedMessage = caeserCipherEncrypt(message, 3)
    assert len(message) == len(encryptedMessage)

def test_caeserCipherDecrypt():
    message = "QIIX QI FILMRH XLI XEFPIW"
    key = 4 
    decryptedMessage = caeserCipherDecrypt(message, key)
    assert len(message) == len(decryptedMessage)
    assert decryptedMessage == "MEET ME BEHIND THE TABLES"

def test_rot13CipherEncrypt():
    message = "meet"
    encryptedMessage = caeserCipherEncrypt(message, 13)
    assert len(message) == len(encryptedMessage)
    assert encryptedMessage == "ZRRG"

def test_vingereCipherEncrypt():
    message = "meet me behind the tables"
    key = "pizza"
    encryptedMessage = vingereCipherEncrypt(message, key)
    assert len(message) == len(encryptedMessage)
    assert encryptedMessage == "bmds mt jdgicl sge iiakeh"

def test_vingereCipherDecrpyt():
    message = "bmds mt jdgicl sge iiakeh"
    key = "pizza"
    decryptedMessage = vingereCipherDecrypt(message, key)
    assert len(message) == len(decryptedMessage)
    assert decryptedMessage == "meet me behind the tables"
    
pytest.main(["-v", "--tb=line", "-rN", __file__])