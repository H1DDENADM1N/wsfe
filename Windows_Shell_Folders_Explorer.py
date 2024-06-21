import subprocess
import time

__LANGUAGE__ = "cn"


class WindowsShellFoldersExplorer:
    def __init__(self):
        self.folders_dict: dict[int, str] = {
            1: "Administrative Tools",
            2: "AppData",
            3: "CD Burning",
            4: "Cache",
            5: "Common Administrative Tools",
            6: "Common AppData",
            7: "Common Desktop",
            8: "Common Documents",
            9: "Common Programs",
            10: "Common Start Menu",
            11: "Common Startup",
            12: "Common Templates",
            13: "CommonMusic",
            14: "CommonPictures",
            15: "CommonVideo",
            16: "Cookies",
            17: "Desktop",
            18: "Favorites",
            19: "Fonts",
            20: "History",
            21: "Local AppData",
            22: "My Music",
            23: "My Pictures",
            24: "My Video",
            25: "NetHood",
            26: "OEM Links",
            27: "Personal",
            28: "PrintHood",
            29: "Programs",
            30: "Recent",
            31: "SendTo",
            32: "Start Menu",
            33: "Startup",
            34: "Templates",
        }
        self.folders_about_dict: dict[int, str] = {
            1: "These are the tools and settings that are available to administrators on a Windows system.",
            2: "This folder contains application data for the current user.",
            3: "This folder is used to hold CDs that are in the process of being burned.",
            4: "This folder is used to cache application data for faster access.",
            5: "This folder contains tools and settings that are available to all users on a Windows system.",
            6: "This folder contains application data that is shared across all users on the system.",
            7: "This folder is the default location for new desktop shortcuts.",
            8: "This folder is the default location for new document shortcuts.",
            9: "This folder contains shortcuts to programs that are commonly used.",
            10: "This folder is the default location for new start menu shortcuts.",
            11: "This folder contains programs that are started automatically when a user logs on.",
            12: "This folder contains templates that can be used to create new documents or other items.",
            13: "This folder contains music files.",
            14: "This folder contains pictures.",
            15: "This folder contains video files.",
            16: "This folder contains cookies.",
            17: "This folder is the default location for new desktop shortcuts.",
            18: "This folder contains shortcuts to items that the user has marked as favorite.",
            19: "This folder contains font files.",
            20: "This folder contains a history of the user's activities.",
            21: "This folder contains application data that is specific to the current user.",
            22: "This folder contains music files.",
            23: "This folder contains pictures.",
            24: "This folder contains video files.",
            25: "This folder contains network shortcuts.",
            26: "This folder contains links to manufacturer-specific drivers and utilities.",
            27: "This folder is the default location for new document shortcuts.",
            28: "This folder contains printers that are available to the user.",
            29: "This folder contains shortcuts to programs that are commonly used.",
            30: "This folder contains shortcuts to recently used items.",
            31: "This folder contains shortcuts to items that can be sent to other users.",
            32: "This folder is the default location for new start menu shortcuts.",
            33: "This folder contains programs that are started automatically when a user logs on.",
            34: "This folder contains templates that can be used to create new documents or other items.",
        }
        self.folders_about_dict_cn: dict[int, str] = {
            1: "管理员在 Windows 系统上可用的工具和设置。",
            2: "当前用户的应用程序数据。",
            3: "保存即将烧录的 CD。",
            4: "缓存应用程序数据以提高访问速度。",
            5: "Windows 系统上所有用户都可用的工具和设置。",
            6: "系统上所有用户共享的应用程序数据。",
            7: "新桌面快捷方式的默认位置。",
            8: "新文档快捷方式的默认位置。",
            9: "常用程序的快捷方式。",
            10: "新开始菜单快捷方式的默认位置。",
            11: "用户登录时自动启动的程序。",
            12: "可用于创建新文档或其他项目的模板。",
            13: "音乐文件。",
            14: "图片。",
            15: "视频文件。",
            16: "Cookie。",
            17: "新桌面快捷方式的默认位置。",
            18: "用户标记为收藏的项目的快捷方式。",
            19: "字体文件。",
            20: "用户活动的历史记录。",
            21: "特定于当前用户的应用程序数据。",
            22: "音乐文件。",
            23: "图片。",
            24: "视频文件。",
            25: "网络快捷方式。",
            26: "制造商驱动程序和实用程序的链接。",
            27: "新文档快捷方式的默认位置。",
            28: "用户可用打印机。",
            29: "常用程序的快捷方式。",
            30: "最近使用项目的快捷方式。",
            31: "可发送到其他用户的项目的快捷方式。",
            32: "新开始菜单快捷方式的默认位置。",
            33: "用户登录时自动启动的程序。",
            34: "可用于创建新文档或其他项目的模板。",
        }

    def open_shell_folder(self, folder_id: int) -> None:
        if folder_id not in self.folders_dict:
            match __LANGUAGE__:
                case "cn":
                    print(f"文件夹编号 {folder_id} 不存在，请输入正确的编号。")
                case _:
                    print(
                        f"Folder ID {folder_id} does not exist, please enter a valid ID."
                    )
            time.sleep(2)
            return

        try:
            subprocess.Popen(f"explorer shell:{self.folders_dict[folder_id]}")
        except Exception as e:
            print(
                f"Error while opening folder {folder_id}. {self.folders_dict[folder_id]}, Error message: {e}"
            )

    def print_folder_about(self) -> None:
        match __LANGUAGE__:
            case "cn":
                for folder_id in self.folders_dict:
                    print(
                        f"{folder_id}: {self.folders_dict[folder_id]}\n └───{self.folders_about_dict_cn[folder_id]}\n"
                    )
                print("请输入要打开的文件夹的编号：(输入 q 退出)")
            case _:
                for folder_id in self.folders_dict:
                    print(
                        f"{folder_id}: {self.folders_dict[folder_id]}\n └───{self.folders_about_dict[folder_id]}\n"
                    )
                print(
                    "Enter the number of the folder you want to open: (enter q to exit)"
                )


if __name__ == "__main__":
    wsfe = WindowsShellFoldersExplorer()
    while True:
        subprocess.call("cls", shell=True)
        wsfe.print_folder_about()
        user_command = input()
        if user_command == "q":
            break
        wsfe.open_shell_folder(int(user_command))
