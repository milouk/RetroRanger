import pygame
import pygame_gui


class Keyboard:
    def __init__(self, gui_manager, search_input):
        self.gui_manager = gui_manager
        self.search_input = search_input

        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((25, 220), (590, 230)),  # Increase the y-coordinate here
            manager=self.gui_manager,
        )
        # Don't show the panel initially
        self.panel.hide()
        self.panel.panel_container.hide()
        self.showing = False

        # Make sure it's on top
        self.panel.change_layer(10)
        self.panel.panel_container.change_layer(10)

        button_width = 45
        button_height = 30
        key_spacing = 10
        key_start_x = 20
        key_start_y = 20

        keys = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "q",
            "w",
            "e",
            "r",
            "t",
            "y",
            "u",
            "i",
            "o",
            "p",
            "a",
            "s",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "z",
            "x",
            "c",
            "v",
            "b",
            "n",
            "m",
            ",",
            ".",
            "?",
            "!",
            "Close",
            "Space",
            "Bksp",
        ]

        for i, key in enumerate(keys):
            row = i // 10
            col = i % 10
            rect = pygame.Rect(
                (
                    key_start_x + col * (button_width + key_spacing),
                    key_start_y + row * (button_height + key_spacing),
                ),
                (button_width, button_height),
            )
            if key == "Bksp":
                rect = pygame.Rect(
                    (460, key_start_y + row * (button_height + key_spacing)),
                    (100, button_height),
                )
            elif key == "Close":
                rect = pygame.Rect(
                    (
                        key_start_x + col * (button_width + key_spacing),
                        key_start_y + row * (button_height + key_spacing),
                    ),
                    (100, button_height),
                )
            elif key == "Space":
                rect = pygame.Rect(
                    (130, key_start_y + row * (button_height + key_spacing)),
                    (320, button_height),
                )

            button = pygame_gui.elements.UIButton(
                relative_rect=rect,
                text=key,
                manager=self.gui_manager,
                container=self.panel,
                object_id=i,
            )

            button.callback = self._on_key_press

    def close_panel(self):
        self.panel.hide()
        self.panel.panel_container.hide()
    
    def open_panel(self):
        self.panel.show()
        self.panel.panel_container.show()

        self.button_list_main = []

    def _on_key_press(self, button):
        print(f"Button {button.text} was pressed.")
        self.search_input.set_text(self.search_input.get_text() + button.text)
