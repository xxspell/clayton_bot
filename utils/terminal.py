import sys
import ctypes

from utils.config import version

def set_console_icon(icon_path):
    if sys.platform.startswith('win32'):
        ctypes.windll.kernel32.SetConsoleIcon(ctypes.windll.shell32.ShellExecuteW(None, "open", icon_path, None, None, 1))


def set_command_line_title(user_data=None):
    if user_data:
        nickname = user_data.get('username', 'Unknown')
        tokens = user_data.get('tokens', 'Unknown')
        title = f"Clayton Bot v{version} | https://github.com/xxspell | User: {nickname}, Tokens: {tokens}"
    else:
        title = f"Clayton Bot v{version} | https://github.com/xxspell"

    if sys.platform.startswith('win32'):
        # Windows
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        # Unix
        sys.stdout.write(f"\x1b]2;{title}\x07")