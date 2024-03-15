#!/bin/bash


############################################################
### basic setup for the env itself
############################################################
# setting up the font inside the live env
read -p "Is the text small for your taste Mr Redaa? [Y/n] " text_small
if [ $text_small = "n" ]
then
    echo "Ok, we will continue using this font size Mr Reda/n"
    sleep 3
    clear
else 
    # making the font get bigger
    echo "making the font get bigger\n"
    echo "this is the font before:"
    sleep 3
    setfont ter-132b
    echo "this is the font after"
    sleep 3
    clear
fi

# set up the time
echo "configuring the time has begun\n"
sleep 3
timedatectl
# setting the ntp protocol true
echo "setting the ntp protocol true\n"
timedatectl set-ntp true
# setting up the time zone
echo "setting up the time zone\n"
timedatectl set-timezone Africa/Casablanca
echo "setting up the time has finished"
sleep 3
clear

# updating keyrings
echo "updating the keyrings \n"
sleep 3
pacman -Sy --needed --noconfirm archlinux-keyring
echo "just updated the keyring for arch \nwhatever that means!\n"
sleep 3
clear



############################################################
### partitionning the drives
############################################################
# choosing the drive
disk_is_selected=0
until [ $disk_is_selected -eq 1 ]
do
    echo "choosing the drive\n"
    sleep 3
    lsblk
    read -p "\nenter the name of the drive , beware of typos !!!\n" disk_name
    sleep 3
    echo "the disk you selected is $disk_name \n"
    read -p "Is this selection the right one ? [yes/No]" user_selected_disk
    if [ $user_selected_disk = "yes" ]
    then
        disk_is_selected=1
        echo "\nyou chose yes/n"
        sleep 3
        clear
    else 
        echo "you chose to repeat the selection \n"
        sleep 3
        clear
    fi
done

# $ parted [options] [device [command [options...]...]]
# partitionning the disk
partitionning_successful=0
until [ $partitionning_successful -eq 1 ]
do
    echo "partitionning the disk\n"
    sleep 3
    # use parted
    echo "use parted\n"
    # creating the gpt label
    echo "creating the gpt label\n"
    parted --fix --script $disk_name mklabel "gpt"
    sleep 3
    # making the efi partition
    echo "making the efi partition\n"
    sleep 3
    parted --fix --script $disk_name mkpart "fat32" 1MiB 512MiB
    # setting the bootable flag for the efi partition
    echo "setting the bootable flag for the efi partition\n"
    sleep 3
    parted --fix --script $disk_name set 1 esp on
    # making the root partition as the rest of the disk
    echo "making the root partition as the rest of the disk\n"
    sleep 3
    parted --fix --script $disk_name mkpart "primary" "ext4" 512MiB 100%
    clear
    parted --script ${disk_name} print list
    read -p "is this partioning scheme acceptable? [yes/No] " user_partitioning_answer
    if [ $user_partitioning_answer = "yes" ]
    then
        echo "you have selected the cuurent partitionning scheme\n"
        partitionning_successful=1
        sleep 3
        clear
    else
        echo "something went wrong with the partitionning \n going at it again but you might want to rewrite the script\n"
        sleep 2
        clear
    fi
done

# making the file system -- formatting
echo "making the file system -- formatting\n"
sleep 3
# formatting the efi partition
echo "formatting the efi partition in vfat 32\n"
sleep 3
mkfs.vfat -F32 -n "EFISYSTEM" "${disk_name}1"
# formatting the root partition 
echo "formatting the root partition in ext4\n"
sleep 3
mkfs.ext4 -L "ROOT" "${disk_name}2"
clear

# mounting the partitions
echo "mounting the partitions\n"
sleep 3
# mouting the root parttion into /mnt
echo "mouting the root parttion into /mnt\n"
sleep 3
mount -t ext4 ${disk_name}2 /mnt
# mounting the efi part to /mnt/boot
echo "mounting the efi part to /mnt/boot\n"
sleep 3
mkdir /mnt/boot
mount -t vfat  ${disk_name}1 /mnt/boot
sleep 3
clear


############################################################
### installing software
############################################################
# chrooting to the live env
echo "installing software"
pacstrap -k /mnt base linux linux-firmware intel-ucode networkmanager
echo "all software has been installed successfully !\n"
sleep 3

############################################################
### before chrooting
############################################################
# generating the fstab file
echo "generating the fstab file "
sleep 2
genfstab -U /mnt >> /mnt/etc/fstab
echo "fstab has been generated\n"
sleep 3
clear

# extracting the UUID of the root partition using a bit of awk magic
echo "extracting the UUID of the root partition using a bit of awk magic\n"
sleep 3
# downloading bat in the live env to easily get the line number for the UUID
echo "downloading bat in the live env to easily get the line number for the UUID\n"
sleep 3
pacman -Sy bat --noconfirm --needed
sleep 2
clear
# selecting the line and field numbers [ the field sep is <Space> by default ]
uuid_target_acquired=0
root_uuid=""
until [ $uuid_target_acquired -eq 1 ]
do
    bat /mnt/etc/fstab
    read -p "Enter the line number : " $line_number
    read -p "Enter the field number : " $field_number
    root_uuid=$(awk -v line=$line_number -v field=$field_number -- ' NR == line { print $field } ' /mnt/etc/fstab)
    clear
    bat /mnt/etc/fstab
    echo "the root UUID is  : $root_uuid \n"
    read -p "Is that accurate? [yes/No] " answer
    if [ $anwser = "yes" ]
    then
        echo "you chose yes\n"
        uuid_target_acquired=1
        sleep 3
        clear
    else
        echo "let's go again\n"
        sleep 3
        clear
    fi
done

# install the bootloader
echo "install the bootloader\n"
sleep 3
# installing the booloader on /mnt/boot
echo "installing the booloader on /mnt/boot\n"
sleep 2
bootctl install --path /mnt/boot
# setting up arch.conf as my default boot entry
echo "setting up arch.conf as my default boot entry\n"
sleep 3
echo "default arch.conf" >> /mnt/boot/loader/loader.conf
# setting up the boot entry itself
echo "setting up the boot entry itself\n"
sleep 3
cat <<EOF > /mnt/boot/loader/entries/arch.conf
title Arch Linux
linux /vmlinuz-linux
initrd /intel-ucode.img
initrd /initramfs-linux.img
options root=$(root_uuid) rw
EOF
clear
echo "here is the the boot entery:\n"
sleep 2
bat /mnt/boot/loader/entries/arch.conf
sleep 6
clear

    



############################################################
### the inside chroot script setup
### and copying it to it
############################################################
cat <<ENDE > /mnt/inside_script.sh

#!/bin/bash

############################################################
### Setting up users
############################################################
# setting the password for the root user
echo "setting the password for the root user\n"
echo root:Tzbg5340 | chpasswd
sleep 3
# adding a new user
echo "adding a new user\n"
useradd -m reda --shell /bin/bash
sleep 3
# setting up the password for reda
echo "setting up the password for reda\n"
echo reda:1966 | chpasswd
sleep 3
# adding reda to certain groups
echo "adding reda to certain groups\n"
sed -i 's/^# %wheel ALL=(ALL:ALL) ALL/%wheel ALL=(ALL:ALL) ALL/' /etc/sudoers
usermod -a -G wheel,storage,power,audio reda
sleep 3

############################################################
### Performing menial tasks 
############################################################
# setting up the timezone
echo "setting up the timezone"
ln -sf /usr/share/zoneinfo/Africa/Casablanca /etc/localtime
sleep 3
# syncing the system to hardware clock
echo "syncing the system to hardware clock"
hwclock --systohc
sleep 3
# setting up the locale
echo "setting up the locale"
sed -i 's/^#en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen
sleep 3
locale-gen
sleep 3
# setting up the language
echo "setting up the language"
echo "LANG=en_US.UTF-8" > /etc/locale.conf
sleep 3
# host name stuff
echo "host name stuff"
sleep 3
#setting up the host name
echo "setting up the host name\n"
echo homeworld16 > /etc/hostname
sleep 2
# setting  up the /etc/hosts file
echo "setting  up the /etc/hosts file\n"
cat <<EOF > /etc/hosts
127.0.0.1 localhost
::1       localhost
127.0.1.1 archmc.localdomain archmc
EOF
sleep 2


############################################################
### misc
############################################################
# enabling the NetworkManager service
echo "enabling the NetworkManager service\n"
systemctl enable NetworkManager.service
ENDE
arch-chroot /mnt sh ./inside_script.sh

echo "\n\n the installation has finished you can reboot now"
