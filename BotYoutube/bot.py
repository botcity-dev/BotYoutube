"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

import datetime
from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):

        self.maestro.alert(
            task_id=execution.task_id,
            title="BotYoutube - Inicio",
            message="Estamos iniciando o processo",
            alert_type=AlertType.INFO
        )

        self.browse("https://www.youtube.com/c/pythonbrasiloficial")

        if not self.find("sobre", matching=0.97, waiting_time=10000):
            self.not_found("sobre")
        self.click()

        if not self.find("inscritos", matching=0.97, waiting_time=10000):
            self.not_found("inscritos")
        self.double_click_relative(-39, 7)
        self.control_c()
        inscritos = self.get_clipboard()
        print(f"Inscritos => {inscritos}")

        if not self.find("visualizacoes", matching=0.97, waiting_time=10000):
            self.not_found("visualizacoes")
        self.double_click_relative(-28, 5)
        self.control_c()
        visualizacoes = self.get_clipboard()
        print(f"Visualizações => {visualizacoes}")

        self.maestro.new_log_entry(
            activity_label="EstatisticasYoutube",
            values={
                "data_hora": datetime.datetime.now().strftime("%Y-%m-%d_%H-%M"),
                "canal": "pythonbrasiloficial",
                "inscritos": inscritos,
                "visualizacoes": visualizacoes
            }
        )

        self.maestro.finish_task(
            task_id=execution.task_id,
            status=AutomationTaskFinishStatus.SUCCESS,
            message="Tarefa BotYoutube finalizada com sucesso"
        )

    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    Bot.main()
