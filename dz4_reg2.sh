#!/bin/bash
read -p  'Введите логин: ' login
read -s -p 'Введите пароль: ' password
echo "$login" >> reg.txt
echo "$password" >> reg.txt
