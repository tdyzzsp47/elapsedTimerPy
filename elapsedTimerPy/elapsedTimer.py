from time import time

class Timer():
    def __init__(self):
        self.test = 'test'
        self.start = []
        self.times = []
        self.end = []

    def set_start(self):
        if len(self.end) != 0:
            raise Exception("すでに計測終了地点が設定されています")
        self.start.append(
            {
                "name": "start",
                "time": time()
            }
        )

    def add_point(self, name=""):
        if len(self.start) == 0:
            raise Exception("計測開始地点を設定してください")
        if name == "":
            raise Exception("中間地点名を入力してください")
        if len(self.end) != 0:
            raise Exception("すでに計測終了地点が設定されています")
        self.times.append(
            {
                "name": name,
                "time": time()
            }
        )

    def set_end(self):
        if self.start == 0:
            raise Exception("計測開始地点を設定してください")
        self.end.append(
            {
                "name": "end",
                "time": time()
            }
        )

    def print(self):
        if self.start == 0:
            raise Exception("計測開始地点を設定してください")
        if self.end == 0:
            raise Exception("計測終了地点を設定してください")
        time_list = self.start + self.times + self.end
        print("="*30)
        for i, t in enumerate(time_list[:-1]):
            print(t["name"] + "~" + time_list[i+1]["name"])
            print(time_list[i+1]["time"] - t["time"], "[s]")
            print("-"*30)
        print("Total")
        print(self.end[0]["time"] - self.start[0]["time"], "[s]")
        print("="*30)



