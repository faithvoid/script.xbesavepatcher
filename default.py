import xbmc
import xbmcgui
import xml.etree.ElementTree as ET
import sys

def main():
    dialog = xbmcgui.Dialog()
    feeds = [
        ("- Primary HDD -", ""),
        ("Patch .XBE Save Location (E:\ to F:\)", "RunScript(Q:\\scripts\\XBESavePatcher\\patcher.py)"),
        ("Unpatch .XBE Save Location (F:\ to E:\)", "RunScript(Q:\\scripts\\XBESavePatcher\\unpatcher.py)"),
        ("- Secondary HDD | \Device\Harddisk0\Partition1 -", ""),
        ("Patch .XBE Save Location (E:\ to H:\)", "RunScript(Q:\\scripts\\XBESavePatcher\\patcherdualhdd.py)"),
        ("Unpatch .XBE Save Location (H:\ to E:\)", "RunScript(Q:\\scripts\\XBESavePatcher\\unpatcherdualhdd.py)"),
        ("- Utilities -", ""),
        ("Check .XBE Save Location", "RunScript(Q:\\scripts\\XBESavePatcher\\checker.py)"),
    ]
    
    feed_list = [name for name, _ in feeds]
    selected = dialog.select(u"XBE Save Patcher - Menu", feed_list)
    
    if selected >= 0:
        name, url = feeds[selected]
        if "RunScript" in url:
            xbmc.executebuiltin(url)

if __name__ == '__main__':
    main()
