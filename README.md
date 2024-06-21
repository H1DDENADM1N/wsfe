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

3: CD Burning
 └───This folder is used to hold CDs that are in the process of being burned.

4: Cache
 └───This folder is used to cache application data for faster access.

5: Common Administrative Tools
 └───This folder contains tools and settings that are available to all users on a Windows system.

6: Common AppData
 └───This folder contains application data that is shared across all users on the system.        

7: Common Desktop
 └───This folder is the default location for new desktop shortcuts.

8: Common Documents
 └───This folder is the default location for new document shortcuts.

9: Common Programs
 └───This folder contains shortcuts to programs that are commonly used.

10: Common Start Menu
 └───This folder is the default location for new start menu shortcuts.

11: Common Startup
 └───This folder contains programs that are started automatically when a user logs on.

12: Common Templates
 └───This folder contains templates that can be used to create new documents or other items.

13: CommonMusic
 └───This folder contains music files.

14: CommonPictures
 └───This folder contains pictures.

15: CommonVideo
 └───This folder contains video files.

16: Cookies
 └───This folder contains cookies.

17: Desktop
 └───This folder is the default location for new desktop shortcuts.

18: Favorites
 └───This folder contains shortcuts to items that the user has marked as favorite.

19: Fonts
 └───This folder contains font files.

20: History
 └───This folder contains a history of the user's activities.

21: Local AppData
 └───This folder contains application data that is specific to the current user.

22: My Music
 └───This folder contains music files.

23: My Pictures
 └───This folder contains pictures.

24: My Video
 └───This folder contains video files.

25: NetHood
 └───This folder contains network shortcuts.

26: OEM Links
 └───This folder contains links to manufacturer-specific drivers and utilities.

27: Personal
 └───This folder is the default location for new document shortcuts.

28: PrintHood
 └───This folder contains printers that are available to the user.

29: Programs
 └───This folder contains shortcuts to programs that are commonly used.

30: Recent
 └───This folder contains shortcuts to recently used items.

31: SendTo
 └───This folder contains shortcuts to items that can be sent to other users.

32: Start Menu
 └───This folder is the default location for new start menu shortcuts.

33: Startup
 └───This folder contains programs that are started automatically when a user logs on.

34: Templates
 └───This folder contains templates that can be used to create new documents or other items.

Enter the number of the folder you want to open: (enter q to exit)

```

```python
1: Administrative Tools
 └───管理员在 Windows 系统上可用的工具和设置。 

2: AppData
 └───当前用户的应用程序数据。

3: CD Burning
 └───保存即将烧录的 CD。

4: Cache
 └───缓存应用程序数据以提高访问速度。

5: Common Administrative Tools
 └───Windows 系统上所有用户都可用的工具和设置。

6: Common AppData
 └───系统上所有用户共享的应用程序数据。        

7: Common Desktop
 └───新桌面快捷方式的默认位置。

8: Common Documents
 └───新文档快捷方式的默认位置。

9: Common Programs
 └───常用程序的快捷方式。

10: Common Start Menu
 └───新开始菜单快捷方式的默认位置。

11: Common Startup
 └───用户登录时自动启动的程序。

12: Common Templates
 └───可用于创建新文档或其他项目的模板。

13: CommonMusic
 └───音乐文件。

14: CommonPictures
 └───图片。

15: CommonVideo
 └───视频文件。

16: Cookies
 └───Cookie。

17: Desktop
 └───新桌面快捷方式的默认位置。

18: Favorites
 └───用户标记为收藏的项目的快捷方式。

19: Fonts
 └───字体文件。

20: History
 └───用户活动的历史记录。

21: Local AppData
 └───特定于当前用户的应用程序数据。

22: My Music
 └───音乐文件。

23: My Pictures
 └───图片。

24: My Video
 └───视频文件。

25: NetHood
 └───网络快捷方式。

26: OEM Links
 └───制造商驱动程序和实用程序的链接。

27: Personal
 └───新文档快捷方式的默认位置。

28: PrintHood
 └───用户可用打印机。

29: Programs
 └───常用程序的快捷方式。

30: Recent
 └───最近使用项目的快捷方式。

31: SendTo
 └───可发送到其他用户的项目的快捷方式。

32: Start Menu
 └───新开始菜单快捷方式的默认位置。

33: Startup
 └───用户登录时自动启动的程序。

34: Templates
 └───可用于创建新文档或其他项目的模板。

请输入要打开的文件夹的编号：(输入 q 退出)

```
