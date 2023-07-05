# from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
# import asyncio
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import aiohttp
# from checkLiveProxy import check_proxy


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.table_widget = QTableWidget(self)
#         self.setCentralWidget(self.table_widget)

#     async def main(self):
#         proxies = open("proxies.txt", "r").read().split()

#         tasks = []
#         async with aiohttp.ClientSession() as session:
#             for proxy in proxies:
#                 proxy = proxy.split(":")
#                 task_check_proxy = check_proxy(*proxy)
#                 tasks.append(asyncio.gather(task_check_proxy))

#             results = await asyncio.gather(*tasks)

#             # Hiển thị kết quả lên QTableWidget
#             self.table_widget.setRowCount(len(results))
#             self.table_widget.setColumnCount(2)

#             for idx, value in enumerate(results):
#                 print(idx, value)
#                 item = QTableWidgetItem(f"{value}")
#                 self.table_widget.setItem(idx, 0, item)
#                 # self.table_widget.setItem(idx, 1, QTableWidgetItem(value))

#         self.table_widget.resizeColumnsToContents()


# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     asyncio.run(window.main())
#     window.show()
#     app.exec_()

import asyncio
from checkLiveProxy import check_proxy


async def main():
    proxies = open("proxies.txt", "r").read().split()
    tasks = []
    for proxy in proxies:
        proxy = proxy.split(":")
        tasks.append(asyncio.create_task(check_proxy(*proxy)))
    result = await asyncio.gather(*tasks)
    print(result)


asyncio.run(main())
