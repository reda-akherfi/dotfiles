############################################################
## This is my own arch install script 
## It is a minimal one since all customization is done
## through my dotfiles' install.sh
############################################################


# making the font get bigger
echo "this is the font before:"
sleep 3
setfont ter-132b
echo "this is the font after"
sleep 3
clear

# set up the time
echo "configuring the time has begun"
sleep 3
timedatectl
timedatectl set-ntp true
timedatectl set-timezone Africa/Casablanca
echo "setting up the time has finished"
sleep 3
clear

# updating keyrings
echo "updating the keyrings "
sleep 3
pacman -Sy --needed --noconfirm archlinux-keyring
sleep 3
clear


# disk partitionning 
# $ parted [options] [device [command [options...]...]]
echo "partitionning the disk"
sleep 3
lsblk
DISK="here goes the disk"
read -p "enter the disk name in here, pay attention to typos" DISK


# menial tasks
# setting up the timezone
echo "setting up the timezone"
sleep 3
ln -sf /usr/share/zoneinfo/Africa/Casablanca /etc/localtime
# syncing the system to hardware clock
echo "syncing the system to hardware clock"
sleep 3
hwclock --systohc
# setting up the locale
echo "setting up the locale"
sleep 3
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen
locale-gen
# setting up the language
echo "setting up the language"
sleep 3
echo "LANG=en_US.UTF-8" > /etc/locale.conf
# host name stuff
echo "host name stuff"
sleep 3
echo homeworld16 > /etc/hostname
echo "127.0.0.1 localhost" >> /etc/hosts
echo "::1       localhost" >> /etc/hosts
echo "127.0.1.1 archmc.localdomain archmc" >> /etc/hosts


