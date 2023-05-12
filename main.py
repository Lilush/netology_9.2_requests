import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        self.base_url = 'https://cloud-api.yandex.net/'

    def get_headers(self):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}',
        }
        return headers

    def _get_upload_url(self, disk_file_path):
        file_url = self.base_url + "v1/disk/resources/upload"
        headers = self.get_headers()
        params = {
            'path': disk_file_path,
            'overwrite': True,
        }
        response = requests.get(file_url, params=params, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data['href']
        else:
            return ""
        
    def upload(self, file_path: str):
        upload_url = self._get_upload_url(file_path)
        response = requests.put(upload_url, data=open(file_path, 'rb'))
        return response.status_code


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
    print(result)
