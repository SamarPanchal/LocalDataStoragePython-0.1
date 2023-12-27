import os


class LocalDataStore:
    def __init__(self, file_type):
        self.value = None
        self.file_type = file_type
        if self.file_type == '':
            self.file_type = 'txt'

    def save_data(self, filename):
        try:
            with open(str(filename) + "." + str(self.file_type), 'x') as f:
                return True
        except Exception as e:
            print(e)

    def load_data(self, filename):
        try:
            with open(str(filename) + "." + str(self.file_type), 'r') as f:
                data = f.read()
                return data
        except Exception as e:
            print(e)

    def update_data(self, filename, value):
        self.value = value
        try:
            with open(str(filename) + "." + str(self.file_type), 'w') as f:
                f.write(value)
        except Exception as e:
            print(e)

    def delete_data(self, filename):
        try:
            os.remove(str(filename) + "." + str(self.file_type))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    print("main.py file")
