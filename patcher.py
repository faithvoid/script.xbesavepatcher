import xbmc
import xbmcgui
import os

# Define the exact byte sequences for hex patterns (ASCII encoded paths).
OLD_TDATA_PATH = b"\x5C\x44\x65\x76\x69\x63\x65\x5C\x48\x61\x72\x64\x64\x69\x73\x6B\x30\x5C\x70\x61\x72\x74\x69\x74\x69\x6F\x6E\x31\x5C\x54\x44\x41\x54\x41"
OLD_UDATA_PATH = b"\x5C\x44\x65\x76\x69\x63\x65\x5C\x48\x61\x72\x64\x64\x69\x73\x6B\x30\x5C\x70\x61\x72\x74\x69\x74\x69\x6F\x6E\x31\x5C\x55\x44\x41\x54\x41"

NEW_TDATA_PATH = b"\x5C\x44\x65\x76\x69\x63\x65\x5C\x48\x61\x72\x64\x64\x69\x73\x6B\x30\x5C\x70\x61\x72\x74\x69\x74\x69\x6F\x6E\x36\x5C\x54\x44\x41\x54\x41"
NEW_UDATA_PATH = b"\x5C\x44\x65\x76\x69\x63\x65\x5C\x48\x61\x72\x64\x64\x69\x73\x6B\x30\x5C\x70\x61\x72\x74\x69\x74\x69\x6F\x6E\x36\x5C\x55\x44\x41\x54\x41"

class XBESavePatcher:
    def __init__(self):
        self.xbe_file_path = None
        self.save_directory = None
        self.save_filename = None

    def browse_for_file(self):
        # Prompt the user to select an .xbe file
        self.xbe_file_path = xbmcgui.Dialog().browse(1, 'Select .xbe file', 'files', '.xbe')
        if not self.xbe_file_path:
            xbmcgui.Dialog().ok("XBE Save Folder Patcher", "No file selected.")
            return False
        return True

    def choose_save_location_and_name(self):
        # Prompt user to select a folder for saving the new .xbe file
        self.save_directory = xbmcgui.Dialog().browse(0, 'Select Folder to Save .xbe', 'files')
        if not self.save_directory:
            xbmcgui.Dialog().ok("XBE Save Folder Patcher", "No save location selected.")
            return False

        # Prompt user for the filename using xbmc.Keyboard
        keyboard = xbmc.Keyboard('', 'Enter filename (without .xbe extension)')
        keyboard.doModal()
        if keyboard.isConfirmed():
            self.save_filename = keyboard.getText()
            if not self.save_filename:
                xbmcgui.Dialog().ok("XBE Save Folder Patcher", "No filename entered.")
                return False
        else:
            xbmcgui.Dialog().ok("XBE Save Folder Patcher", "Filename input canceled.")
            return False

        # Combine directory and filename to create full path
        self.save_file_path = os.path.join(self.save_directory, self.save_filename + ".xbe")
        return True

    def replace_hex(self):
        # Ensure an input file is selected
        if not self.xbe_file_path:
            xbmcgui.Dialog().ok("XBE Save Folder Patcher", "Please select an .xbe file first.")
            return

        try:
            with open(self.xbe_file_path, 'rb') as xbe_file:
                xbe_data = xbe_file.read()

                # Check if either OLD_TDATA_PATH or OLD_UDATA_PATH exists in xbe_data
                if OLD_TDATA_PATH not in xbe_data and OLD_UDATA_PATH not in xbe_data:
                    xbmcgui.Dialog().ok("Pattern Not Found", "Are you sure this game supports saving?")
                    return

                # Perform replacements: replace OLD_TDATA_PATH with NEW_TDATA_PATH and OLD_UDATA_PATH with NEW_UDATA_PATH
                xbe_data = xbe_data.replace(OLD_TDATA_PATH, NEW_TDATA_PATH)
                xbe_data = xbe_data.replace(OLD_UDATA_PATH, NEW_UDATA_PATH)

                # Write modified data to new file
                with open(self.save_file_path, 'wb') as new_xbe_file:
                    new_xbe_file.write(xbe_data)

                xbmcgui.Dialog().ok("XBE Save Folder Patcher", "File saved successfully!")

        except Exception as e:
            xbmcgui.Dialog().ok("XBE Save Folder Patcher", "Error: " + str(e))

    def run(self):
        # Step 1: Ask user to browse for the input file
        if not self.browse_for_file():
            return
        
        # Step 2: Ask user for save location and filename
        if not self.choose_save_location_and_name():
            return
        
        # Step 3: Perform hex replacement and save the modified file
        self.replace_hex()

# Main execution
if __name__ == '__main__':
    editor = XBESavePatcher()
    editor.run()
