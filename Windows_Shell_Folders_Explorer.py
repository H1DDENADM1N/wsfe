import subprocess
import time
from typing import OrderedDict

__LANGUAGE__ = "cn"


class WindowsShellFoldersExplorer:
    """
    A class to manage the Windows shell folders.

    Attributes:
        - folders_dict: A dictionary containing the shell folders and their descriptions.

    Funtions:
        - open_shell_folder(folder_id: int) -> None: Opens the shell:<***> folder in explorer with the given ID.
        - print_folder_about() -> None: Prints a list of all the shell folders and their descriptions.
    """

    def __init__(self):
        self.folders_dict: dict[str, tuple[str, str]] = OrderedDict(
            {
                # Format："Folder Name": ("Description in English", "中文描述")
                # You cam note or remove the comments below if you don't need them, nothing else needs to be changed.
                "Administrative Tools": (
                    "These are the tools and settings that are available to administrators on a Windows system.",
                    "管理员在 Windows 系统上可用的工具和设置。",
                ),
                "AppData": (
                    "This folder contains application data for the current user.",
                    "当前用户的应用程序数据。",
                ),
                "AppsFolder": (
                    "This folder contains the programs and shortcuts that are installed on the system.",
                    "系统上安装的程序和快捷方式。",
                ),
                "CD Burning": (
                    "This folder is used to hold CDs that are in the process of being burned.",
                    "保存即将烧录的 CD。",
                ),
                "Cache": (
                    "This folder is used to cache application data for faster access.",
                    "缓存应用程序数据以提高访问速度。",
                ),
                "Common Administrative Tools": (
                    "These are the tools and settings that are available to all users on a Windows system.",
                    "Windows 系统上所有用户都可用的工具和设置。",
                ),
                "Common AppData": (
                    "This folder contains application data that is shared across all users on the system.",
                    "系统上所有用户共享的应用程序数据。",
                ),
                "Common Desktop": (
                    "This folder is the default location for new desktop shortcuts.",
                    "新桌面快捷方式的默认位置。",
                ),
                "Common Documents": (
                    "This folder is the default location for new document shortcuts.",
                    "新文档快捷方式的默认位置。",
                ),
                "Common Programs": (
                    "This folder contains shortcuts to programs that are commonly used.",
                    "常用程序的快捷方式。",
                ),
                "Common Start Menu": (
                    "This folder is the default location for new start menu shortcuts.",
                    "新开始菜单快捷方式的默认位置。",
                ),
                "Common Startup": (
                    "This folder contains programs that are started automatically when a user logs on.",
                    "用户登录时自动启动的程序。",
                ),
                "Common Templates": (
                    "This folder contains templates that can be used to create new documents or other items.",
                    "可用于创建新文档或其他项目的模板。",
                ),
                "CommonMusic": ("This folder contains music files.", "音乐文件。"),
                "CommonPictures": ("This folder contains pictures.", "图片。"),
                "CommonVideo": ("This folder contains video files.", "视频文件。"),
                "Cookies": ("This folder contains cookies.", "Cookie。"),
                "Desktop": (
                    "This folder is the default location for new desktop shortcuts.",
                    "新桌面快捷方式的默认位置。",
                ),
                "Favorites": (
                    "This folder contains shortcuts to items that the user has marked as favorite.",
                    "用户标记为收藏的项目的快捷方式。",
                ),
                "Fonts": ("This folder contains font files.", "字体文件。"),
                "History": (
                    "This folder contains a history of the user's activities.",
                    "用户活动的历史记录。",
                ),
                "Libraries": (
                    "This folder contains libraries, which are collections of documents, music, and other files.",
                    "文档、音乐和其他文件的集合。",
                ),
                "Local AppData": (
                    "This folder contains application data that is specific to the current user.",
                    "特定于当前用户的应用程序数据。",
                ),
                "My Music": ("This folder contains music files.", "音乐文件。"),
                "My Pictures": ("This folder contains pictures.", "图片。"),
                "My Video": ("This folder contains video files.", "视频文件。"),
                "NetHood": (
                    "This folder contains network shortcuts.",
                    "网络快捷方式。",
                ),
                "OEM Links": (
                    "This folder contains links to manufacturer-specific drivers and utilities.",
                    "制造商驱动程序和实用程序的链接。",
                ),
                "Personal": (
                    "This folder is the default location for new document shortcuts.",
                    "新文档快捷方式的默认位置。",
                ),
                "PrintHood": (
                    "This folder contains printers that are available to the user.",
                    "用户可用打印机。",
                ),
                "Programs": (
                    "This folder contains shortcuts to programs that are commonly used.",
                    "常用程序的快捷方式。",
                ),
                "ProgramFiles": (
                    "This folder contains 64-bit programs.",
                    "64 位程序。",
                ),
                "ProgramFilesCommon": (
                    "This folder contains programs and settings that are shared between users.",
                    "用户之间共享的程序和设置。",
                ),
                "ProgramFilesX86": (
                    "This folder contains 64-bit programs.",
                    "64 位程序。",
                ),
                "ProgramFilesCommonX86": (
                    "This folder contains programs and settings that are shared between users.",
                    "用户之间共享的程序和设置。",
                ),
                # "Quick Launch": (
                #     "This folder contains shortcuts to programs that are frequently used. Used by old versions of Windows.",
                #     "旧版 Windows 常用程序的快捷方式。",
                # ),
                "Recent": (
                    "This folder contains shortcuts to recently used items.",
                    "最近使用项目的快捷方式。",
                ),
                "RecycleBinFolder": (
                    "This folder contains items that have been deleted.",
                    "已删除的项目。",
                ),
                "SendTo": (
                    "This folder contains shortcuts to items that can be sent to other users.",
                    "可发送到其他用户的项目的快捷方式。",
                ),
                "Start Menu": (
                    "This folder is the default location for new start menu shortcuts.",
                    "新开始菜单快捷方式的默认位置。",
                ),
                "Startup": (
                    "This folder contains programs that are started automatically when a user logs on.",
                    "用户登录时自动启动的程序。",
                ),
                "Templates": (
                    "This folder contains templates that can be used to create new documents or other items.",
                    "可用于创建新文档或其他项目的模板。",
                ),
                "UserFilesFolder": (
                    "This folder contains files that are specific to the current user.",
                    "特定于当前用户的文件。",
                ),
                "UsersLibrariesFolder": (
                    "This folder contains libraries, which are collections of documents, music, and other files.",
                    "文档、音乐和其他文件的集合。",
                ),
            }
        )

    def open_shell_folder(self, folder_id: int) -> None:
        """
        Opens the shell:<***> folder in explorer with the given ID.

        :param folder_id: The ID of the shell folder to open.
        """
        if folder_id not in range(1, len(self.folders_dict) + 1):
            match __LANGUAGE__:
                case "cn":
                    print(f"文件夹编号 {folder_id} 不存在，请输入正确的编号。")
                case _:
                    print(
                        f"Folder ID {folder_id} does not exist, please enter a valid ID."
                    )
            time.sleep(2)
            return

        folder_name: str = list(self.folders_dict.keys())[folder_id - 1]
        try:
            subprocess.Popen(f"explorer shell:{folder_name}")
        except Exception as e:
            print(
                f"Error while opening folder {folder_id}. {folder_name}, Error message: {e}"
            )

    def print_folder_about(self) -> None:
        """
        Prints a list of all the shell folders and their descriptions.
        """
        match __LANGUAGE__:
            case "cn":
                for i, (key, value) in enumerate(self.folders_dict.items(), start=1):
                    print(f"{i}: {key}\n └───{value[1]}\n")
                print("请输入要打开的文件夹的编号：(输入 q 退出)")
            case _:
                for i, (key, value) in enumerate(self.folders_dict.items(), start=1):
                    print(f"{i}: {key}\n └───{value[0]}\n")
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
