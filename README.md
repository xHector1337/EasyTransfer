![Ekran görüntüsü 2024-09-07 170424](https://github.com/user-attachments/assets/8d4f5113-8438-4643-a940-eec87fc5c3b6)

Easy Transfer is a file server/uploading service I made in order to make file uploading to my Raspberry Pi easier. It is a bit buggy and might not be so secure. So, using it is your own risk.

# Installation

After cloning or downloading the repository open up `listener.py` with your favorite IDE. Then change `key` and `directory` variables if you wish. `Key` variable stores the security key and `directory` variable stores the directory which is going to store uploaded files.
Default key is `SKYFM` and default directory is `/var/www/html/easytransfer`.
Note: Don't forget to change `passkey` variable in `client.py` if you change default key.

# Usage

After saving your changes run `listener.py` with sudo. It'll ask you for port to be listened and your Pi's public ip address.
Then run `client.py` and answer questions with your listener's port and ip address. Finally, choose your file type (file or directory)
If you choose directory type, it'll upload every file in the directory.

Happy uploading!!!
