from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

# coding
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "e-cycling-382122",
  "private_key_id": "47e933ca8a093cf1562024c37661fd19f101069b",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQCrB5XgTLk2AK25\nQ25dNR8XJKe6gLpSq50q0t1VSkormkLvVroaUZHNOl51FXnM8RD9zfcHq2Uua2rS\nrmxgiXl8xLvCXM50xS9QotZjOYGFBiiaLza+gsbv02kFOtnZv4S3OdhVNQ1EAqfF\nC94Avq7tCjmYvsH0DPp11XdIupU9J7X1D9+gwvrgwA2xEmRicvbZmvSY1Gi7vhGB\nLzrSuWCVScEGBzbUBQnHhtWIP467mhW/WbQC2+qRkTZ7vMnYcwK0ebyee0lWmdNa\nctAbdQZuXCUf8EO3/CtdP7cwP+n6FimcdEen8wLGFIG/6YZxpYE3/UN6ebw8VGer\ns8M3SWoRAgMBAAECggEAASVTjSl0bPLBlzH3BIG3aes3YrPrs6O10YhwvkpZb3v4\nxnPWOriIzZc+VGJawttLV+j0Jolw28gRUtSjchzfqwziHWPr5+s9hTi3Dxp+tjR/\nq4NFFo8HnEoWPDhMBvX+EpBtFSqOIoJSS4sYH1kHsNu6fa4K/HqlB6qwwjRqTSri\n8ZhitcvN9/YXbpoJrVC8obLg9aPmQUTpc1kGeeBymQ+m1DMlH4dpBK1gGaUt6Wdx\nXF3C0y5l2plzuwkoRL54Od8JhXE9vEOHftlWRieb5sqWLfyCVYOFeJ8TWBjRy5FW\n98bD5kxZM9IykQzF9FSY1v4J5/hVaJERUSLbO9/rQQKBgQDeH132AMYUvjpU61vz\nXe2v+wMByGiiQj/jx4zOmlg8wNaROA40M9UP3PnpM2Mp26TCCw82Ws1okJND3dQY\nYHuGTqkgeEU4XMhYfwhyi2TkxH8NvQGK5XItSYuRPYNQXrm2s3gkyWS408okV1ZU\nXeWazI8oPZqUWrQd4+dhCLvoQQKBgQDFHVQnQCOEpSps+Joux7bCMBtMxs9SM5L3\nv/1DpTN+avPjeUxhvtCnngNODhMhz4kDymBRKKx/Kby1JcEowxRBa09OW+scvlZp\ni6uYtjZcrwI972m06OznJSG/TUVRVjCW2KtHmgLKjuaLeMaAnto4gZWYVemvbZxr\nn/nwIbWN0QKBgQCyM3QMgr5nsd3WdyRD8R1ZzAWzjnbzhjb/pP6AWi9kPklmJBSx\nKMxMd7o/ryxlToO18W147AxTUXn0PqmEDRPMwprJI/RUrYtGBFRgoRiGuGY+PV5Z\nco7RammAUlthRT21J/LBgJk/9xn7Yd4uvU4RjP9lB1dWohZSzJ66qGkogQKBgQCa\n8yk6CaNiHGwzaWHasEgscqCjRA2psr0vYI745B6MnArIoIu4ssVXXlF+xHWpuHke\nr7HzWqPu+qJLTDiBkIiVvIOFN6Ck4cMQCSmFTIeDaFe81D0mZ4wDUB8tQNLi03wy\nuHQ8Pwc+sALvVKvGZBlrHgK406B1tRanTASwDe+oYQKBgQDS8MD6TgDtfmtpCUah\n/cAnQlrx7oQEqB2U4iNLpZLpp8IBwRftu/AVavF5cLJthzdmREVkMft6ScGIRzZE\n70vzkXLh4cDwWC7nOCy5neoebI3w6J2qhZl0w3hJyEjjI+Ps+aAU8UbYlzgyRRU0\nJZIaUPXPC0namI439lIpCLaz+A==\n-----END PRIVATE KEY-----\n",
  "client_email": "975177100251-compute@developer.gserviceaccount.com",
  "client_id": "117044790078051334110",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/975177100251-compute%40developer.gserviceaccount.com"
}

try:
  res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
  
  print(info)

  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('weather_teste')
  blob = bucket.blob('weather_info.txt')

    #   with open('weather_info.txt', 'a') as f:
    #     f.write(info + '\n')

    #   print("Finished.")

  blob.upload_from_string(info + '\n')

  print('File uploaded.')

  print("Finished.")

except Exception as ex:
  print(ex) 