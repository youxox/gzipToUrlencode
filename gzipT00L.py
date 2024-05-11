import gzip
from urllib.parse import quote_plus

"""
脚本会读取需要上传的webshell文件并对其进行gzip压缩在进行url编码,以便进行webshell上传
jsp -> gzip -> url编码
"""


def gzip_compress_and_url_encode(file_path):
    # 读取并压缩文件
    with open(file_path, 'rb') as file:
        data = file.read()
        compressed_data = gzip.compress(data)

    # 进行URL编码
    url_encoded_data = quote_plus(compressed_data)

    return url_encoded_data


# 假定你的txt文件路径
input_file_path = '要读取的木马文件'
encoded_string = gzip_compress_and_url_encode(input_file_path)
print(encoded_string)
