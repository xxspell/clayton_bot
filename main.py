from core.game import GameAutomation
from core.http import HttpClient
from utils.config import load_config, version, icon_path, common_headers
from utils.terminal import set_command_line_title, set_console_icon

config = load_config()

if __name__ == "__main__":
    set_command_line_title(None)
    set_console_icon(icon_path)
    def print_welcome():
        title = f"Welcome to Clayton Bot v{version}"
        message = "Your ultimate companion for automated gaming!"
        art = """
                  ,,
      .g8\"\"\"bgd `7MM                        mm                              `7MM\"\"\"Yp,             mm         
    .dP'     `M   MM                        MM                                MM    Yb             MM
    dM'       `   MM   ,6\"Yb.  `7M'   `MF'mmMMmm   ,pW\"Wq.  `7MMpMMMb.        MM    dP  ,pW\"Wq.  mmMMmm
    MM            MM  8)   MM    VA   ,V    MM    6W'   `Wb   MM    MM        MM\"\"\"bg. 6W'   `Wb   MM
    MM.           MM   ,pm9MM     VA ,V     MM    8M     M8   MM    MM        MM    `Y 8M     M8   MM
    `Mb.     ,'   MM  8M   MM      VVV      MM    YA.   ,A9   MM    MM        MM    ,9 YA.   ,A9   MM
      `\"bmmmd'  .JMML.`Moo9^Yo.    ,V       `Mbmo  `Ybmd9'  .JMML  JMML.    .JMMmmmd9   `Ybmd9'    `Mbmo
                                  ,V
                               OOb\"
    """

        max_length = max(len(title), len(message), max(len(line) for line in art.split("\n")))
        print("+" + "-" * (max_length + 2) + "+")
        print("|" + title.center(max_length + 2) + "|")
        print("|" + " " * (max_length + 2) + "|")
        for line in art.split("\n"):
            print("|  " + line.ljust(max_length) + "|")
        print("|" + " " * (max_length + 2) + "|")
        print("|" + message.center(max_length + 2) + "|")
        print("+" + "-" * (max_length + 2) + "+")
    print_welcome()

    if config:
        init_data = config['SETTINGS']['init_data']
        user_agent = config['SETTINGS']['user_agent']
        print(f"Init data: {init_data}")
        print(f"User Agent: {user_agent}")

        http_client = HttpClient(user_agent=user_agent, common_headers=common_headers)
        game_automation = GameAutomation(http_client, init_data)
        game_automation.run()
    else:
        print("Config is null")