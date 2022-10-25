read -p  'Введите логин: ' login
read -s -p 'Введите пароль: ' password

c=0
for i in $(cat reg.txt)
do
    if [[ $i = $login ]]
    then
        c=$(( $c + 1))
    fi
    if [[ $i = $password ]]
    then 
        c=$(( $c + 1))
    fi

done

if [[ $c = 2 ]]
then
    echo -e "\ngreat job"
else
    echo -e "\nfalse"
fi
