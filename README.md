# Автоматический запуск скрипта Python на MacOS с помощью launchd

1. **Создайте файл планировщика:**

   ```bash
   sudo nano /Library/LaunchDaemons/com.user.notion_update.plist
   ```

2. **Вставьте следующее содержимое:**

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.notion_update</string>
       <key>ProgramArguments</key>
       <array>
           <string>/usr/local/bin/python3</string>
           <string>Ваш путь к файлу notion_update.py</string>
       </array>
       <key>StartInterval</key>
       <integer>60</integer>
       <key>RunAtLoad</key>
       <true/>
       <key>StandardOutPath</key>
       <string>Ваш путь к файлу notion_update.log</string>
       <key>StandardErrorPath</key>
       <string>Ваш путь к файлу notion_update_error.log</string>
   </dict>
   </plist>
   ```

3. **Сохраните файл и установите права:**

   Для сохранения файла нажмите **Ctrl+O**, затем **Ctrl+X**, чтобы выйти из редактора.  
   Установите правильные права доступа:

   ```bash
   sudo chmod 644 /Library/LaunchDaemons/com.user.notion_update.plist
   ```

4. **Загрузите задачу:**

   Выполните команду для загрузки задачи:

   ```bash
   sudo launchctl load /Library/LaunchDaemons/com.user.notion_update.plist
   ```

5. **Проверьте, работает ли задача:**

   Используйте следующую команду, чтобы убедиться, что задача добавлена:

   ```bash
   launchctl list | grep com.user.notion_update
   ```
