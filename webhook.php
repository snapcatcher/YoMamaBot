<?php
$json = json_decode(file_get_contents('php://input'), true);

$chat_id = $json['message']['chat']['id'];
$message = $json['message']['text'];

$command = escapeshellcmd('/usr/bin/python /var/www/yomama/YoMamaBot.py ' . $chat_id . ' ' . $message);

shell_exec($command);

?>