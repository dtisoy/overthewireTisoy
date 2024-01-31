read -p "bandit level: " level
read -p "password: " pass

echo -e "bandit$level\npassword: $pass" > bandit"$level".txt

ssh bandit"$level"@bandit.labs.overthewire.org -p 2220
