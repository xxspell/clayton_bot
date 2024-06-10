import json
import random
import time
import logging

from datetime import datetime, timedelta
from utils.config import load_config
from utils.terminal import set_command_line_title

config = load_config()

class GameAutomation:
    def __init__(self, http_client, init_data):
        self.logged_in = False
        self.active_farm = False
        self.start_time = None
        self.user_data = {}
        self.http_client = http_client

        self.setup_logger()
        self.http_client.add_header("Init-Data", init_data)

    def setup_logger(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(username)s | %(action)s | %(tokens)s (%(session_tokens)s)')


        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)


        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def login(self):
        response = self.http_client.post('https://tonclayton.fun/api/user/login')

        if response:
            self.process_login_response(response)
            self.logged_in = True

    def process_login_response(self, response):
        if response is None:
            self.logger.error("No response to process.")
            return

        try:
            data = response if isinstance(response, dict) else json.loads(response)

            if "user" in data:
                self.user_data = data["user"]
                self.active_farm = self.user_data.get('active_farm', False)
                start_time_str = self.user_data.get('start_time')
                if start_time_str:
                    self.start_time = datetime.strptime(start_time_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                    self.start_time += timedelta(hours=6)

            self.log_action("logged in", self.user_data.get('tokens', 0))
            set_command_line_title(user_data=self.user_data)

        except json.JSONDecodeError as e:
            self.log_action(f"Error processing JSON: {e}", self.user_data.get('tokens', 0))

    def start_farm(self):
        response = self.http_client.post('https://tonclayton.fun/api/user/start')
        if response:
            self.log_action("Game started successfully.", self.user_data.get('tokens', 0))
        else:
            self.log_action("Failed to start game.", self.user_data.get('tokens', 0))
        # self.logger.debug(response)

        set_command_line_title(user_data=self.user_data)

    def start_game(self):
        response = self.http_client.post('https://tonclayton.fun/api/game/start')
        if response:
            self.log_action("Game start successfully.", self.user_data.get('tokens', 0))
        else:
            self.log_action("Failed to start game.", self.user_data.get('tokens', 0))
        # self.logger.debug(response)

        set_command_line_title(user_data=self.user_data)

    def end_game(self):
        response = self.http_client.post('https://tonclayton.fun/api/game/end', json={"maxTile": 256})
        if response:
            self.log_action("Game ended successfully.", self.user_data.get('tokens', 0))
        else:
            self.log_action("Failed to end game.", self.user_data.get('tokens', 0))
        # self.logger.debug(response)

        set_command_line_title(user_data=self.user_data)

    def log_action(self, action, session_tokens):
        log_data = {
            'username': self.user_data.get('username', 'Unknown'),
            'action': action,
            'tokens': self.user_data.get('tokens', 0),
            'session_tokens': session_tokens
        }
        self.logger.info('', extra=log_data)

    def run(self):
        while True:
            if not self.logged_in:
                self.login()

            if not self.active_farm:
                self.start_farm()

            if self.start_time:
                current_time = datetime.utcnow()
                if current_time > self.start_time:
                    time_difference = current_time - self.start_time
                    self.log_action(f"Time until end: {time_difference}", self.user_data.get('tokens', 0))
                    self.start_game()
                    self.log_action("game start", self.user_data.get('tokens', 0))
                    wait_time = random.randint(72, 120)
                    self.log_action(f"Waiting for {wait_time} seconds...", self.user_data.get('tokens', 0))
                    time.sleep(wait_time)
                    self.end_game()
                    self.log_action("game end", self.user_data.get('tokens', 0))
                    self.start_time = None
                else:
                    time_difference = self.start_time - current_time
                    self.log_action(f"Waiting for {time_difference} until game start...", self.user_data.get('tokens', 0))
                    time.sleep((self.start_time - current_time).total_seconds())