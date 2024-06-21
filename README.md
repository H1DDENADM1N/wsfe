# wsfe (Windows Shell Folders Explorer)

This is a tool to explore Windows shell folders.

It is a single file Python3 script that has no dependency.

It will list all the `shell:<folder>` folders and allow you to open them in Explorer by input the folder list id.

## Usage

### Simply:

```powershell
python Windows_Shell_Folders_Explorer.py
```

### Set Powershell Alias:

```powershell
notepad.exe $PROFILE
```

then add the wsfe function to the file that opens up.

❗Don't forget to change the path to where you saved the Windows_Shell_Folders_Explorer.py.

```powershell
# Windows_Shell_Folders_Explorer
function wsfe {
    python 'C:\Users\user0\Documents\wsfe\Windows_Shell_Folders_Explorer.py'
}
```

## `shell:<folder>` Example Output

You can change the `__LANGUAGE__` variable in the script to change the language of the output.

```
1: Administrative Tools
 └───These are the tools and settings that are available to administrators on a Windows system.

2: AppData
 └───This folder contains application data for the current user.

3: AppsFolder
 └───This folder contains the programs and shortcuts that are installed on the system.

4: CD Burning
 └───This folder is used to hold CDs that are in the process of being burned.

5: Cache
 └───This folder is used to cache application data for faster access.

6: Common Administrative Tools
 └───These are the tools and settings that are available to all users on a Windows system.

7: Common AppData
 └───This folder contains application data that is shared across all users on the system.

8: Common Desktop
 └───This folder is the default location for new desktop shortcuts.

9: Common Documents
 └───This folder is the default location for new document shortcuts.

10: Common Programs
 └───This folder contains shortcuts to programs that are commonly used.

11: Common Start Menu
 └───This folder is the default location for new start menu shortcuts.

12: Common Startup
 └───This folder contains programs that are started automatically when a user logs on.

13: Common Templates
 └───This folder contains templates that can be used to create new documents or other items.

14: CommonMusic
 └───This folder contains music files.

15: CommonPictures
 └───This folder contains pictures.

16: CommonVideo
 └───This folder contains video files.

17: Cookies
 └───This folder contains cookies.

18: Desktop
 └───This folder is the default location for new desktop shortcuts.

19: Favorites
 └───This folder contains shortcuts to items that the user has marked as favorite.

20: Fonts
 └───This folder contains font files.

21: History
 └───This folder contains a history of the user's activities.

22: Libraries
 └───This folder contains libraries, which are collections of documents, music, and other files.

23: Local AppData
 └───This folder contains application data that is specific to the current user.

24: My Music
 └───This folder contains music files.

25: My Pictures
 └───This folder contains pictures.

26: My Video
 └───This folder contains video files.

27: NetHood
 └───This folder contains network shortcuts.

28: OEM Links
 └───This folder contains links to manufacturer-specific drivers and utilities.

29: Personal
 └───This folder is the default location for new document shortcuts.

30: PrintHood
 └───This folder contains printers that are available to the user.

31: Programs
 └───This folder contains shortcuts to programs that are commonly used.

32: ProgramFiles
 └───This folder contains 64-bit programs.

33: ProgramFilesCommon
 └───This folder contains programs and settings that are shared between users.

34: ProgramFilesX86
 └───This folder contains 64-bit programs.

35: ProgramFilesCommonX86
 └───This folder contains programs and settings that are shared between users.

36: Recent
 └───This folder contains shortcuts to recently used items.

37: RecycleBinFolder
 └───This folder contains items that have been deleted.

38: SendTo
 └───This folder contains shortcuts to items that can be sent to other users.

39: Start Menu
 └───This folder is the default location for new start menu shortcuts.

40: Startup
 └───This folder contains programs that are started automatically when a user logs on.

41: Templates
 └───This folder contains templates that can be used to create new documents or other items.

42: UserFilesFolder
 └───This folder contains files that are specific to the current user.

43: UsersLibrariesFolder
 └───This folder contains libraries, which are collections of documents, music, and other files.

Enter the number of the folder you want to open: (enter q to exit)

```

```python
1: Administrative Tools
 └───管理员在 Windows 系统上可用的工具和设置。 

2: AppData
 └───当前用户的应用程序数据。

3: AppsFolder
 └───系统上安装的程序和快捷方式。

4: CD Burning
 └───保存即将烧录的 CD。

5: Cache
 └───缓存应用程序数据以提高访问速度。

6: Common Administrative Tools
 └───Windows 系统上所有用户都可用的工具和设置。

7: Common AppData
 └───系统上所有用户共享的应用程序数据。        

8: Common Desktop
 └───新桌面快捷方式的默认位置。

9: Common Documents
 └───新文档快捷方式的默认位置。

10: Common Programs
 └───常用程序的快捷方式。

11: Common Start Menu
 └───新开始菜单快捷方式的默认位置。

12: Common Startup
 └───用户登录时自动启动的程序。

13: Common Templates
 └───可用于创建新文档或其他项目的模板。        

14: CommonMusic
 └───音乐文件。

15: CommonPictures
 └───图片。

16: CommonVideo
 └───视频文件。

17: Cookies
 └───Cookie。

18: Desktop
 └───新桌面快捷方式的默认位置。

19: Favorites
 └───用户标记为收藏的项目的快捷方式。

20: Fonts
 └───字体文件。

21: History
 └───用户活动的历史记录。

22: Libraries
 └───文档、音乐和其他文件的集合。

23: Local AppData
 └───特定于当前用户的应用程序数据。

24: My Music
 └───音乐文件。

25: My Pictures
 └───图片。

26: My Video
 └───视频文件。

27: NetHood
 └───网络快捷方式。

28: OEM Links
 └───制造商驱动程序和实用程序的链接。

29: Personal
 └───新文档快捷方式的默认位置。

30: PrintHood
 └───用户可用打印机。

31: Programs
 └───常用程序的快捷方式。

32: ProgramFiles
 └───64 位程序。

33: ProgramFilesCommon
 └───用户之间共享的程序和设置。

34: ProgramFilesX86
 └───64 位程序。

35: ProgramFilesCommonX86
 └───用户之间共享的程序和设置。

36: Recent
 └───最近使用项目的快捷方式。

37: RecycleBinFolder
 └───已删除的项目。

38: SendTo
 └───可发送到其他用户的项目的快捷方式。

39: Start Menu
 └───新开始菜单快捷方式的默认位置。

40: Startup
 └───用户登录时自动启动的程序。

41: Templates
 └───可用于创建新文档或其他项目的模板。

42: UserFilesFolder
 └───特定于当前用户的文件。

43: UsersLibrariesFolder
 └───文档、音乐和其他文件的集合。

请输入要打开的文件夹的编号：(输入 q 退出)

```
